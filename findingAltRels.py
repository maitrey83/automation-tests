from bs4 import BeautifulSoup
import os
import os.path
import openpyxl
import requests
import logging

timeStamp='%(asctime)s %(message)s'
logFilePath = 'C:\\Users\\maitreypatel\\Desktop\\SEOTestCases\\LATTETestCases\\LATTE-1107\\logs\\LATTE-1107.log'
logger = logging.basicConfig(format=timeStamp,filename=logFilePath,level=logging.INFO)
path = "C:\\Users\\maitreypatel\\Desktop\\SEOTestCases\\LATTETestCases\\LATTE-1107"
currentPath = os.getcwd()
print(os.getcwd())

list = os.listdir()
os.chdir("C:\\Users\\maitreypatel\\Desktop\\SEOTestCases\\LATTETestCases\\LATTE-1107")
list = os.listdir()

wb = openpyxl.load_workbook("LATTE-1107 Test Data.xlsx")
valuesInSheet = wb.get_sheet_by_name('Sheet1')
cellValues = valuesInSheet.columns[0]
numOfRelCanUrls = 0

for cellObjects in cellValues:
    urls = cellObjects.value
    req = requests.get(urls)
    soup = BeautifulSoup(req.content, "html.parser")
    prettify = soup.prettify()
    relCans = soup.find("link", {"rel": "alternate"})
    logging.info("rel alternate is not displayed" + str(urls))
    logging.info(urls)
    if relCans != None:
        print(relCans)
        numOfRelCanUrls += 1
        logging.error("Alt canonical is present")

if numOfRelCanUrls == 0:
    print("There are no alternate Urls")
else:
    print("There are alternamte urls")
