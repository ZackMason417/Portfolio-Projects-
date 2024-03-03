import os
import shutil

# Path to the directory you want to sort
path = r"C:/Users/thety/Documents/AutoSort/"

# List of folder names for each file type
folder_names = [
    "CSV Files",
    "Text Files",
    "Excel Files",
    "PDF Files",
    "Zip Files",
    "Applications",
    "Installers",
    "Photos"
]

# Iterate through each folder name
for folder_name in folder_names:
    # Create the folder if it doesn't exist
    if not os.path.exists(path + folder_name):
        os.makedirs(path + folder_name)

# Get the list of files in the directory
file_names = os.listdir(path)

# Iterate through each file and move to appropriate folder
for file in file_names:
    if file.endswith(".csv"):
        shutil.move(path + file, path + "CSV Files/" + file)
    elif file.endswith(".txt"):
        shutil.move(path + file, path + "Text Files/" + file)
    elif file.endswith(".exe"):
        shutil.move(path + file, path + "Applications/" + file)
    elif file.endswith(".zip"):
        shutil.move(path + file, path + "Zip Files/" + file)
    elif file.endswith(".pdf"):
        shutil.move(path + file, path + "PDF Files/" + file)
    elif file.endswith(".msi"):
        shutil.move(path + file, path + "Installers/" + file)
    elif file.endswith(".xls") or file.endswith(".xlsx"):
        shutil.move(path + file, path + "Excel Files/" + file)
    elif file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(path + file, path + "Photos/" + file)
