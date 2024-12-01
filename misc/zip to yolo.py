import zipfile, tempfile
import os 

import tkinter as tk
from tkinter import filedialog
import shutil

root = tk.Tk()
root.withdraw()

# print(os.path.basename(zip.name).split('.')[0])
# print(zip.name)
def extractZip():
    zip = filedialog.askopenfile(initialdir='./')
    foldername = os.path.basename(zip.name).split('.')[0]
    foldername = f'./{foldername}'
    os.makedirs(foldername,exist_ok=True)
    with zipfile.ZipFile(zip.name,'r') as zip_ref:
        zip_ref.extractall(foldername)
    # os.makedirs('./extracted',exist_ok=True)
    # shutil.move(zip.name,'./extracted')
    return foldername

def createYaml():
    classes = []

    with open("classes.txt",'r') as file:
        classes = file.read().splitlines()

    with open("data.yaml",'w') as file:
        file.write("train: ./images\n")
        file.write("val: ./images\n")
        file.write("names:\n")
        for num, name in enumerate(classes):
            file.write(f"  {num}: {name}\n")

# createYaml()

def createTrainValSubset(dir):
    # Enter dir and make the Train Val subsets
    os.chdir(dir)
    files = os.listdir('.')
    # Remove the hash
    for file in files:
        try:
            os.rename(file,file[9:])
        except:
            os.remove(file)
    files = os.listdir('.')
    os.makedirs('./train')
    for files in files:
        shutil.move(files,'./train')
    # Copy this into val folder as well
    # os.makedirs('./val')
    shutil.copytree('./train','./val')
    os.chdir('..')


def main():
    foldername = extractZip()
    os.chdir(foldername)
    createTrainValSubset('./images')
    createTrainValSubset('./labels')
    createYaml()

main()
    # Get all images of current then create folder to push them into


# extractZip()



# shutil.copytree()

# os.listdir('.')
# os.chdir()
# print(zip.)
# dir = filedialog.askdirectory(initialdir='./')
# print(zipfile)


# tmpdir = tempfile.TemporaryDirectory()
# print(tmpdir.name)
# with zipfile.ZipFile(zipfilepath,'r') as zip_ref:
#     zip_ref.extractall(tmpdir)
# tmpdir.cleanup()

# Change the work directory of pythona nd reset back?
# main()
# os.chdir('smiskiseries1')
# print(os.getcwd())
#  Extract zip
# Remove hashes from all image and folder name
# Move into a folder
# Rename into train
# Copy into as val subsets in same dir
# Yaml
# enumerate txt file