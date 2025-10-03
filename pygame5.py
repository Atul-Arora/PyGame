import pygame 
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  

pygame.display.set_caption("Runner")

sky_surface = pygame.image.load("Graphics/sky.png")
ground_surface = pygame.image.load("Graphics/ground.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    #The one we write first is made first in python (overlapping occurs based on order of writing code)

    pygame.display.update()
    clock.tick(60)  
