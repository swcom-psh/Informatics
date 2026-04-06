import glob, os

files = glob.glob('*.html')
for f in files:
    if f == 'index.html':
        continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Only add if not already added
    if '메인으로</a>' not in content and '<div class="notebook-container">' in content:
        home_button = '''<div class="notebook-container">
        <!-- 홈으로 가기 버튼 -->
        <a href="index.html" class="absolute top-6 right-8 bg-slate-100 hover:bg-slate-200 text-slate-600 px-4 py-2 rounded-full font-bold text-sm shadow-sm transition border border-slate-200 flex items-center z-50" style="text-decoration:none;">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg> 
            메인으로
        </a>'''
        
        content = content.replace('<div class="notebook-container">', home_button)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Added home button to {f}')
