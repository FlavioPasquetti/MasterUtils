from pygame import mixer

#---------------------------------------------------------------------------------------------

def playMusic (pathMusic):
    
    mixer.init()
    mixer.music.load(pathMusic)
    mixer.music.play()