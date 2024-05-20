import pygame
import random
# Intialize the pygame
pygame.init()

HEIGHT=600
WIDTH=800

# create the screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("space-invaders-icon.png")
pygame.display.set_icon(icon)


#player
playerImg=pygame.image.load("space-invaders.png")
playerX=370
playerY=480
playerX_change=0

enemyImg=pygame.image.load("enemy.png")
enemyX=random.randint(0,800)
enemyY=random.randint(80,150)
enemyX_change=0

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))
#Game Loop
running=True
while running:
    screen.fill((0,0,0)) #RGB
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    # if key stroke is pressed check whether its right or left
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key ==pygame.K_RIGHT:
                playerX_change=0.3
        if event.type==pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    if playerX>=768:
        playerX=768
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
    