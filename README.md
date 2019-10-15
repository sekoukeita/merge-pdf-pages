# Merge-pdf-pages
Use a python script to open pdf files even they have a password (that you will provide, of course), select the pages you want and add them together into a new pdf document you can also protect with a password.
I am a beginner and your suggestion and help to improve this program would be really aprreciated.

## How the program works
1. Launch the program. 
2. Enter the pdf document name and eventually the password.
3. Choose the way you want to select your pages. The program selects them an merge them into a new pdf document.
5. Name your new pdf file and eventually provide the password you for it.
6. The program creates the new pdf file into the working directory.

## Getting started
The script could be run in 2 different environments (windows environments):

### Python environment
To be run in python environment, your computer should have the folling programs and modules installed:
1. Download and install [python3](https://www.python.org/downloads/) which should install also **pip**, python packages manager.
2. Install the third party module **PyPDF2** using the following syntax in the command prompt:
```
    pip install PyPDF2
````
3. Place pdf files you want to use pages from into your python working directory.
4. Launch the script (*pdfsCombiner.py*)

### Non-Python environment
You can still run this program even if you don't have python installed on your computer. In this case, you will need to create the executable file in python environment and  then run the *pdfsCombiner.exe* in a non-python environment. You can follow these steps:
1. Install the package *pyinstaller* using the command prompt:
```
    pip install pyinstaller
```
2. Set the current directory to your working directory where the script is:
```
    C:\Users\yourComputerUserName>cd yourCurrentWorkingDirectoryPath
```
3. Run pyinstaller on the script:
```
    pyinstaller pdfsCombiner.py
```
4. *pyinstall* will create a folder called *dist* that contains the folder *pdfsCombiner*.
5. Zip the folder and redistribute it where you want to run the program.
6. Unzip the folder, open it,  add the pdf files you want to use and launch the *pdfsCombiner.exe* to run the program.

## Bonus
* I am providing the zip file I made for you to test.
* Download it, unzip the folder, add the pdf files you want to merge pages from and lunch the program.
* Your new file should be created into the folder.


## Author
    Sekou Keita
