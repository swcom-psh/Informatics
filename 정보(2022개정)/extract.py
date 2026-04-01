import fitz  # PyMuPDF

pdf_path = "고등학교 정보_(주)도서출판 길벗.pdf"
output_path = "extracted_text.txt"

# Open the document
doc = fitz.open(pdf_path)

# PDF pages are 0-indexed. Physical pages 96-101 corresponds to indices 95-100.
start_page = 95
end_page = 100

extracted_text = ""

# Make sure we don't go out of bounds
total_pages = len(doc)
end_page = min(end_page, total_pages - 1)

if start_page < total_pages:
    for page_num in range(start_page, end_page + 1):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        extracted_text += f"\n\n--- Page {page_num + 1} ---\n\n"
        extracted_text += text

with open(output_path, "w", encoding="utf-8") as f:
    f.write(extracted_text)

print(f"Extraction complete. Text saved to {output_path}")
