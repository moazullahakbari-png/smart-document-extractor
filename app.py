import fitz
import pytesseract
from PIL import Image
import streamlit as st

import csv
import io
import os

from pypdf import PdfReader
from pypdf.errors import PdfReadError
from main import extract_data

if os.name == "nt":
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    if os.path.exists(tesseract_path):
        pytesseract.pytesseract.tesseract_cmd = tesseract_path 


st.title("Less Confusing. More Focus.")

st.subheader("Smart Document Extractor")

st.write(
    "Spend less time copying information by hand."
)

st.write(
    "Upload TXT, CSV, or text-based PDF files, "
    "review the results, and download them as CSV."
)

with st.expander("Supported files and current limits"):
    st.markdown("""
    **Supported files**
    - TXT: Simple field-and-value text
    - CSV: Tables with column headers
    - PDF: Text-based and scanned PDF documents (English OCR)

    **Current limits**
    - OCR works best with clear, printed English text.
    - Complex PDF layouts and tables may not be preserved accurately.
    - Please review extracted data before using it.
    """)


uploaded_files = st.file_uploader(
    "Choose documents",
    type=["txt", "csv", "pdf"],
    accept_multiple_files=True  
)


for file_index, uploaded_file in enumerate(uploaded_files or []):

    st.divider()
    st.subheader(f"File: {uploaded_file.name}")

    try:
        file_bytes = uploaded_file.getvalue()
        filename = uploaded_file.name.lower()
        original_name = os.path.splitext(uploaded_file.name)[0]
        output_filename = f"{original_name}_extracted.csv"

        # TXT processing
        if filename.endswith(".txt"):
            content = file_bytes.decode("utf-8-sig")
            data = extract_data(content)

            if not data:
                st.warning("No data found in the TXT file.")
                continue

            rows = [
                {"Field": key, "Value": value}
                for key, value in data.items()
            ]

            st.metric("Fields extracted", len(data))
            st.dataframe(rows, use_container_width=True)

            output = io.StringIO(newline="")
            writer = csv.writer(output)
            writer.writerow(["Field", "Value"])
            writer.writerows(data.items())

            st.download_button(
                "Download CSV",
                data=output.getvalue().encode("utf-8-sig"),
                file_name=output_filename,
                mime="text/csv",
                key=f"download_{file_index}"
            )

        # CSV processing
        elif filename.endswith(".csv"):
            content = file_bytes.decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(content))
            rows = list(reader)

            if not reader.fieldnames:
                st.warning("The CSV file has no column headers.")
                continue

            if not rows:
                st.warning("The CSV file has no data rows.")
                continue

            st.metric("Rows found", len(rows))
            st.dataframe(rows, use_container_width=True)

            output = io.StringIO(newline="")
            writer = csv.DictWriter(
                output,
                fieldnames=reader.fieldnames
            )
            writer.writeheader()
            writer.writerows(rows)

            st.download_button(
                "Download CSV",
                data=output.getvalue().encode("utf-8-sig"),
                file_name=output_filename,
                mime="text/csv",
                key=f"download_{file_index}"
            )

       
        # PDF processing
        elif filename.lower().endswith(".pdf"):
            reader = PdfReader(io.BytesIO(file_bytes))

            if reader.is_encrypted:
                st.warning("This PDF is encrypted.")
                continue

            page_rows = []

            # Open the PDF for rendering pages as images
            pdf_document = fitz.open(
                stream=file_bytes,
                filetype="pdf"
            )

            try:
                for page_number, page in enumerate(
                    reader.pages, start=1
                ):
                    text = page.extract_text() or ""

                    # Use OCR when this page has no extractable text
                    if not text.strip():
                        pdf_page = pdf_document[page_number - 1]

                        pix = pdf_page.get_pixmap(
                            matrix=fitz.Matrix(2, 2),
                            alpha=False
                        )

                        image = Image.frombytes(
                            "RGB",
                            [pix.width, pix.height],
                            pix.samples
                        )

                        text = pytesseract.image_to_string(
                            image,
                            lang="eng"
                        )

                    if text.strip():
                        page_rows.append({
                            "Page": page_number,
                            "Text": text.strip()
                        })

            finally:
                pdf_document.close()

            if not page_rows:
                st.warning(
                    "No text could be extracted from this PDF."
                )
                continue

            st.metric("Pages with extracted text", len(page_rows))
            st.dataframe(page_rows, use_container_width=True)

            output = io.StringIO(newline="")
            writer = csv.DictWriter(
                output,
                fieldnames=["Page", "Text"]
            )
            writer.writeheader()
            writer.writerows(page_rows)

            st.download_button(
                "Download extracted PDF text",
                data=output.getvalue().encode("utf-8-sig"),
                file_name="extracted_pdf_text.csv",
                mime="text/csv",
                key=f"download_{file_index}"
            )

    except (
        UnicodeDecodeError,
        csv.Error,
        OSError,
        ValueError,
        PdfReadError
    ) as error:
        st.error(f"Could not process this file: {error}")