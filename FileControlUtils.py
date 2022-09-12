import os, sys
import shutil
from tkinter import filedialog
import ctypes

#Caminha em uma pasta listando diretorios e arquivos -> for root, dirs, files in os.walk(path):
#Verifica se a string comeca com uma substring -> String.startswith(String)
#Verifica se a string termina com uma subtring -> String.endswith(String)

#---------------------------------------------------------------------------------------------

def openFile (typeFile, exts):
    #typeFile exemplo: "Imagens"
    #exts exemplo: ("*.jpg","*.png") 

    return filedialog.askopenfiles(filetypes=[(typeFile, exts)])        

#---------------------------------------------------------------------------------------------

def localPath ():

    localPath = ""
    if getattr(sys, "frozen", False):
        localPath = os.path.dirname(sys.executable)
    elif __file__:
        localPath = os.path.dirname(__file__)

    return localPath

#---------------------------------------------------------------------------------------------

def extFile(pathFile, ext):

    return pathFile.lower().endswith(ext)

#---------------------------------------------------------------------------------------------

def dirList (pathDir, prefix = ""):

    listDir = ""
    folders = []

    for path in os.listdir(pathDir):

        if os.path.isfile(os.path.join(pathDir, path)):
            listDir += prefix + "- " + path + "\n"

        else:
            listDir += prefix + " " + path + "\n"

    return listDir, folders 

#---------------------------------------------------------------------------------------------

def dirWalk (pathDir, limit = False, loopC = 100, prefix = ""):

    listDir = ""
    folders = []

    print (prefix + "╭ " + pathDir)
    prefix += "|"

    for name in os.listdir(pathDir):

        path = os.path.join(pathDir, name)

        if os.path.isfile(path):
            print (prefix + " " + name)


    for name in os.listdir(pathDir):

        path = os.path.join(pathDir, name)
        loopC -= 1

        if not os.path.isfile(path):
            loopC = dirWalk (path, limit, loopC, prefix)

        if loopC <= 0 and limit:
            break
            
    return loopC

#---------------------------------------------------------------------------------------------

def listFilesandFolders (pathDir, recurs = False):

    files = []
    folders = []

    for name in os.listdir(pathDir):

        path = os.path.join(pathDir, name)

        if os.path.isfile(path):
            files.append(path)

        if os.path.isdir(path):
            folders.append(path)

            if (recurs):
                filesAp, foldersAp = listFilesandFolders(path, recurs)
                for file in filesAp: files.append(file)
                for folder in foldersAp: folders.append(folder)

    return files, folders

#---------------------------------------------------------------------------------------------

def cleanPath(path):
   
    path = str(path).strip()
    for char in '<>"|?*':
        assert (char not in path), \
               'character {0} is not allowed on a folder name'.format(char)    

    path = f'{path!r}'[1:-1].replace('\\\\', '\\').replace('/', '\\')

    return path

#---------------------------------------------------------------------------------------------

def addPath(path):

    path = cleanPath(path)
        
    path, extension = os.path.splitext(path)
    if (extension != ''):
        path = os.path.dirname(path) # remove file.
    if (path != ''):
        path, folder = os.path.split(path)
        if (folder != ''):
            path = os.path.join(path, folder)
        os.makedirs(path, exist_ok=True)

#---------------------------------------------------------------------------------------------

def existePath (pathFileorDir):
    #Verifica se o arquivo ou diretório existe

    return os.path.exists(pathFileorDir)

#---------------------------------------------------------------------------------------------

def isFile (pathFile):
    #Verifica se o caminho é um arquivo

    return os.path.isfile(pathFile)

#---------------------------------------------------------------------------------------------

def isDir (pathDir):
    #Verifica se o caminho é um diretório

    return os.path.isdir(pathDir)

#---------------------------------------------------------------------------------------------

def delete (pathFileorDir, confirm = True):

    valid = False
    if (not confirm):
        valid = True

    if (existePath(pathFileorDir)):
        
        if (isFile(pathFileorDir)):
            validReturn = messageBox("Delete File", "Delele File:\n" + str(pathFileorDir), 0x40, 1, 0x1000)
            if (validReturn == 1): valid = True
            if (valid): os.remove(pathFileorDir)
        
        else:
            validReturn = messageBox("Delete Folder", "Delele All Folder:\n" + str(pathFileorDir), 0x40, 1, 0x1000)
            if (validReturn == 1): valid = True
            if (valid): shutil.rmtree(pathFileorDir)

        return True

    return False

#---------------------------------------------------------------------------------------------

def createPath (pathCreate):

    if (not existePath(pathCreate)):
        os.makedirs(pathCreate)

#---------------------------------------------------------------------------------------------

def moveOrRename (iniPath, outPath):

    if (isFile(iniPath)):
        os.rename(iniPath, outPath)

    elif (isDir(iniPath)):

        iniPath = iniPath.replace("\\", "/")
        folderName = iniPath.split("/")[-1]

        createPath(outPath + "/" + folderName)

        files, folders = listFilesandFolders (iniPath, True)

        for folder in folders: 
            folder = folder.replace(iniPath, outPath + "/" + folderName)

            createPath(folder)

        for file in files: 

            outFile = file.replace(iniPath, outPath + "/" + folderName)
            moveOrRename(file, outFile)

        delete(iniPath, False)

#---------------------------------------------------------------------------------------------

def copyFileorFolder (iniPath, outPath):

    if (isFile(iniPath)):
        shutil.copy(iniPath, outPath)

    elif (isDir(iniPath)):

        iniPath = iniPath.replace("\\", "/")
        folderName = iniPath.split("/")[-1]

        createPath(outPath + "/" + folderName)

        files, folders = listFilesandFolders (iniPath, True)

        for folder in folders: 
            folder = folder.replace(iniPath, outPath + "/" + folderName)

            createPath(folder)

        for file in files: 

            outFile = file.replace(iniPath, outPath + "/" + folderName)
            shutil.copy(file, outFile)
        
#---------------------------------------------------------------------------------------------

def messageBox (title, message, icon = 0x10, buttons = 0, styleWindow = 0x2000):

    # ICON
    #MB_ICONEXCLAMATION = MB_ICONWARNING = 0x30
    #MB_ICONINFORMATION = MB_ICONASTERISK = 0x40
    #MB_ICONQUESTION = 0x20
    #MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10

    #BUTTONS
    #MB_ABORTRETRYIGNORE = 2
    #MB_CANCELTRYCONTINUE = 6
    #MB_HELP = 0x4000
    #MB_OK = 0
    #MB_OKCANCEL = 1
    #MB_RETRYCANCEL = 5
    #MB_YESNO = 4
    #MB_YESNOCANCEL = 3

    #STYLE WINDOW
    #MB_APPLMODAL = 0
    #MB_SYSTEMMODAL = 0x1000
    #MB_TASKMODAL = 0x2000

    return ctypes.windll.user32.MessageBoxW(None, message, title, icon | buttons | styleWindow)
