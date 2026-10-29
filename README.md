# Smart Document Extractor

### Spend Less Time Copying Data. Spend More Time Using It.

Smart Document Extractor is a simple tool that helps you extract information from text files, spreadsheets, and text-based PDF documents, then download the results as CSV files that can be opened in Excel.

No programming knowledge is needed to use the web interface.

## 1. What Problems Does It Solve?

Working with documents can involve a lot of repetitive tasks. You may need to open files one by one, find the information you need, copy it, organize it, and prepare it for a spreadsheet.

This can become frustrating when you have several files to process.

**Smart Document Extractor helps make these tasks easier.**

### Less Copying and Pasting

Instead of manually copying every piece of information from a supported text file, upload it and let the tool extract the available data.

### Easier Spreadsheet Preparation

Need information in a spreadsheet? Download the extracted results as a CSV file and open it in Microsoft Excel or another compatible spreadsheet application.

### Multiple Files in One Session

Have several documents? Upload multiple supported files in one session instead of processing each file in a separate run.

### Easier Document Review

View the processed information in a table before downloading it. This makes it easier to check the results and spot information that may need correction.

### A Simpler Workflow

You do not need to write Python code or manually enter file paths to use the web interface.

## 2. How Can It Help You?

This tool may be useful for:

- **Office workers:** Reduce repetitive data-entry work when handling supported documents.
- **Small businesses:** Prepare document data for spreadsheets and further processing.
- **Students and researchers:** Organize information from supported text files and PDFs.
- **Anyone handling multiple files:** Make routine document processing more convenient.

The tool is designed to assist with repetitive work, not to replace human review. Always check important results before using them in official records or business decisions.

## 3. Key Features

- **TXT extraction:** Extract information written in a format such as `Name: Ahmad`.
- **CSV processing:** Read and display tabular data.
- **PDF text extraction:** Extract available text from text-based PDF files, organized by page.
- **Multiple file uploads:** Process several supported documents in one session.
- **Downloadable results:** Export processed information as CSV files.
- **Clear output filenames:** Generate filenames based on the original uploaded filenames.
- **Helpful warnings:** Show messages when files are empty, CSV headers are missing, or a PDF has no extractable text.

## 4. How to Use It

1. Open the application in your web browser.
2. Upload one or more supported files.
3. Review the displayed results.
4. Download the generated CSV files.
5. Open the CSV files in Excel or another compatible spreadsheet application.

That's it! No programming knowledge is required to use the web interface.

## 5. Current Limitations

We are continuing to improve the tool and reduce these limitations.

- **Scanned PDFs and image-only documents:** The current version cannot read text contained only in images because OCR is not yet implemented.
- **Specific TXT structure:** TXT extraction currently works best with simple key-value lines, such as `Name: Ahmad`.
- **Complex PDF layouts:** Tables, columns, and complicated page layouts may not be extracted in the same structure as the original document.
- **Output format:** The current version produces CSV files, not fully formatted Excel workbooks.
- **Data accuracy:** Extracted results may require manual review, especially when documents have unusual formatting or inconsistent data.

## 6. What's Coming Next?

We are working toward making document processing more capable and convenient.

Planned improvements include:

- OCR to read scanned PDFs and images.
- Smarter extraction of names, dates, email addresses, and other useful information.
- Excel workbook export (`.xlsx`).
- Better handling of complex documents and unusual input.
- Additional automation features to reduce repetitive work.

These improvements are planned features and are not all available in the current version.

## 7. Privacy and Responsible Use

Only upload documents you are authorized to use.

Before using an online version, review its privacy arrangements and avoid uploading sensitive personal, financial, or confidential business information unless appropriate protections are in place.

## Project Status

**Version 1 — Core document extraction**

Currently supports TXT, CSV, and text-based PDF processing through a simple Streamlit interface.

## Feedback

Feedback and suggestions are welcome. They can help guide future improvements to the tool.
