import pygame 
from sys import exit

""" Surfaces:
Display surface: The main window visible to the player.
Regular surfaces: Images/text/colors drawn and then blitted onto the display surface.
"""

pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  

pygame.display.set_caption("Runner")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    #Draw all elements
    #update everything
    pygame.display.update()
    clock.tick(60)  
