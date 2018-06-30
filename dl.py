from pathlib import Path
import re
from bs4 import BeautifulSoup
import requests

def getChapter():
    return 900

def get_url_image(chapter, page):
    page = requests.get(f"https://scantrad.fr/mangas/one-piece/{chapter}?page={page}")
    soup = BeautifulSoup(page.content, "html.parser")
    list_link = soup.find_all('img')
    for link in list_link:
        if "display" in str(link):
            return filter_url(str(link))
    return None

def filter_url(html_img_tag):
    url = re.search(r'https.*\.png', html_img_tag).group(0)
    return url

def dowload_image(url, name):
    r = requests.get(url)
    open(name, 'wb').write(r.content)

def dl_chapter(chapter):
    path = Path(f"./{chapter}")
    path.mkdir()

    page = 1
    url = get_url_image(chapter, page)
    while url:
        dowload_image(url, f"./{chapter}/{page}")
        page += 1
        url = get_url_image(chapter, page)
if __name__ == '__main__':
    print("main")
