import fitz
import json

doc = fitz.open('고등학교 정보_(주)도서출판 길벗.pdf')
targets = ['변수와 자료형', '다차원 데이터 구조', '제어 구조', '객체와 클래스', '프로그램 공유 및 성능 평가', '인공지능의 이해', '기계학습의 이해', '지능 에이전트의 이해']
res = {t: [] for t in targets}

for i in range(doc.page_count):
    text = doc[i].get_text('text').replace('\n', ' ')
    for t in targets:
        if t in text:
            res[t].append(i)

with open('pages_found.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
