from bs4 import BeautifulSoup
import requests
url = "https://www.overstock.com/"

def extract_links(url):
    reqs = requests.get(url.rstrip('\n'))
    soup = BeautifulSoup(reqs.content, 'html.parser')
    hrefs = []
    anchors = soup.findAll('a')
    for links in anchors:
        hrefs.append(links['href'])
    return hrefs
print(extract_links(url))
