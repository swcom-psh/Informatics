import fitz

pdf_path = "고등학교 정보_(주)도서출판 길벗.pdf"
doc = fitz.open(pdf_path)

targets = [
    ("기계학습 프로젝트", 185),
    ("기계 학습 프로젝트", 185),
    ("기계학습의 유형", 160),
    ("사회 문제", 175)
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
        for j in range(found_idx, min(found_idx + 6, len(doc))):
            chunk += f"\n--- Page {j} ---\n"
            chunk += doc[j].get_text("text")

        filename = f"extract_{target.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(chunk)
        print(f"Saved {target} starting at page {found_idx}")
