__author__ = 'maitreypatel'
import requests
import os
import openpyxl
import os.path

path = "C:\\Users\\maitreypatel\\Desktop\\SEOKeywordProcessor"
print(os.getcwd())
os.chdir(path)
print(os.getcwd())
#print(os.listdir(path))

wb = openpyxl.load_workbook("Sample_KeyPhrase.xlsx")
valuesInSheet = wb.get_sheet_by_name('Sheet1')
cellValues = valuesInSheet.columns[0]
numOfUrlCodes = 0

for cellObjects in cellValues:
    urlCode = requests.get(cellObjects.value).status_code
    #print(cellObjects.value)
    #print(urlCode)
    if urlCode != 200:
        badUrls = "Number of 404 urls : "
        print (urlCode)
        print (cellObjects.value)
        numOfUrlCodes+=1
if numOfUrlCodes == 0:
    print("All urls are valid")

else:
    print("There are invalid images exist")



