
import csv
import os


def extract_data(content):
    data = {}
    lines = content.splitlines()

    for line in lines:
        if ":" not in line:
            continue

        rr = line.split(":", 1)
        data[rr[0].strip()] = rr[1].strip()

    return data


def extract_csv(filename):
    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_output(output_filename, headers, rows):
    with open(output_filename, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    filename = input("Enter file name: ").strip()

    if not filename:
        print("Please enter a file name")
        return

    output_filename = os.path.splitext(filename)[0] + "_output.csv"

    try:
        if filename.lower().endswith(".csv"):
            rows = extract_csv(filename)

            if not rows:
                print("CSV file has no data rows")
                return

            headers = list(rows[0].keys())
            output_rows = [list(row.values()) for row in rows]

        elif filename.lower().endswith(".txt"):
            with open(filename, encoding="utf-8-sig") as file:
                content = file.read()

            data = extract_data(content)

            if not data:
                print("No data found in text file")
                return

            headers = ["Field", "Value"]
            output_rows = list(data.items())

        else:
            print("Unsupported file type. Use TXT or CSV.")
            return

        save_output(output_filename, headers, output_rows)
        print(f"Data saved to {output_filename}")

    except FileNotFoundError:
        print("File not found")

    except (csv.Error, UnicodeDecodeError):
        print("Input file could not be read")


if __name__ == "__main__":
    main()

