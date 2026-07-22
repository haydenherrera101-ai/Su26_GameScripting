import sys
import pygame
import random

#INTIALIZER
pygame.init() #Starts off pygame

#Scene setup
# 0 = title
# 1 = game
# 2 = game over/replay

scene = 1


#Loads enemy image
enemy = pygame.image.load("barnicle.png")
enemy2 = pygame.image.load("rock.png")
enemy3 = pygame.image.load("slime.png")

enemies = [enemy, enemy2, enemy3]

#Setup Screen
width = 600
height = 400
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dungeon Splat")
pygame.display.set_icon(enemy3)

#Defines colors
green = (74, 99, 35)
orange = (243, 121, 78)
black = (0, 0, 0)

#-------TITLE STUFF--------
titleY = 100
playY = 300
buttonMargin = 10

titleFont = pygame.font.SysFont("Arial", 65)
enemyTitle = titleFont.render("Dungeon Splat!", False, green)
gameOverTitle = titleFont.render("GAME OVER", False, orange)

buttonFont = pygame.font.SysFont("Arial", 30)
playWord = buttonFont.render("PLAY", False, green)
quitWord = buttonFont.render("QUIT", False, green)
restartWord = buttonFont.render("RESTART", False, orange)

playButton = pygame.draw.rect(screen, black, ((width/2)-(playWord.get_width()/2) - buttonMargin, playY - buttonMargin, playWord.get_width() + (buttonMargin*2), playWord.get_height()+(buttonMargin*2)),0)

quitButton = pygame.draw.rect(screen, black, ((width/4)-quitWord.get_width()/2 - buttonMargin, playY - buttonMargin, quitWord.get_width() + (buttonMargin * 2), quitWord.get_height() +(buttonMargin *2)), 0)

restartButton = pygame.draw.rect(screen, green, ((width * .75)-(restartWord.get_width()/2) - buttonMargin, playY - buttonMargin, restartWord.get_width() + (buttonMargin * 2), restartWord.get_height() +(buttonMargin *2)), 0)
#--------------------------

#-------GAMEPLAY MODE LOAD-
#Enemy definitions
counter = 0
numOfThings = 7
enemyImage = []
enemyX = []
enemyY = []
enemySpeed = []
baseSpeed = .3
speedMulti = 1.2

#Releases the enemies 
while counter < numOfThings:
    enemyImage.append(random.choice(enemies)) #assign random image
    enemyX.append(random.randint(0, width - enemyImage[counter].get_width()))
    enemyY.append(0 - random.randint(enemyImage[counter].get_height(), enemyImage[counter].get_height() * 2))
    enemySpeed.append(baseSpeed * random.random())

    counter += 1


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
        if scene == 0: #If title screen
            #Button to play
            print("title screen")
        elif scene == 1: #play area
            #We can't use collidepoint() because don't have 
            #individual rects on each enemy image. Old version.
            counter = 0
            while counter < numOfThings:
                #Click greater = left side and less = right side and greater than top, less than bottom (within image)
                if coords[0] >= enemyX[counter] and coords[0] <= enemyX[counter] + enemyImage[counter].get_width() and coords[1] >= enemyY[counter] and coords[1] <= enemyY[counter] + enemyImage[counter].get_height():
                    #print("Clicked it")
                    enemyImage[counter] = random.choice(enemies)
                    enemyX[counter] = random.randint(0, width - enemyImage[counter].get_width())
                    enemyY[counter] = 0 - random.randint(enemyImage[counter].get_height(), enemyImage[counter].get_height() * 2)
                    enemySpeed[counter] *= speedMulti
                    
                counter += 1
        else: #gameover screen
            #print("game over screen")
            scene = 2
            if pygame.Rect.collidepoint(quitButton, coords):
                gameOver = True
            if pygame.Rect.collidepoint(restartButton, coords):
                #RESET YOUR GAME BEFORE RELOADING OR GOING BACK
                counter = 0
                while counter < numOfThings:
                    enemyImage[counter] = random.choice(enemies)
                    enemyX[counter] = random.randint(0, width - enemyImage[counter].get_width())
                    enemyY[counter] = 0 - random.randint(enemyImage[counter].get_height(), enemyImage[counter].get_height() * 2)
                    enemySpeed.append(baseSpeed * random.random())
                    counter += 1
                scene = 1





    #UPDATE
    #Movement and floor checks
    if scene == 1:
        counter = 0
        while counter < numOfThings:
            #check if hit bottom
            if enemyY[counter] + enemyImage[counter].get_height() > height:
                scene = 2
            else:
                enemyY[counter] += enemySpeed[counter]
            counter += 1


    #DRAW
    #title scene
    if scene == 0:
        screen.fill(orange)
    
    #game play
    elif scene == 1:
        screen.fill(green)
        #Draws the enemies
        counter = 0
        while counter < numOfThings:
            screen.blit(enemyImage[counter], (enemyX[counter], enemyY[counter]))
            counter += 1

    else:
        screen.fill(black)
        #gameOver text
        screen.blit(gameOverTitle, (width/2 - gameOverTitle.get_width()/2, titleY))
        #left slime
        screen.blit(enemy3, ((width/2)-(gameOverTitle.get_width()/2)-enemy3.get_width(), titleY + (gameOverTitle.get_height()-enemy3.get_height())))
        #right slime
        screen.blit(enemy3, (width/2 + gameOverTitle.get_width()/2, titleY + (gameOverTitle.get_height()-enemy3.get_height())))

        #-------BUTTONS---------
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