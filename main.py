import pygame

pygame.init()

#all the parameters for the window
win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Pygame Trying Project")

#all the parameters for the character
x = 50
y = 50
w = 30
h = 50
vel = 10
left = False
right = False
walkCounter = 0


def redrawGameWindow():
    global walkCounter
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, w, h))
    pygame.display.update()
    
#main loop
run = True
while run:
    pygame.time.delay(100)
    #closing the game whitout problems
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x <1600 - w - vel:
        x+=vel
    if keys[pygame.K_UP] and y > vel:
        y-=vel
    if keys[pygame.K_DOWN] and y < 900 -h - vel:
        y+=vel
    if keys[pygame.K_a] and x > vel:
        x-=vel
    if keys[pygame.K_d] and x <1600 - w - vel:
        x+=vel
    if keys[pygame.K_w] and y > vel:
        y-=vel
    if keys[pygame.K_s] and y < 900 -h - vel:
        y+=vel
    redrawGameWindow()
#closing the game
pygame.quit()