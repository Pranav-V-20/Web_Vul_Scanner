import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_forms(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.find_all("form")

def get_all_links(url):
    urls = set()
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            full_url = urljoin(url, href)
            if full_url.startswith("http"):
                urls.add(full_url)
    return list(urls)
