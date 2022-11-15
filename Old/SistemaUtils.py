import os
import webbrowser
from pygame import mixer

#---------------------------------------------------------------------------------------------

def openSite (andressSite):

    webbrowser.open(andressSite) 

#---------------------------------------------------------------------------------------------

def openApp (andressApp):

    os.startfile(andressApp)

#---------------------------------------------------------------------------------------------

def playMusic (pathMusic):
    
    mixer.init()
    mixer.music.load(pathMusic)
    mixer.music.play()