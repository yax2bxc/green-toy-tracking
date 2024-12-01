import os
import tkinter as tk
from tkinter import filedialog
import shutil

root = tk.Tk()
root.withdraw()

dir = filedialog.askdirectory(initialdir='./')
abspath = os.path.abspath(dir)
files = [filename for filename in os.listdir(dir)]
# images = [filename for filename in os.listdir(dir) if filename.endswith('jpg')]
for file in files:
    old = os.path.join(abspath,file)
    new = os.path.join(abspath,file[9:])
    try:
        os.rename(old,new)
    except:
        os.remove(old)
        print(file)
