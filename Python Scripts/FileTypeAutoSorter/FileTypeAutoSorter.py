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

# Create folders if they don't exist
for folder_name in folder_names:
    if not os.path.exists(os.path.join(path, folder_name)):
        os.makedirs(os.path.join(path, folder_name))

# Get the list of files in the directory
file_names = os.listdir(path)

# Move files to appropriate folders based on extension
for file in file_names:
    if file.endswith(".csv"):
        shutil.move(os.path.join(path, file), os.path.join(path, "CSV Files", file))
    elif file.endswith(".txt"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Text Files", file))
    elif file.endswith(".exe"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Applications", file))
    elif file.endswith(".zip"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Zip Files", file))
    elif file.endswith(".pdf"):
        shutil.move(os.path.join(path, file), os.path.join(path, "PDF Files", file))
    elif file.endswith(".msi"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Installers", file))
    elif file.endswith(".xls") or file.endswith(".xlsx"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Excel Files", file))
    elif file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Photos", file))
