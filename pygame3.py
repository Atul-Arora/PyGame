import pygame 
from sys import exit

"""
Create a ceiling and a floor for our frame rate and well creating the ceiling is very easy but creating the floor is much more difficult for the simple reason 
that you can just tell your computer not to run the game faster than a certain speed and if your computer can run a game at 100 frames per second you could just 
tell it to run slower that shouldn't really be a problem however if your computer is too slow to run the game then well you couldn't magically tell it to run faster
and be more capable so to account for the minimum frame rate you just have to be a good video game developer and ensure that there's never too much on the screen 
at the same time for example something that video game developers are very much concerned with but setting the maximum frame rate is very easy to do so 
"""

pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  #make sure the C in Clock() should be capital . 
#By itself this clock object wont do anything but we will call i

pygame.display.set_caption("Runner")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    #Draw all elements
    #update everything
    pygame.display.update()
    clock.tick(60) #This while true will not work faster than 60 times per second 
