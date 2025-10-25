#Using rectangle to centre the score text 
#Drawing with pygame.draw
#Also renamed text_surface to score_surface
#In pygame there is a sub module called draw and can pass different attributes like circle , lines , rectangle , pointes , ellipse etc
#Also checkout pygame doumentation on pygame.draw  

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  
score_font = pygame.font.Font("font/Pixeltype.ttf",50)

pygame.display.set_caption("Runner")

sky_surface = pygame.image.load("Graphics/sky.png").convert() 
ground_surface = pygame.image.load("Graphics/ground.png").convert()

score_surf = score_font.render("My Game",False,"Black").convert()
score_rect = score_surf.get_rect(center = (400,50))


snail_surf = pygame.image.load("Graphics/snail/snail1.png",).convert_alpha()
snail_x_pos = 600 
snail_rect = snail_surf.get_rect(bottomright = (600,300) )

player_surf = pygame.image.load("Graphics/Player/player_walk_1.png").convert_alpha()

player_rect = player_surf.get_rect(midbottom = (80,300)) 
width = 825 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 

        

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    #pygame.draw tells pygame to draw and after that we defined what shape we want to draw 
    pygame.draw.rect(screen,"Pink",score_rect) 
    #Draws a filled rectangle (solid pink).
    pygame.draw.rect(screen,"Pink",score_rect,10)  
    #Draws only the border (outline) of the same rectangle, with a line thickness of 10 pixels. 
    
    screen.blit(score_surf,score_rect)

    snail_rect.x -= 4
    if snail_rect.right<=0:
        snail_rect.left=800
    screen.blit(snail_surf,(snail_rect))
    screen.blit(player_surf,player_rect) 
    
    width -= 5
    pygame.draw.line(screen,"Gold",(0,0),(800,400),width)

    pygame.display.update()
    clock.tick(60)  


"""Go through the documentation and draw a straight line from the top left to the bottom right of the screen"""

