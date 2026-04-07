import os
import glob

base_dir = r"c:\Users\SDHS\Desktop\Anti\class_study"
target_dir = os.path.join(base_dir, "정보(2022개정)")
old_index_path = os.path.join(target_dir, "index.html")
new_index_path = os.path.join(base_dir, "index.html")

# 1. index.html 읽어서 링크 수정하기
if os.path.exists(old_index_path):
    with open(old_index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # href="xxx.html" 을 href="정보(2022개정)/xxx.html" 로 바꾼다. (ch1, ch2 이런 앵커 태그는 피하기)
    # 정규식 대신 파싱? 단순하게 .html" 로 끝나는 로컬 링크 앞에 폴더명을 붙입니다.
    # 예: href="1-1-1. 네트워크의 이해.html" -> href="정보(2022개정)/1-1-1. 네트워크의 이해.html"
    import re
    # href="1-1-1 부터 4-2-4 같은 걸 찾아야 함
    # 혹은 href=" 로 시작하고 .html" 로 끝나는 문자열 중 "http"가 없는 것
    def replacer(match):
        link = match.group(1)
        if link.startswith('http') or link.startswith('#') or '/' in link:
            return f'href="{link}"'
        else:
            # 특수문자 처리를 원활히 하기 위해 URL 인코딩은 굳이 안해도 모던 브라우저가 처리
            # 폴더명이 정보(2022개정)
            return f'href="정보(2022개정)/{link}"'
            
    index_content = re.sub(r'href="([^"]+\.html)"', replacer, index_content)
    
    # 수정된 내용을 새 위치에 쓰기
    with open(new_index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    # 원본 index 삭제
    os.remove(old_index_path)
    print("Moved and updated index.html to parent folder")

# 2. 정보(2022개정) 내의 모든 html 파일에서 메인으로 경로 수정
html_files = glob.glob(os.path.join(target_dir, '*.html'))
for file_path in html_files:
    if os.path.basename(file_path) == 'index.html':
        continue # 혹시 몰라 스킵
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # <a href="index.html" class="absolute 을 <a href="../index.html" class="absolute 로
    if 'href="index.html"' in content:
        content = content.replace('href="index.html"', 'href="../index.html"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated back links for {os.path.basename(file_path)}")

print("All tasks complete!")
