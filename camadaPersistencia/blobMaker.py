from tkinter import filedialog
from tkinter import *
import tkinter as tk


class BlobSolver:
    def convertToBinaryData(filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    
    def insertBLOB():
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =(("image", ".jpeg"), ("image", ".png"),("image", ".jpg"),("all files","*.*")))
        return file_path