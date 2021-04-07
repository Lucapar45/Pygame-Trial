import pygame

pygame.init()

logo = pygame.image.load('radioactive_icon.ico')

#all the parameters for the window
win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Radioactive - The Game")
pygame.display.set_icon(logo)

#import the sprites
up = pygame.image.load('sprites/walking_up_sprite.png')
down = pygame.image.load('sprites/walking_down_sprite.png')
right = pygame.image.load('sprites/walking_right_sprite.png')
left = pygame.image.load('sprites/walking_left_sprite.png')
char_up = pygame.image.load('sprites/standing_up_sprite.png')
char_down = pygame.image.load('sprites/standing_down_sprite.png')
char_right = pygame.image.load('sprites/standing_right_sprite.png')
char_left = pygame.image.load('sprites/standing_left_sprite.png')

#all the parameters for the character
x = 50
y = 50
w = 36
h = 45
v = 0.6
walking = False
l = False
r = False
u = False
d = False


def redrawGameWindow():
    win.fill((0, 0, 0))
    win.blit(char_right, (x, y))
    if walking == False and u == True:
        win.blit(char_up, (x, y))
    if walking == False and d == True:
        win.blit(char_down, (x, y))
    if walking == False and r == True:
        win.blit(char_right, (x, y))
    if walking == False and l == True:
        win.blit(char_left, (x, y))
    if walking == True and u == True:
        win.blit(up, (x, y))
    if walking == True and d == True:
        win.blit(down, (x, y))
    if walking == True and l == True:
        win.blit(left, (x, y))
    if walking == True and r == True:
        win.blit(right, (x, y))
    pygame.display.update()

#main loop
run = True
while run:
    pygame.time.delay(1)
    #closing the game whitout problems
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= v:
        x-=v
        l = True
        r = False
        u = False
        d = False
        walking = True

    if keys[pygame.K_RIGHT] and x <1600 - w:
        x+=v
        r = True
        l = False
        u = False
        d = False
        walking = True

    if keys[pygame.K_UP] and y >= v:
        y-=v
        u = True
        r = False
        l = False
        d = False
        walking = True

    if keys[pygame.K_DOWN] and y < 900 -h :
        y+=v
        d = True
        r = False
        l = False
        u = False
        walking = True

    if keys[pygame.K_a] and x >= v:
        x-=v
        l = True
        r = False
        u = False
        d = False
        walking = True

    if keys[pygame.K_d] and x <1600 - w:
        x+=v
        r = True
        l = False
        u = False
        d = False
        walking = True

    if keys[pygame.K_w] and y >= v:
        y-=v
        u = True
        r = False
        l = False
        d = False
        walking = True

    if keys[pygame.K_s] and y < 900 -h :
        y+=v
        d = True
        r = False
        l = False
        u = False
        walking  = True

    redrawGameWindow()
    walking = False


#closing the game
pygame.quit()