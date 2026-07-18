import sys
import pygame
import random

#INTIALIZER
pygame.init() #Starts off pygame

#Loads enemy image
enemy = pygame.image.load()
enemy2 = pygame.image.load()
enemy3 = pygame.image.load()

#Setup Screen
width = 600
height = 400
size = (600, 400)
screen = pygame.display.set_mode(size)

#GAME LOOP
gameOver = False
while not gameOver:
    #Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    #CLICKS

    if pygame.mouse.get_pressed()[0]: #Left Click
        coords = pygame.mouse.get_pos() #Receives positio at click


    #UPDATE




    #DRAW




    pygame.display.flip()






pygame.display.quit()