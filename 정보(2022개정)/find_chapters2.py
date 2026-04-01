import fitz

pdf_path = "고등학교 정보_(주)도서출판 길벗.pdf"
doc = fitz.open(pdf_path)

targets = [
    ("추상화와 알고리즘", 90),
    ("데이터 암호화", 55),
    ("빅데이터의 이해", 65),
    ("빅데이터 분석", 75)
]

for target, start_idx in targets:
    found_idx = -1
    for i in range(start_idx, len(doc)):
        text = doc[i].get_text("text").replace("\n", " ")
        if target in text:
            found_idx = i
            break
            
    if found_idx != -1:
        chunk = ""
        for j in range(found_idx, min(found_idx + 5, len(doc))):
            chunk += f"\n--- Page {j} ---\n"
            chunk += doc[j].get_text("text")

        filename = f"extract_{target.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(chunk)
        print(f"Saved {target} starting at page {found_idx}")
