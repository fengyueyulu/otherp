import re
from bs4 import BeautifulSoup

with open(r"../text/html1.html","r",encoding="utf-8") as f:
    html_note=f.read()
    soup=BeautifulSoup(html_note,"html.parser")
    print(soup.get_text())