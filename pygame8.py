#Basic Collisions with rectangle
#Can be done using collide rect method rect1.colliderect(rect2)
#theres a different kind of collision you can use for rectangles rect.collidepoint((x,y))
#rect.collidepoint((x,y)) just checks if rectangle collides with a point 
#rect.collidepoint((x,y)) + mouse  - if you ever want to click with a mouse on something 
#getting the mouse position two methods - pygame.mouse / event loop 
#pygame.mouse - mouse position, clicks bluttons,visibility etc. 
#event loop - get mousemotion, clicks,position etc.

import pygame 
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  
score_font=pygame.font.Font("font/Pixeltype.ttf",50)

pygame.display.set_caption("Runner")

sky_surface = pygame.image.load("Graphics/sky.png").convert() 
ground_surface = pygame.image.load("Graphics/ground.png").convert()
score_surf= score_font.render("My Game",False,"Black").convert()



snail_surf=pygame.image.load("Graphics/snail/snail1.png",).convert_alpha()
snail_x_pos = 600 
snail_rect = snail_surf.get_rect(bottomright = (600,300) )

player_surf=pygame.image.load("Graphics/Player/player_walk_1.png").convert_alpha()

player_rect = player_surf.get_rect(midbottom = (80,300)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    
        #checking via event loop 
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN: #Triggers when clicking mouse button 
            print('mouse down')
        if event.type == pygame.MOUSEBUTTONUP: #Triggers when releasing mouse button 
            print('mouse up')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(score_surf,score_rect)

    snail_rect.x -= 4
    if snail_rect.right<=0:
        snail_rect.left=800
    screen.blit(snail_surf,(snail_rect))
    screen.blit(player_surf,player_rect) 

    #if (player_rect.colliderect(snail_rect)):
        #print("collision1")

    mouse_pos = pygame.mouse.get_pos()

    if player_rect.collidepoint((mouse_pos)):
        #print("mouse on player ")
        print(pygame.mouse.get_pressed()) 
        #this will basically give true for which mouse button you are pressing 

    pygame.display.update()
    clock.tick(60)  
