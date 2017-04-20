#include pygame which we got from pip
#in order to use pygame, we have to run the init method

import pygame
pygame.init()
clock = pygame.time.Clock()

# 3 Create a screen with a size

screen = {
    "height": 512, #in pixels
    "width": 480,
}

keys = {
    "right": 275,
    "left": 276,
    "up": 273,
    "down":274
}

keys_down = {
    "right": False,
    "left": False,
    "up": False,
    "down":False
}

hero = {
    "x": 100,
    "y": 100,
    "speed": 20

}

goblin = {
    "x": 100,
    "y":100,
    "speed": 20
}

screen_size = (screen["height"], screen["width"]) #requires we give it
#unchanged screen size
pygame_screen = pygame.display.set_mode(screen_size) #object called display,
#has something call set mode with a tuple with screen size
pygame.display.set_caption("Goblin Chase") #methond provided by display coming
#from pygame
background_image = pygame.image.load("./images/background.png")
hero_image = pygame.image.load("./images/hero.png")
goblin_image = pygame.image.load("./images/goblin.png")

# 4 Create the game loop (while 1)
game_on = True
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        elif event.type == pygame.KEYDOWN:
            if event.key == keys['up']:
                keys_down['up'] = True
            if event.key == keys['down']:
                keys_down['down'] = True
            if event.key == keys['left']:
                keys_down['left'] = True
            if event.key == keys['right']:
                keys_down['right'] = True



    # the user let go of a key... and that key was the up arrow
        elif event.type == pygame.KEYUP:
            if event.key == keys['up']:
                keys_down['up'] = False
            if event.key == keys['down']:
                keys_down['down'] = False
            if event.key == keys['left']:
                keys_down['left'] = False
            if event.key == keys['right']:
                keys_down['right'] = False


    #update hero position

    if keys_down['up']:
        hero['y'] -= hero ['speed']
    elif keys_down['down']:
        hero['y'] += hero ['speed']
    if keys_down['left']:
        hero['x'] -= hero ['speed']
    elif keys_down['right']:
        hero['x'] += hero ['speed']



    pygame_screen.blit(background_image, [0,0])
    pygame_screen.blit(hero_image, [hero['x'], hero['y']])
    # pygame_screen.blit(goblin_image, [goblin['x'], goblin['y'])
    pygame.display.flip()




#update our boolean so pygame can escape
# print(event) #will allow you to see everything you do within the pygame window
# pygame.display.update()
# clock.tick(60)
# 5 Add a quit event (requires sys) #won't run without quit event

##we are inside the main game loop. It will run as long as game_on is true
#looping through all events that happen
#this game loop cycle
# Screen.fill (pass bg_color)
# Flip the screen and start ove4
#game loop, waiting for user input
#the user clicked on the red X to elave the game
