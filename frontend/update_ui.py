import os
import re

dir_path = r'd:\Dikshya-PBS\FYP\dealfinder\frontend'

with open(os.path.join(dir_path, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header, nav, footer from index.html
header_match = re.search(r'(<header class="top-header">.*?</header>)', index_content, flags=re.DOTALL)
nav_match = re.search(r'(<nav class="navbar .*?</nav>)', index_content, flags=re.DOTALL)
footer_match = re.search(r'(<footer>.*?</footer>)', index_content, flags=re.DOTALL)

if not header_match or not nav_match or not footer_match:
    print("Could not find header, nav, or footer in index.html")
    exit(1)

header_block = header_match.group(1)
nav_block = nav_match.group(1)
footer_block = footer_match.group(1)

# Fix logo in header and footer
new_logo_html = '''<a href="index.html" class="logo">
                        <img src="logo.png" alt="DealFinder Logo">
                    </a>'''

# Replace the only <a href="index.html"> that contains the image
header_block = re.sub(r'<a href="index\.html">.*?</a>', new_logo_html, header_block, flags=re.DOTALL)
footer_block = re.sub(r'<a href="index\.html">.*?</a>', new_logo_html, footer_block, flags=re.DOTALL)

def add_wishlist_class(html_content):
    def replace_heart(match):
        attrs = match.group(1)
        if 'btn-wishlist' not in attrs:
            attrs = re.sub(r'class="([^"]*)"', r'class="\1 btn-wishlist"', attrs)
        return f"<i{attrs}></i>"
    
    html_content = re.sub(r'<i([^>]*fa-heart[^>]*)></i>', replace_heart, html_content)
    return html_content

html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip existing header, nav, footer, and any old banner
    content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav[^>]*>.*?</nav>', '', content, flags=re.DOTALL)
    content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Banner Section -->.*?</div>', '', content, flags=re.DOTALL)
    
    # Fix Wishlist buttons
    content = add_wishlist_class(content)
    
    # Insert header, nav, banner right after <body...>
    banner_html = ""
    if filename != 'index.html':
        title = filename.replace('.html', '').replace('-', ' ').title()
        # Some special cases
        if filename == 'faq.html': title = 'FAQs'
        if filename == 'k-beauty.html': title = 'K-Beauty'
        banner_html = f'''
    <!-- Banner Section -->
    <div class="bg-secondary text-white py-5 text-center my-banner">
        <h1 class="display-5 fw-bold text-dark">{title}</h1>
        <p class="lead text-dark">Explore our {title} selection</p>
    </div>'''

    insertion = '\n' + header_block + '\n' + nav_block + '\n' + banner_html + '\n'
    
    # Need to escape backslashes for re.sub regex replacement string
    # Easiest way is lambda
    content = re.sub(r'(<body[^>]*>)', lambda m, ins=insertion: m.group(1) + ins, content, count=1)
    
    # Find where to insert footer block
    # Logic: insert before the first <script> tag that is below all main content, 
    # OR just before </body>.
    
    body_close_idx = content.rfind('</body>')
    # find scripts at the bottom
    script_idx = content.rfind('<script', 0, body_close_idx) if body_close_idx != -1 else content.rfind('<script')
    
    insert_idx = -1
    # Check if script_idx is at the bottom (within last 300 chars of body)
    if script_idx != -1 and body_close_idx != -1 and (body_close_idx - script_idx) < 300:
        insert_idx = script_idx
    elif body_close_idx != -1:
        insert_idx = body_close_idx

    if insert_idx != -1:
        content = content[:insert_idx] + '\n' + footer_block + '\n' + content[insert_idx:]
    else:
        # Fallback
        content += '\n' + footer_block
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully processed {len(html_files)} HTML files.")
