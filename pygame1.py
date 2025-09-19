import pygame 


pygame.init()
screen = pygame.display.set_mode((800,400))  #This intialises everything
#pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #This unintialises everything

    #Draw all elements
    #update everything
    pygame.display.update()

    """You click the ❌ close button on the window.

Pygame sends a QUIT event into its event queue.

Your loop checks:

if event.type == pygame.QUIT:
    pygame.quit()


✅ This line uninitializes Pygame (shuts down graphics, sound, etc.).

👉 BUT the while True: loop is still running.
That means after quitting Pygame, the loop goes back around and runs pygame.display.update(), even though the window is already destroyed.
This can lead to errors like "pygame.error: display Surface quit"."""