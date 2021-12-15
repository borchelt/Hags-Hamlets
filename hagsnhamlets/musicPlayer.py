import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(.5)
def setvol(vol):
    pygame.mixer.music.set_volume(vol)
def playSound(song):
    pygame.mixer.Channel(1).stop()
    song1 = pygame.mixer.Sound(song)
    pygame.mixer.Channel(1).play(song1, -1)