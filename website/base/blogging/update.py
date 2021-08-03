import os
import shutil
from bs4 import BeautifulSoup
from pathlib import Path

PAGE_LIMIT = 10
PAGE_TEMPLATE_PATH = os.path.join('..', 'templates', 'base', 'blog_page.html')

BLOGGING_DIR        = Path(__file__).resolve().parent
ENTRIES_DIR         = BLOGGING_DIR.joinpath('entries')
BASE_TEMPLATES_DIR  = BLOGGING_DIR.parent.joinpath('templates', 'base')
BLOG_PAGE_TEMPLATE  = BASE_TEMPLATES_DIR.joinpath('blog_page.html')
BLOG_ENTRY_TEMPLATE = BASE_TEMPLATES_DIR.joinpath('blog_entry.html')
BLOG_PAGES          = BASE_TEMPLATES_DIR.joinpath('blog-pages')
BLOG_ENTRIES        = BASE_TEMPLATES_DIR.joinpath('blog-entries')

entries = sorted(ENTRIES_DIR.glob('*.html'))
# https://stackoverflow.com/a/17511341
last_page = -(-len(entries) // PAGE_LIMIT)  

page = 0 # will immediately turn to 1 in first iteration; 0 mod n = 0
for counter, html in enumerate(entries):
    # add to blog-entries
    dest = BLOG_ENTRIES.joinpath(html.name.split('_')[0] + '.html')
    dest.write_text(html.read_text())

    # add to blog-pages
    if counter % PAGE_LIMIT == 0:
        page += 1

    with open(BLOG_PAGE_TEMPLATE, 'r') as f:
        replacing_dict = {
            'FIRST_PAGE': '1',
            'PREVIOUS_PAGE': str(page - 1) if page != 1 else 1,
            'CURRENT_PAGE': str(page),
            'NEXT_PAGE': str(page + 1) if page (!= last_page) else
            
        }
        txt = f.read()
        soup = BeautifulSoup(f.read(), 'html.parser')
        print(soup.get_text())
        for pagination in soup.find_all('p', 'blog-pages-pagination'):
            pagination.replace_with
        print(soup)
        


