import fitz

pdf_path = "고등학교 정보_(주)도서출판 길벗.pdf"
doc = fitz.open(pdf_path)

targets = [
    "추상화와 알고리즘",
    "빅데이터 분석",
    "빅데이터의 이해",
    "데이터 암호화",
    "데이터 압축"
]

results = {}
for target in targets:
    for i in range(15, len(doc)): # Skip ToC
        text = doc[i].get_text("text").replace("\n", " ")
        if target in text:
            results[target] = i
            break

print("Found chapters at PDF indices:")
for k, v in results.items():
    print(f"{k}: {v}")
    
    chunk = ""
    for j in range(v, min(v + 5, len(doc))):
        chunk += f"\n--- Page {j} ---\n"
        chunk += doc[j].get_text("text")
    
    filename = f"extract_{k.replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(chunk)
    print(f"Saved {filename}")
