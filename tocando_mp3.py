# Tocando MP3

import pygame
pygame.init()
pygame.mixer.music.load('musica_tocando.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
