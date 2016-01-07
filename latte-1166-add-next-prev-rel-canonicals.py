from bs4 import BeautifulSoup
import os
import os.path
import openpyxl
import requests
import logging

timeStamp='%(asctime)s %(message)s'
logFilePath = 'C:\\Users\\maitreypatel\\Desktop\\SEOTestCases\\LATTETestCases\\Logs\\results.log'
logger = logging.basicConfig(format=timeStamp,filename=logFilePath,level=logging.INFO)
path = "C:\\Users\\maitreypatel\\Desktop\\SEOTestCases\\LATTETestCases"
workBook = "latte-1166-testdata.xlsx"
sheetName = "Sheet1"

def verifyRels():
    #sarpUrls = openpyxl.load_workbook(workBook).get_sheet_by_name(sheetName).columns[0]
    readFile = open('sarpLinks.txt','r')
    lineByLine = readFile.readlines()

    for url in lineByLine:
        #link = url.value
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        relCans = soup.find("link", {"rel": "canonical"})
        relNext = soup.find("link", {"rel": "next"})
        relPrev = soup.find("link", {"rel": "prev"})
        #desc = soup.find("meta", {"name": "description"})['content']
        #titleTag = soup.title

        if relNext == None and relPrev == None:
            logging.error("Rel prev or next is not displayed " + str(url))
        print(relCans)
        print(relNext)
        print(relPrev)

verifyRels()

