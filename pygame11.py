#Colours with the use of rgb and hex codes
#The player character 
#1.Keyboard input #2.jump + gravity #3.Creating a floor

#KEYBOARD IMPUT - pygame.key OR event loop

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  
score_font = pygame.font.Font("font/Pixeltype.ttf",50)

pygame.display.set_caption("Runner")

sky_surface = pygame.image.load("Graphics/sky.png").convert() 
ground_surface = pygame.image.load("Graphics/ground.png").convert()

score_surf = score_font.render("My Game",False,(64,64,64)).convert()
score_rect = score_surf.get_rect(center = (400,50))


snail_surf = pygame.image.load("Graphics/snail/snail1.png",).convert_alpha()
snail_x_pos = 600 
snail_rect = snail_surf.get_rect(bottomright = (600,300) )

player_surf = pygame.image.load("Graphics/Player/player_walk_1.png").convert_alpha()

player_rect = player_surf.get_rect(midbottom = (80,300)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("jump")

        #Keyboard imput in event loop - 1.check if any button was pressed 2.wprk with a specific key         

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,"#c0e8ec",score_rect) 
    pygame.draw.rect(screen,"#c0e8ec",score_rect,10)  
    #If width = 0 → fills the rectangle completely (solid)
    #If width > 0 → draws only the border with that thickness

    screen.blit(score_surf,score_rect)

    snail_rect.x -= 4
    if snail_rect.right<=0:
        snail_rect.left=800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect) 

    """keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("jump")"""
    

    pygame.display.update()
    clock.tick(60)  


