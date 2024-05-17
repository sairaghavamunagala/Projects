import pygame

# Intialize the pygame
pygame.init()

HEIGHT=800
WIDTH=600

# create the screen
screen=pygame.display.set_mode((HEIGHT,WIDTH))
running=True
while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    