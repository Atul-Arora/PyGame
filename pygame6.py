#Animating ==> just changing position 
"""surf.convert():
-Returns a surface in display’s pixel format.
-Good for opaque images (JPEGs, fully opaque sprites).

surf.convert_alpha():
-Necessary for PNGs with transparent regions or for per-pixel alpha blending.
-Useful when you need smooth semi-transparent edges."""

import pygame 
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  
test_font=pygame.font.Font("font/Pixeltype.ttf",50)

pygame.display.set_caption("Runner")

sky_surface = pygame.image.load("Graphics/sky.png").convert() 
ground_surface = pygame.image.load("Graphics/ground.png").convert()
text_surface=test_font.render("My Game",False,"Black").convert()
#.convert basically Converting it to the display format lets SDL accelerate blits . Basically better performance in theory

snail_surface=pygame.image.load("Graphics/snail/snail1.png",).convert_alpha()
snail_x_pos = 600 #intial snail x _posn


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(snail_surface,(snail_x_pos,262))
    snail_x_pos -= 4
    
    #Create an if statement that places snail on the right if it goes too far left 
    if snail_x_pos<-100: 
        snail_x_pos=800
    

    pygame.display.update()
    clock.tick(60)  
