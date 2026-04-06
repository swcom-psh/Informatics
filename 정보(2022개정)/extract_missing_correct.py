import fitz

doc = fitz.open('고등학교 정보_(주)도서출판 길벗.pdf')
extracts = [
    ("변수와 자료형", 110),
    ("다차원 데이터 구조", 118),
    ("제어 구조", 125),
    ("객체와 클래스", 137),
    ("프로그램 공유 및 성능 평가", 143),
    ("인공지능의 이해", 158),
    ("기계학습의 이해", 168),
    ("지능 에이전트의 이해", 161)
]

for name, start_page in extracts:
    chunk = ""
    for j in range(start_page, min(start_page + 5, len(doc))):
        chunk += f"\n--- Page {j} ---\n"
        chunk += doc[j].get_text("text")

    filename = f"extract_{name.replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(chunk)
    print(f"Extraction complete for {name}")
