import pygame

clock = pygame.time.Clock()
pygame.init()

def play(filename):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(3)
    except pygame.error:
        print ("File %s not found! (%s)" % (filename, pygame.get_error()))

#Usage:
#import APlayMusic
#words=[]
#words.append("/usr/share/sounds/alsa/Front_Left.wav")
#words.append("/usr/share/sounds/alsa/Front_Right.wav")

#for word in words:
#  APlayMusic.play(word)


        

