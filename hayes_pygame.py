import pygame
from math import fabs
from random import randint
pygame.init()

#-----------Variable------------

screen = {
	"height": 512,
	"width": 480
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
	"down": False,
}

hero = {
	"x": 100,
	"y": 100,
	"speed": 10,
	"wins": 0,
	"is_alive": True
}

goblin = {
	"x": 200,
	"y": 200,
	"speed_x": 5,
	"speed_y": 5,
	"direction": "N"
}

powerup = {
	'active': True,
	'tick_gotten': 0	
}

game_paused = False


directions = ['N','S','E','W','NE','NW','SE','SW']

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('./images/background.png')
hero_image = pygame.image.load('./images/hero.png')
hero_image_scaled = pygame.transform.scale(hero_image, (32,32))
goblin_image = pygame.image.load('images/goblin.png')
powerup_image = pygame.image.load('./images/monster.png')
powerup_image_scaled = pygame.transform.scale(powerup_image, (32,32))

# Add music files
win_sound = pygame.mixer.Sound('./sounds/win.wav')
lose_sound = pygame.mixer.Sound('./sounds/lose.wav')

tick = 0
timer = 0
game_on = True

#---------------Functions---------------

def key_is_pressed():
	if event.type == pygame.KEYDOWN:
		if event.key == keys['up']:
			keys_down['up'] = True
		elif event.key == keys['down']:
			keys_down['down'] = True
		elif event.key == keys['left']:
			# print "User pressed left!"
			keys_down['left'] = True
		elif event.key == keys['right']:
			# print "User pressed right!"
			keys_down['right'] = True
		elif event.key == 121:
			# userpushed "y"
			hero['x'] = 100
			hero['y'] = 100
		elif event.key == 32:
			# user pushed space!
			game_paused = not game_paused
	elif event.type == pygame.KEYUP:
		# print "The user let go of a key"
		if event.key == keys['up']:
			# the user let go of a key... and that key was the up arrow
			keys_down['up'] = False
		if event.key == keys['down']:
			keys_down['down'] = False
		if event.key == keys['left']:
			keys_down['left'] = False
		if event.key == keys['right']:
			keys_down['right'] = False

def hero_move():
	if(not game_paused):
		# Update Hero position
		if keys_down['up']:
			hero['y'] -= hero['speed']
		elif keys_down['down']:
			hero['y'] += hero['speed']
		if keys_down['left']:
			hero['x'] -= hero['speed']
		elif keys_down['right']:
			hero['x'] += hero['speed']

# //////////////////////////////////////////////
# //////////////MAIN GAME LOOP/////////////////
# ////////////////////////////////////////////

while game_on:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# the user clicked on the red X to leave the game
			game_on = False
			# update our boolean, so pygame can escape the loop
		key_is_pressed()
	hero_move()

#///////////////////////
#////////RENDER////////
#/////////////////////
	pygame_screen.blit(background_image, [0,0])

	# Draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])

	if (tick % 30 == 0):
		timer += 1
	timer_text = font.render("Seconds Alive: %d" % (timer), True, (0,0,0))
	pygame_screen.blit(timer_text, [40,100])

	if(game_paused):
		timer_text = font.render("Game Paused. Hit space to unpause", True, (0,0,0))
		pygame_screen.blit(timer_text, [200,300])


	# draw the hero
	pygame_screen.blit(hero_image_scaled, [hero['x'],hero['y']])
	pygame_screen.blit(goblin_image, [goblin['x'],goblin['y']])
	pygame_screen.blit(powerup_image_scaled, [100,200])

	# clear the screen for next time
	pygame.display.flip()





































