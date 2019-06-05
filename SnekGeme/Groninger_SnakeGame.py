
#Welcome to Snek Geme
#This program is based on NewBoston's Pygame Snake Game Tutorials
#You need to have pygame installed!
#Have fun my little Slytherin!

import pygame
import time
import random

pygame.init()

white= (255,255,255)
black= (0,0,0)
red= (255,0,0)
yellow=(255,255,0)
green= (0,155,0)
blue= (0,0,255)
g=(0,255,0)


display_width = 800
display_height = 600


gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snek')

icon = pygame.image.load('sneeeek.png')
pygame.display.set_icon(icon)

img= pygame.image.load('sneeeek.png')
appleimg = pygame.image.load('apple.png')



clock = pygame.time.Clock()
FPS=10

direction = "right"
AppleThickness = 20
block_size= 20
block_m = 20

#1. I used a different font
smallfont = pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 25)
medfont = pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 50)
bigfont = pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 80)
#2. I added a larger font size 
hugefont = pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 100)

def game_intro():
  
  intro = True
  
  while intro:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        
      if event.type == pygame.KEYDOWN:
        if event.key== pygame.K_c:
           intro = False
        if event.key == pygame.K_q:
          pygame.quit()
          quit()
    
    #3. I created an interesting Intro Page by using all font sizes
    gameDisplay.fill(white)
    message_to_screen("Snek Geme", green, -100, "Huge")
    message_to_screen("Snek want Apple", black, -30, "medium")
    message_to_screen("Giv Snek Apple", black, +20, "medium")
    message_to_screen("Press C to Plaaaaaay", red, +80,"large")
    message_to_screen("Eat Apple= bigger Snek", black, +140, "small")
    message_to_screen("But Snek dont like touching itself, it's bad", black, +160, "small")
    message_to_screen("Snek just want to be big boi... ", black, +180, "small")
    
    pygame.display.update()
    clock.tick(15)

def randAppleGen():
  randAppleX = round(random.randrange(0,display_width-AppleThickness))
  randAppleY = round(random.randrange(0,display_height-AppleThickness))
  return randAppleX,randAppleY

def score(score):
  text = smallfont.render('Score: ' + str(score), True, black)
  gameDisplay.blit(text, [0,0])
  
pressK = pygame.key.get_pressed()




def snake(block_m,snakeList):
  
    if direction == "right":
      head = pygame.transform.rotate(img, 270)
    if direction == "left":
      head = pygame.transform.rotate(img, 90)
    if direction == "up":
      head = img
    if direction == "down":
      head = pygame.transform.rotate(img, 180)
    
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
      
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green,[XnY[0],XnY[1],block_m, block_m])

def text_objects(text,color,size):
    if size == "small":
      textSurface =smallfont.render(text,True,color)
    if size == "medium":
      textSurface =medfont.render(text,True,color)
    if size == "large":
      textSurface =bigfont.render(text,True,color)
    if size == "Huge":
      textSurface =hugefont.render(text,True,color)
    return textSurface, textSurface.get_rect()

                         
def message_to_screen(msg,color, y_displace= 0, size = "small"):
    textSurface, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/ 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurface, textRect)

    
def gameLoop():
    global direction
    gameExit= False
    gameOver= False

    lead_x=display_width/2
    lead_y=display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    randAppleX,randAppleY = randAppleGen()
    
    while not gameExit:

        while gameOver== True:
          
            gameDisplay.fill(black)
            message_to_screen("SNEK DED", green, -60, size= "Huge")
            message_to_screen("Game Over", red, -15, size= "medium")
            message_to_screen("Press C to Play or Q to Quit", white, +50, size= "medium")
            
            pygame.display.update()

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()
        gameDisplay.fill(white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
            if event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT: 
                  direction = "left"
                  gameDisplay.fill(yellow)
                  lead_x_change=-block_size
                  lead_y_change= 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    gameDisplay.fill(red)
                    lead_x_change= block_size
                    lead_y_change= 0
                elif event.key ==pygame.K_UP:
                    direction = "up"
                    gameDisplay.fill(g)
                    lead_y_change=-block_size
                    lead_x_change= 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    gameDisplay.fill(blue)
                    lead_y_change= block_size
                    lead_x_change= 0
                    
#4. With every key pressed, depending on which key, a color will flash. I did this in order to distract >;D.
                    
        if lead_x >= display_width or lead_x< 0 or lead_y >= display_height  or lead_y < 0:
              gameOver = True
    
        lead_x += lead_x_change
        lead_y += lead_y_change

                                 
        if lead_x == randAppleX and lead_y ==randAppleY:
            randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0
        
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(block_m,snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
            
        score((snakeLength-1)/2)
            
        pygame.display.update()
        
        
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX,randAppleY = randAppleGen()
            #5. I decided to have the apple worth 2 snakelengths for double the fun. Note this affects score and snakelength. 
            snakeLength += 2

        elif lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 2

        elif lead_x > randAppleX and lead_x < randAppleX + AppleThickness or  lead_x + block_m > randAppleX and lead_x + block_m < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_m > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 2
     
        clock.tick(FPS)

    pygame.quit()
    quit()


game_intro()
gameLoop()
