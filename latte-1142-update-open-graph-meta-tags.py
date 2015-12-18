import openpyxl
import os
import requests
from bs4 import BeautifulSoup

path = "C:\\Users\\maitreypatel\\Desktop\\"
workBook = "latte-1142-testdata.xlsx"
sheetName = "Sheet1"


def changeDirectory():
    changedir = os.chdir(path)

def getFacebookImages():
    getProducts = openpyxl.load_workbook(workBook).get_sheet_by_name(sheetName).columns[0]
    for products in getProducts:
        names = products.value
        req = requests.get(names)
        soup = BeautifulSoup(req.content,'html.parser')
        metaPropertyWidth = soup.find("meta", {"property":"og:image:width"})
        metaPropertyHeight  = soup.find("meta", {"property":"og:image:height"})
        metaUrl = soup.find("meta", {"property":"og:url"})
        #print(str(metaUrl))
        if metaPropertyWidth == None:
            print(str(metaUrl) + "No image size found")

changeDirectory()
getFacebookImages()
