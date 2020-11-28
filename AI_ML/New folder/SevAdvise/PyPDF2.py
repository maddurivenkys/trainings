# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('C:\FNOverview.pdf', 'rb') 
print('File has loaded ')

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
numPages= pdfReader.numPages
print('Total pages in pdf ', numPages) 

# creating a page object 
for x in range(numPages):
    print(x)
    pageObj = pdfReader.getPage(x)
    # extracting text from page
    print(pageObj.extractText()) 
# closing the pdf file object 
pdfFileObj.close() 