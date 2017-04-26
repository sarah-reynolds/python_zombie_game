import pygame
import time
from math import fabs
from random import randint

pygame.init()

screen_wh = {
    "display_width": 480,
    "display_height": 512
}

keys = {
     "right": 275,
     "left": 276,
     "up": 273,
     "down": 274
 }

keys_down = {
     "right": False,
     "left": False,
     "up": False,
     "down": False
 }
hero_dict = {
    "x": 100,
    "y": 100,
    "speed": 10,
    "wins": 0,
    "Death": 0
}
goblin_dict = {
    "x": 200,
    "y": 200,
    "speed": 10,
    "direction": "N"
}
monster_dict = {
    "x": 50,
    "y": 50
}
hero_width = 10
screen_size = (screen_wh["display_height"], screen_wh["display_width"])
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Adventure Time Goblin Game")
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

background_img = pygame.image.load("images/bg8bit.png")
hero_img = pygame.image.load("images/finn.png")
goblin_img = pygame.image.load("images/iceking.png")
monster_img = pygame.image.load("images/monster.png")
game_on = True
tick = 0

directions = ['N','S','E','W','NW','NE','SE','SW']
# def monster_moving():
#     while monster_dict["x"] > 0 and monster_dict["x"] < screen_wh["display_width"] - 32:
#         monster_dict["x"] += 5
#     while monster_dict["y"] > 0 and monster_dict["y"] < screen_wh["display_height"] - 32:
#         monster_dict["y"] += 5

def keydown():
    
    if event.type == pygame.KEYDOWN:  # keydown means a user pressed a key
        if event.key == pygame.K_LEFT:
                keys_down["left"] = True
        elif event.key == pygame.K_RIGHT:
            keys_down["right"] = True
        elif event.key == keys["down"]:
            keys_down["down"] = True
        elif event.key == keys["up"]:
            keys_down["up"] = True
    elif event.type == pygame.KEYUP:
        for key in keys_down:
            keys_down[key] = False

def goblin_movement(monster):
    if (monster['direction'] == "N"):
        monster['x'] += monster['speed']
    if (monster['direction'] == "S"):
        monster['x'] -= monster['speed']
    if (monster['direction'] == "E"):
        monster['y'] += monster['speed']
    if (monster['direction'] == "W"):
        monster['y'] -= monster['speed']

def hero_movement():
    if keys_down["up"]:
        if hero_dict["y"] > 0:
            hero_dict["y"] -= hero_dict["speed"]
    if keys_down["down"]:
        if hero_dict["y"] < screen_wh["display_height"] - 64:
            hero_dict["y"] += hero_dict["speed"]
    if keys_down["left"]:
        if hero_dict["x"] > 0:
            hero_dict["x"] -= hero_dict["speed"]
    if keys_down["right"]:
        if hero_dict["x"] < screen_wh["display_width"]:
            hero_dict["x"] += hero_dict["speed"]

# ------------MAIN LOOP----------
while game_on:
    tick += 1
    print tick
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        keydown()

    hero_movement()

    # if hero_dict["x"] < 0:
    #     hero_dict["x"] = 10
    # if hero_dict["x"] > screen_wh["display_width"] - 10:
    #     hero_dict["x"] = screen_wh["display_width"] - 10
    # if hero_dict["y"] < 0:
    #     hero_dict["y"] = 10
    # if hero_dict["y"] > screen_wh["display_height"] - 64:
    #     hero_dict["y"] = screen_wh["display_height"] - 64
    goblin_movement(goblin_dict)

    if (tick % 60 == 0):
        new_dir_index = randint(0,len(directions)-1)
        goblin_dict['direction'] = directions[new_dir_index]

    # collision detection
    if abs(hero_dict["x"] - goblin_dict["x"]) + abs(hero_dict["y"] - goblin_dict["y"]) < 32:
        goblin_dict["x"] = randint(0, 450)
        goblin_dict["y"] = randint(0, 482)
        hero_dict["wins"] += 1

    # monster eats the hero
    if abs(hero_dict["x"] - monster_dict["x"]) + abs(hero_dict["y"] - monster_dict["y"]) < 32:
        monster_dict["x"] = randint(0, 450)
        monster_dict["y"] = randint(0, 482)
        hero_dict["x"] = 0
        hero_dict["y"] = 0
        hero_dict["Death"] += 1
    screen.fill(white)
    screen.blit(background_img, [0, 0])
    font = pygame.font.Font(None, 25)
    wins_font = font.render("WINS: %d" % hero_dict["wins"], True, red)
    screen.blit(wins_font, [40, 40])
    death_font = font.render("Death: %d" % hero_dict["Death"], True, (0, 0, 0))
    screen.blit(death_font, [410, 410])
    screen.blit(hero_img, [hero_dict["x"], hero_dict["y"]])
    screen.blit(goblin_img, [goblin_dict["x"], goblin_dict["y"]])
    screen.blit(monster_img, [monster_dict["x"], monster_dict["y"]])
    pygame.display.update()
    clock.tick(60)
