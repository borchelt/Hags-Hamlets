import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(.5)
def setvol(vol):
    pygame.mixer.music.set_volume(vol)
def playSound(song):
    pygame.mixer.Channel(0).stop()
    sound = pygame.mixer.Sound(song)
    pygame.mixer.Channel(0).play(sound)