import glob, os, re

files = glob.glob('*.html')
for f in files:
    if f == 'index.html' or f == 'template.html':
        continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<pre><code' in content and 'highlight.js' not in content:
        head_inject = '''
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/googlecode.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
</head>'''
        content = content.replace('</head>', head_inject)
        
        content = re.sub(r'<pre><code>', '<pre><code class="language-python">', content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
