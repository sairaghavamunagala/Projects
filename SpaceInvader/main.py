import pygame

# Intialize the pygame
pygame.init()

HEIGHT=800
WIDTH=600

# create the screen
screen=pygame.display.set_mode((HEIGHT,WIDTH))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

running=True
while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        screen.fill((255,255,255)) #RGB
        pygame.display.update()
    