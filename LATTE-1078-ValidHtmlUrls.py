__author__ = 'maitreypatel'
import os
import os.path
import openpyxl
import requests
path = "C:\\Users\\maitreypatel\\Desktop\\SEOKeywordProcessor"
currentPath = os.getcwd()
print(os.getcwd())

list = os.listdir()
print(list)
os.chdir("C:\\Users\\maitreypatel\\Desktop\\SEOKeywordProcessor")
print(os.getcwd())
list = os.listdir()
#print(list)

wb = openpyxl.load_workbook("LATTE-1078-imageUrlValidations.xlsx")
valuesInSheet = wb.get_sheet_by_name('Sheet1')
cellValues = valuesInSheet.columns[0]
numOfUrlCodes = 0
for cellObjects in cellValues:
    urlCode = requests.get(cellObjects.value).status_code
    if urlCode != 200:
        badUrls = "Number of 404 urls : "
        print (urlCode)
        print (cellObjects.value)
        numOfUrlCodes+=1
if numOfUrlCodes == 0:
    print("All image urls are valid")
else:
    print("There are invalid images exist")
