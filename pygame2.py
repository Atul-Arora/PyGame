import pygame 
from sys import exit
"""Sys module is something inbuilt into python and gives access to diff system cmd- one of these is exit cmd which breaks the code entirely"""

pygame.init()
screen = pygame.display.set_mode((800,400))  #Setting the window title via pygame.display.set_caption("Game Title").



pygame.display.set_caption("Runner")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() #Once we call this exit the while true loop will also be gone 
    #Draw all elements
    #update everything
    pygame.display.update()
