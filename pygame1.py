import pygame 


pygame.init()
screen = pygame.display.set_mode((800,400))  #This intialises everything
#pygame.display.set_mode((width,height))

while True:  
    #This creates an infinite loop "game loop" so game can keep continously running. Inside this you check for inputs,update,redraw
    
    for event in pygame.event.get():  
        #returns a list of all event that happened since last frame(for loop goes through each event 1 by 1 )
        
        if event.type == pygame.QUIT: 
            #pygame.QUIT(ALL CAPS)-is a constant defined inside pygame-represent the event type for when close is clicked 
            
            pygame.quit() #This unintialises everything [ This is a function (method call) ]

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