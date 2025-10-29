#Better enemy logic
#TIMERS
# We create a custom user event that is triggered in certain time intervals 
# 1.create a custom event
# 2.tell pygame to trigger that event continously 
# 3.add code in event loop

#NEW OBSTACLE LOGIC 
# 1.We create a list of obstacle rectangles
# 2.everytime the timer triggers we add a new rectangle to that list
# 3.We move every rect in that list to the left on every frame 
# 4.We delete rectangles too far left

import pygame
from sys import exit
from random import randint

def dispay_score():

    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(snail_surf,obstacle_rect)
    return obstacle_list

pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  
test_font = pygame.font.Font("font/Pixeltype.ttf",50)
game_active = False
start_time = 0
score = 0


pygame.display.set_caption("Runner")

sky_surface = pygame.image.load("Graphics/sky.png").convert() 
ground_surface = pygame.image.load("Graphics/ground.png").convert()

# Obstacles
snail_surf = pygame.image.load("Graphics/snail/snail1.png",).convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300) )

obstacle_rect_list=[]


player_surf = pygame.image.load("Graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

# Intro Screen 
player_stand = pygame.image.load("Graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200));

game_name = test_font.render("Pixel Runner","False",(111,196,169))
game_name_rect = game_name.get_rect(center=(400,80))

game_msg = test_font.render("Press space to run", False ,(111,196,169))
game_msg_rect = game_msg.get_rect(center=(400,320))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos) and player_rect.bottom == 300 : 
                        player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300 :
                    player_gravity = -21

            if event.type == obstacle_timer:
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
        
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active =1 
                snail_rect.x=800
                start_time=int(pygame.time.get_ticks()/1000)

       

               
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        
        score = dispay_score()

       

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >=300 : player_rect.bottom = 300
        screen.blit(player_surf,player_rect) 

        #Obstacle movement 
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        score_message = test_font.render(f"Your Score: {score}", False ,(111,196,169))
        score_message_rect = score_message.get_rect(center=(400,330))
        screen.blit(game_name,game_name_rect)
        if score == 0: screen.blit(game_msg,game_msg_rect)
        else: screen.blit(score_message,score_message_rect)
       


    pygame.display.update()
    clock.tick(60)  


