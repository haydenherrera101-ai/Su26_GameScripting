# Name: Hayden Herrera
# Date: 07/21/2026
# Description: This chicken drop will demonstrate functions from Python and
# converting them into a functional pygame. Chickens will be dropped and must be catched
# before hitting the ground. There are also eggs you can click to get a powerup to slow down.


import sys
import pygame
import random

pygame.init() #Starts off Chicken Drop

#Scene Setup
# 0 = title
# 1 = game
# 2 = game over/replay

scene = 1

chicken1 = pygame.image.load("chicken.png")
chicken2 = pygame.image.load("chicken2.png")
eggImage = pygame.image.load("eggs.png")

chickens = [chicken1, chicken2]

#Set Up
width = 600
height = 400
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chicken Drop")
pygame.display.set_icon(chicken1)

#Defines Colors
green = (74,99,35)
orange = (243, 121, 78)
black = (0,0,0)

clock = pygame.time.Clock()
clock.tick(60)

#---------------TITLE FUNCTIONS----------------
titleY = 100
playY = 300
buttonMargin = 10

titleFont = pygame.font.SysFont("timesnewroman", 65)
enemyTitle = titleFont.render("Chicken Drop", False, green)
gameOverTitle = titleFont.render("GAME OVER", False, orange)

buttonFont = pygame.font.SysFont("timesnewroman", 30)
playWord = buttonFont.render("PLAY", False, green)
quitWord = buttonFont.render("QUIT", False, green)
restartWord = buttonFont.render("RESTART", False, orange)

playButton = pygame.draw.rect(screen, black, ((width/2)-(playWord.get_width()/2) - buttonMargin, playY - buttonMargin, playWord.get_width() + (buttonMargin*2), playWord.get_height()+(buttonMargin*2)),0)

quitButton = pygame.draw.rect(screen, black, ((width/4)-quitWord.get_width()/2 - buttonMargin, playY - buttonMargin, quitWord.get_width() + (buttonMargin * 2), quitWord.get_height() +(buttonMargin *2)), 0)

restartButton = pygame.draw.rect(screen, green, ((width * .75)-(restartWord.get_width()/2) - buttonMargin, playY - buttonMargin, restartWord.get_width() + (buttonMargin * 2), restartWord.get_height() +(buttonMargin *2)), 0)

#-------------GAMEPLAY FUNCTIONS----------------
# Definitions
counter = 0
numOfChickens = 7
chickenImage = []
chickX = []
chickY = []
chickSpeed = []
baseSpeed = 0.1
speedMulti = 1.13

#-------------CHICKENS--------------
# Releases the chickens 
while counter < numOfChickens:
    chickenImage.append(random.choice(chickens)) #assign random image
    chickX.append(random.randint(0, width - chickenImage[counter].get_width()))
    chickY.append(0 - random.randint(chickenImage[counter].get_height(), chickenImage[counter].get_height() * 2))
    chickSpeed.append(baseSpeed * random.random())

    counter += 1

#------------POWERUP-------------
eggActive = False
eggX = 0
eggY = 0

eggTimer = random.randint(3000, 6000)
powerupTimer = 0

normalSpeed = baseSpeed
slowMultiplier = 0.2

#------------GAME LOOP-------------
gameOver = False
while not gameOver:
    #Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

#-------------CLICKS--------------

    if pygame.mouse.get_pressed()[0]: #Left Click
        coords = pygame.mouse.get_pos() #Receives positio at click
        if scene == 0: #If title screen
            #Button to play
            print("title screen")
        elif scene == 1: #play area
            #We can't use collidepoint() because don't have 
            #individual rects on each enemy image. Old version.
            counter = 0
            while counter < numOfChickens:
                #Click greater = left side and less = right side and greater than top, less than bottom (within image)
                if coords[0] >= chickX[counter] and coords[0] <= chickX[counter] + chickenImage[counter].get_width() and coords[1] >= chickY[counter] and coords[1] <= chickY[counter] + chickenImage[counter].get_height():
                    #print("Clicked it")
                    chickenImage[counter] = random.choice(chickens)
                    chickX[counter] = random.randint(0, width - chickenImage[counter].get_width())
                    chickY[counter] = 0 - random.randint(chickenImage[counter].get_height(), chickenImage[counter].get_height() * 2)
                    chickSpeed[counter] *= speedMulti

                counter += 1

            if eggActive:
                    if (coords[0] >= eggX and
                        coords[0] <= eggX + eggImage.get_width() and
                        coords[1] >= eggY and
                        coords[1] <= eggY + eggImage.get_height()):

                        eggActive = False
                        powerupTimer = 5400

        else: #gameover screen
            #print("game over screen")
            scene = 2
            if pygame.Rect.collidepoint(quitButton, coords):
                gameOver = True
            if pygame.Rect.collidepoint(restartButton, coords):
                #RESET YOUR GAME BEFORE RELOADING OR GOING BACK
                counter = 0
                while counter < numOfChickens:
                    chickenImage[counter] = random.choice(chickens)
                    chickX[counter] = random.randint(0, width - chickenImage[counter].get_width())
                    chickY[counter] = 0 - random.randint(chickenImage[counter].get_height(), chickenImage[counter].get_height() * 2)
                    chickSpeed[counter] = baseSpeed * random.random()
                    counter += 1
                scene = 1


#-----------UPDATE------------
    #Egg Spawn and Movement
    if not eggActive:
        eggTimer -= 1

        if eggTimer <= 0:
            eggX = random.randint(0, width - eggImage.get_width())
            eggY = random.randint(50, height - eggImage.get_height() - 50)
            eggActive = True
            eggTimer = random.randint(3000, 6000)

    #Movement and floor checks
    if scene == 1:

        counter = 0

        while counter < numOfChickens:
            if chickY[counter] + chickenImage[counter].get_height() > height:
                scene = 2
            else:
                if powerupTimer > 0:
                    chickY[counter] += chickSpeed[counter] * slowMultiplier
                else:
                    chickY[counter] += chickSpeed[counter]

            counter += 1


    # Slow motion timer
    if powerupTimer > 0:
        powerupTimer -= 1


#------------DRAW-------------
    #title scene
    if scene == 0:
        screen.fill(orange)
    
    #game play
    elif scene == 1:
        screen.fill(green)
        #Draws the enemies
        counter = 0
        while counter < numOfChickens:
            screen.blit(chickenImage[counter], (chickX[counter], chickY[counter]))
            counter += 1

        #Draws eggs
        if eggActive:
            screen.blit(eggImage, (eggX, eggY))

    else:
        screen.fill(black)
        #gameOver text
        screen.blit(gameOverTitle, (width/2 - gameOverTitle.get_width()/2, titleY))
        #left slime
        screen.blit(chicken2, ((width/2)-(gameOverTitle.get_width()/2)-chicken2.get_width(), titleY + (gameOverTitle.get_height()-chicken2.get_height())))
        #right slime
        screen.blit(chicken2, (width/2 + gameOverTitle.get_width()/2, titleY + (gameOverTitle.get_height()-chicken2.get_height())))

#--------------BUTTONS-------------
        #QUIT
        coords = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(quitButton, coords): #check if mouse is hovering over button and flip colors
            quitButton = pygame.draw.rect(screen, green, ((width/4)-quitWord.get_width()/2 - buttonMargin, playY - buttonMargin, quitWord.get_width() + (buttonMargin * 2), quitWord.get_height() +(buttonMargin *2)), 0)
        else:
            quitButton = pygame.draw.rect(screen, orange, ((width/4)-quitWord.get_width()/2 - buttonMargin, playY - buttonMargin, quitWord.get_width() + (buttonMargin * 2), quitWord.get_height() +(buttonMargin *2)), 0)

        screen.blit(quitWord, ((width/4)-(quitWord.get_width()/2), playY))
        #RESTART
        if pygame.Rect.collidepoint(restartButton, coords): #if hovered over
            restartButton = pygame.draw.rect(screen, orange, ((width * .75)-(restartWord.get_width()/2) - buttonMargin, playY - buttonMargin, restartWord.get_width() + (buttonMargin * 2), restartWord.get_height() +(buttonMargin *2)), 0)
        else:
            restartButton = pygame.draw.rect(screen, green, ((width * .75)-(restartWord.get_width()/2) - buttonMargin, playY - buttonMargin, restartWord.get_width() + (buttonMargin * 2), restartWord.get_height() +(buttonMargin *2)), 0)
            screen.blit(restartWord, ((width * .75) - (restartWord.get_width()/2), playY))
  



    #At the end of drawing, will flip display
    pygame.display.flip()


#Makes sure that the game can quit
pygame.display.quit()