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

test_surface = pygame.Surface((200,100)) #Surface S should be capital
test_surface.fill("Red")
test_surface2 = pygame.Surface((100,200)) 
test_surface2.fill("Yellow")
screen.fill("White")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    
    screen.blit(test_surface,(0,0))  #Blit is block image transfer . fancy way of saying one surface on other surface
    screen.blit(test_surface2,(200,100))


    pygame.display.update()
    clock.tick(60)  
