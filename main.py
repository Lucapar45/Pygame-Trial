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
vel = 5

#main loop
run = True
while run:
    pygame.time.delay(100)
    #closing the game whitout problems
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x-=vel

    if keys[pygame.K_RIGHT] and x <1600 - w - vel:
        x+=vel

    if keys[pygame.K_UP] and y > vel:
        y-=vel

    if keys[pygame.K_DOWN] and y < 900 -h - vel:
        y+=vel

    win.fill((0, 0, 0))
    #the actual character
    pygame.draw.rect(win, (0, 0, 255), (x, y, w, h))
    pygame.display.update()

#closing the game
pygame.quit()