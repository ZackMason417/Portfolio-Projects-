# File Type Auto Sorter

Python script that automatically sorts files in a directory based on their file types. A convenient tool for organizing and managing files efficiently.

This Python project automatically sorts files by file type into designated folders. It provides a simple solution for organizing a directory with various file types.

## Project Overview

The script takes a directory path and a list of folder names for each file type. It then iterates through each file in the directory and moves them to the appropriate folder based on their file extension.

Folder Structure
The script creates the following folders (if they don't exist) and sorts the files accordingly:

CSV Files
Text Files
Excel Files
PDF Files
Zip Files
Applications
Installers
Photos
Dependencies
Python 3.x
shutil
os
Example
Suppose you have files like data.csv, report.pdf, image.jpg, app.exe, etc., in the specified directory. After running the script, the files will be sorted into their respective folders:

AutoSort/

├── CSV Files/

│   └── data.csv

├── Text Files/

├── Excel Files/

├── PDF Files/

│   └── report.pdf

├── Zip Files/

├── Applications/

│   └── app.exe

├── Installers/

├── Photos/

│   └── image.jpg

Credits
Author: Zack Mason
