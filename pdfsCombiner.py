#!python3
# pdfsCombiner - Combines pdf pages from differents pdf documents.

import PyPDF2, os, sys, time

pdfWriter = PyPDF2.PdfFileWriter()# a blank pdf file that will hold pdf pages that will be added.

# function that check if the page number is a digit (in string format) and is a valid number for the document's pages.
def pageChecker(pageNumber, strDisplayed, totalOfPages ):
    while not (pageNumber.isdigit() and (int(pageNumber) <= totalOfPages and int(pageNumber) > 0)):
        if not pageNumber.isdigit():
            pageNumber = input('Enter the %s number: ' %(strDisplayed))
            continue
        if not (int(pageNumber) <= totalOfPages and int(pageNumber) > 0):
            pageNumber = input('The %s number should be between 1 and %s, the total number of pages: ' %(strDisplayed, str(totalOfPages)))
            continue
    return pageNumber

# chose pages from pdf document(s) and add them together to create a new pdf document. 
while True:
    fileName = input("Enter the pdf document's name, E.g: myFile.pdf: ")
    
    # check for the file existence in the folder.
    exist = True
    for folder, subfolders, files in os.walk('.'):
        if fileName not in files: # if the pdf file is not in the list of files contained in the current working directory.
            exist = False    
        break # Exit the loop after only one iteration, the current working directory.
    if not exist:     
        print("Sorry, '%s' doesn't exist in the current working directory. Double check the file name and try again!" %(fileName))
        continue # go to the next iteration of the while True loop.

    # open, unlock and read the file.
    pdfFile = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)# the content of pdfFile is stored in pdfReader.
    if pdfReader.isEncrypted: 
        password = input('This pdf file has a password. Please, enter the password: ')
        while not pdfReader.decrypt(password): # returns 1 (True) or 0 (False)
            password = input('The password you provided is wrong. Please, enter the password: ')
    pages = pdfReader.numPages # get the number of page of the document.
    
    # display the 3 possibilities to the screen.
    print('Which pages do you want from this document?')
    print('For the whole document, enter: 1')
    print('For a contiguous excerpt or a single page, enter: 2')
    print('For a discontinued excerpt, enter: 3')
    
    # choose among the 3 adding possibilities.
    choice = ''
    while choice not in ['1', '2', '3']:
        choice = input('Enter 1, 2 or 3: ')
    
    if choice == '1':
        # to add a whole document.
        for n in range(pages): # the number of page starts by 0.
            pageObj = pdfReader.getPage(n)
            pdfWriter.addPage(pageObj)
        print('The pdf document %s has been added to your new pdf document.' %(fileName))
    elif choice == '2':
        # to add a contiguous excerpt or a single page.
        firstPage = ''
        firstPage = pageChecker(firstPage, 'first page', pages)   
        lastPage = ''
        lastPage = pageChecker(lastPage, 'last page', pages)
        while not int(lastPage) >= int(firstPage):
            lastPage = input('Enter the last page number or the same number in case of a single page (last Page should be greater or equal to first page): ')
        for n in range(int(firstPage) -1, int(lastPage)):# if page 4 to 7, range(3, 7)
            pageObj = pdfReader.getPage(n)
            pdfWriter.addPage(pageObj)
        if int(firstPage) == int(lastPage):
            print('The page %s from the pdf document %s has been added to your new pdf document.' %(firstPage, fileName))
        else:
            print('The pages %s to %s from the pdf document %s has been added to your new pdf document.' %(firstPage, lastPage, fileName))
    else:
        # to add a discontinued excerpt.
        numberOfPage = ''
        numberOfPage = pageChecker(numberOfPage, 'page(s) to add', pages)
        pagesList = []
        for i in range(int(numberOfPage)):
            pageNumber = ''
            pageNumber = pageChecker(pageNumber, 'page %s' %(i + 1), pages) # pageNumber is a string
            pagesList.append(pageNumber)      
        for n in pagesList: # pagesList is a list of string digits that represent pages number to print. 
            pageObj = pdfReader.getPage(int(n) - 1)# the number of page starts by 0.
            pdfWriter.addPage(pageObj)
        print('The pages %s from the pdf document %s has been added to your new pdf document.' %(','.join(pagesList), fileName))

    # adding other pages.       
    answer = ''
    while answer.upper() not in ['Y', 'N']:
        answer = input('Do you want to add other pages? Y or N: ')
    if answer.upper() == 'N':       
        break

# naming, adding password, and creating the new document.    
newFile = input("Enter the name you want for your new pdf document. E.g: mydocument.pdf: ")
pdfOutputFile = open(newFile, 'wb')
encription = ''
while encription.upper() not in ['Y', 'N']:
    encription = input('Do you want to add a password to %s? Y or N: ' %(newFile))
if encription.upper() == 'Y':
    password = input('Enter the password: ')
    pdfWriter.encrypt(password)
    print('A password has been added to %s.' %(newFile))
pdfWriter.write(pdfOutputFile) # Write all pages that have been added to the new file.
pdfOutputFile.close()
print('The new pdf file %s has been created.' %(newFile))
print('The program will close in 5 seconds.')
time.sleep(5) # make 5 seconds pause before the program closes.










































































































































































































































































































pdfFile.close()
        
        
        
        
    
    
    
          
    
    


