from tkinter import filedialog

def openFile (typeFile, exts):

    return filedialog.askopenfiles(filetypes=[(typeFile, exts)])   

#Teste
files= openFile("Imagens (.png, .jpg)", ("*.png", "*.jpg"))