import fitz
import sys

pdf_path = "고등학교 정보_(주)도서출판 길벗.pdf"
try:
    doc = fitz.open(pdf_path)
except Exception as e:
    print(f"Error opening pdf: {e}")
    sys.exit(1)

targets = [
    "네트워크의 이해",
    "네트워크의 환경",
    "사물 인터넷 시스템의 활용",
    "사물 인터넷 프로젝트를 위한 준비",
    "변수와 자료형",
    "다차원 데이터 구조", 
    "제어 구조",
    "객체와 클래스",
    "프로그램 공유 및 성능 평가",
    "인공지능의 이해",
    "기계학습의 이해",
    "지능 에이전트의 이해"
]

for target in targets:
    found_idx = -1
    for i in range(10, len(doc)): # Start from page 10 to skip initial TOC
        text = doc[i].get_text("text").replace("\n", " ")
        if target in text:
            # simple heuristic: the chapter title usually is quite prominent
            # but standard search is fine
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
    else:
        print(f"Could not find {target}")
