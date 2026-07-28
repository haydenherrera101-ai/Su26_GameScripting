# Name: Hayden Herrera
# Date: 07/22/2026
# Description: This is the final project to utilize our knowledge and skill
# to develop a pygame program. My project will take a simularity towards the classic
# game "Galaga".

import pygame, random, sys

#-----------INITIALIZER-------------
pygame.init() #Starts off Pygame


#Scene setup
# 0 = title
# 1 = game
# 2 = game over/replay

scene = 0

#Setup Screen
screen_width = 850
screen_height = 600
surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Astro Blast")


#---------------GAMEPLAY FUNCTIONS------------------
titleFont = pygame.font.SysFont("timesnewroman", 72)
font = pygame.font.SysFont("timesnewroman", 28)
score = 0
highScore = 0
lives = 3

clock = pygame.time.Clock()

green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

#Assigns images to thier respectable functions
playerImage = pygame.image.load("Player.png")
pygame.display.set_icon(playerImage)
missileImage = pygame.image.load("goodMissile.png")

enemyImages = [
        pygame.image.load("enemy1.png"),
        pygame.image.load("enemy2.png"),
        pygame.image.load("enemy3.png"),
        pygame.image.load("enemy4.png"),
        pygame.image.load("enemy5.png")
    ]



eMissileImage = pygame.image.load("evilMissile.png")

background = pygame.image.load("spacebackground.png")
background = pygame.transform.scale(background,(screen_width,screen_height))


#---------------MOVEMENT FUNCTIONS------------------
class Player:
    #Initializes the players image, position, and overall direction
    def __init__(self, image, x, y, width, height):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.direction = ''
        self.speed = 7


    
    #Initializes move functions
    def move(self):
        if self.direction == 'E':
            self.rect.x = self.rect.x+self.speed
        if self.direction == 'W':
             self.rect.x = self.rect.x-self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y+self.speed


    def collided(self, other_rect):
        #This returns true if self collided with other_rect
        return self.rect.colliderect(other_rect)

            
    def draw(self, surface):
        #Helps draw image on screen
        surface.blit(self.image, self.rect)


#Builds player
sq = Player(playerImage,375,500,70,70)

#Builds Entities for Player
missiles = []
enemies = []
enemyMissiles = []

#-----------MAIN LOOP-------------
#Repeats in loop unitl player quits
done = False
while not done:

#EVENTS/USER INPUT

    #Recieves user input through keys A and D
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
           
        elif event.type == pygame.KEYDOWN:
            print(event.key) # Helps print value of key press

#TITLE SCREEN

            if scene == 0:
                if event.key == pygame.K_SPACE:
                    scene = 1

#GAME CONTROLS

            elif scene == 1:

                #Functions to move left and right
                if event.key == pygame.K_a: #A
                    sq.direction = 'W'
                if event.key == pygame.K_d: #S
                    sq.direction = 'E'
                if event.key == pygame.K_SPACE: #Spacebar for Player Missiles
                    
                    spawnx = sq.rect.centerx - 5
                    m = Player(missileImage, spawnx, sq.rect.top, 10,25)
                    m.direction = 'N'
                    m.speed = 12
                    missiles.append(m)
#RESTART GAME
            #If user chooses R, everything will be cleared and scores reset
            elif scene == 2:
                if event.key == pygame.K_r:
                    score = 0
                    lives = 3

                    missiles.clear()
                    enemies.clear()
                    enemyMissiles.clear()

                    sq.rect.x = 375
                    sq.rect.y = 500
                    sq.direction = ""

                    scene = 1
                #If player chooses Q, game will end and exit out
                if event.key == pygame.K_q:
                    done = True

        #Stops player movement once key is released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                sq.direction = ""
            if event.key == pygame.K_d:
                sq.direction = ""

#------------TITLE SCREEN-------------
    #If the scene is at title, draws the main menu to show title and input to start
    if scene == 0:
        surface.blit(background, (0,0))
        title = titleFont.render("ASTRO BLAST", True, white)
        press = font.render("Press SPACE to Start", True, white)

        surface.blit(title, (250,170))
        surface.blit(press, (250,300))


    #----------UPDATE------------
    #If scene is at Gameplay, the game will activate
    elif scene == 1:

        #Player Movement 
        sq.move()

        #Player Missiles Movement and Removal
        for m in missiles:
            m.move()
        for m in missiles[:]:
            if m.rect.bottom < 0:
                missiles.remove(m)

        #Enemy Movement and Removal
        for e in enemies:
            e.move()
        for e in enemies[:]:
            if e.rect.top > screen_height:
                enemies.remove(e)
                

        for e in enemies:
            if random.randint(1,150) == 1:
                missile = Player(eMissileImage,e.rect.centerx-5,e.rect.bottom,10,25)
                missile.direction = "S"
                missile.speed = 5
                enemyMissiles.append(missile)

        for m in enemyMissiles:
            m.move()

        for m in enemyMissiles[:]:
            if m.rect.top > screen_height:
                enemyMissiles.remove(m)

        
        #Limits movement to keep player inside the screen
        if sq.rect.left < 0:
            sq.rect.left = 0

        if sq.rect.right > screen_width:
            sq.rect.right = screen_width

        if sq.rect.top < 0:
            sq.rect.top = 0

        if sq.rect.bottom > screen_height:
            sq.rect.bottom = screen_height




        #Spawns Enemies at the top
        enemySpawn = 40

        if score > 1000:
            enemySpawn = 30

        if score > 3000:
                enemySpawn = 20

        if score > 6000:
                enemySpawn = 15

        if random.randint(1, enemySpawn) == 1: # Slows down enemies
            x = random.randint(0, screen_width-40)

            enemyImage = random.choice(enemyImages)
            e = Player(enemyImage, x, -50, 50,50)
            e.direction = 'S'
            e.speed = 2
            enemies.append(e)


        #Checks Collisions

        for i in reversed(range(len(missiles))):
            for j in reversed(range(len(enemies))):
                if missiles[i].collided(enemies[j].rect):
                    score += 100
                    del enemies[j]
                    del missiles[i]
                    break

        for m in enemyMissiles[:]:
            if sq.collided(m.rect):
                enemyMissiles.remove(m)
                lives -= 1

        for e in enemies[:]:
            if sq.collided(e.rect):
                enemies.remove(e)
                lives -= 1

        if lives <= 0:
            if score > highScore:
                highScore = score
            scene = 2


    #-----------DRAW-------------

        #Backup background draw
        surface.blit(background, (0, 0))

        #DRAWS ALL ENTITIES
        for m in missiles:
            m.draw(surface)

        for m in enemyMissiles:
            m.draw(surface)

        for e in enemies:
            e.draw(surface)

        sq.draw(surface)

    #SCORE DISPLAY

        scoreText = font.render("Score: " + str(score), True, white)
        surface.blit(scoreText, (15,15))

        livesText = font.render("Lives: " + str(lives), True, white)
        surface.blit(livesText, (700,15))

#GAME OVER SCREEN
    #If player dies, game over scene will show all results and the options to leave or restart
    elif scene == 2:

        surface.blit(background, (0,0))

        gameOver = titleFont.render("GAME OVER", True, red)
        finalScore = font.render("TOTAL SCORE: " + str(score), True, white)
        highScoreText = font.render("HIGH SCORE: " + str(highScore), True, yellow)
        restart = font.render("Press R to Play Again", True, white)
        quit = font.render("Press Q to Exit Game", True, white)

        surface.blit(gameOver, (220,170))
        surface.blit(finalScore, (290,260))
        surface.blit(highScoreText, (285,300))
        surface.blit(restart, (240,350))
        surface.blit(quit, (275, 390))


#SCREEN UPDATE
    #At the end of drawing, will flip display
    pygame.display.flip()
    clock.tick(60) #60FPS

#Makes sure that the game can quit if requested
pygame.display.quit()