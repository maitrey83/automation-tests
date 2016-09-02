from bs4 import BeautifulSoup
import requests
url = "https://www.overstock.com/Home-Garden/Kids-Furniture/Black~Brown~Grey~White,Faux-Leather~Steel,/color,material,/1455/cat.html?TID=SN:cat1455:::refinements-5-5:"
reqs = requests.get(url.rstrip('\n'))
soup = BeautifulSoup(reqs.content, 'html.parser')
for links in soup.findAll('a'):
    print(links.get('href'))