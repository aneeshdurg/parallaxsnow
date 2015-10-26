import pygame
import random
 
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 225)
 
SIZE = [1920, 1080]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Parallax Snow")
 
snow_list = []
 
for i in range(500):
    colors=random.randint(1, 3)
    if colors==1:
        color=WHITE
    elif colors==2:
        color=RED
    else:
        color=GREEN 
    x = random.randrange(0, 1920)
    y = random.randrange(0, 1080)
    speed=random.randint(1, 5)
    snow_list.append([color, [x, y], speed])
 
clock = pygame.time.Clock()
x_speed=0
y_speed=0
x_coord=100
y_coord=100
 
done = False
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(BLACK)
            pygame.display.flip()     # Flag that we are done so we exit this loop
            # User pressed down on a key
        
    screen.fill(BLACK)
   
    for i in range(len(snow_list)):
 
        colors=random.randint(1, 4)
        if colors==1:
            color=WHITE
        elif colors==2:
            color=RED
        elif colors==3:
            color=BLUE
        else:
            color=GREEN 
            snow_list[i][0]
        pygame.draw.circle(screen, color, snow_list[i][1], 2)
        
        snow_list[i][1][1] += snow_list[i][2]
        if snow_list[i][1][1] > 1080:
            #snow_list.pop(i)
            # Reset it just above the top
            snow_list[i][1][1] = random.randrange(-20, 0)
            # Give it a new x position
            x = random.randrange(0, 1920)
            snow_list[i][1][0] = int(x)
 
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
