# Listing the files in the given folder 

import os
folders=input("Enter the list of folders name: ").split()

for folder in folders:
    try:
        files= os.listdir(folder)
    except FileNotFoundError:
        print("Folder Not Found in the given input")
        continue
    print("Files in the folder " + folder + " are: ")
    for file in files:
        print(file)

        