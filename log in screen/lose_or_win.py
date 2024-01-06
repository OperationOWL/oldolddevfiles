import pygame
import csv

pygame.init()
dis = (500,500)
win = pygame.display.set_mode(dis)
red = (255,100,100)
black = (0,0,0)
green = (100,255,100)
blue = (120,120,255)
score_display = True #this is to confirm whether score display should be called or not. Setting to True will call a win or a loss depending on the 'victory' variable

#these are the values that must be given to run this program
victory = True #if player won, set to True. If player lost, set to false
user = 'OWL' #this is the 1st attribute of the player in the csv file 'gameInfo.csv'. name should match so that it can be printed

#this function displays the score
def score():
	f = open('gameInfo.csv', 'r', newline = '')
	csv_r = csv.reader(f)
	for i in csv_r:
		if (i[0] == user):
			win.fill(blue)
			font = pygame.font.Font("Roboto-ThinItalic.ttf", 36)

			text = font.render(i[0], True, black, blue)
			textRect = text.get_rect()
			textRect.center = (dis[0] // 2, (dis[1]-350))
			win.blit(text, textRect)

			text = font.render('wins: '+i[2], True, black, blue)
			textRect = text.get_rect()
			textRect.center = (dis[0] // 2, (dis[1]-250))
			win.blit(text, textRect)

			text = font.render('losses: '+i[3], True, black, blue)
			textRect = text.get_rect()
			textRect.center = (dis[0] // 2, (dis[1]-150))
			win.blit(text, textRect)

#this function displays a lose
def lost():
	win.fill(red)
	font = pygame.font.Font("Roboto-ThinItalic.ttf", 36) 
	text = font.render('You Lost', True, black, red)
	textRect = text.get_rect()
	textRect.center = (dis[0] // 2, (dis[1]-300))
	win.blit(text, textRect)
	text = font.render('Haha you suck', True, black, red)
	textRect = text.get_rect()
	textRect.center = (dis[0] // 2, (dis[1]-200))
	win.blit(text, textRect)

#this function ddisplays a win
def won():
	win.fill(green)
	font = pygame.font.Font("Roboto-ThinItalic.ttf", 36) 
	text = font.render('You won', True, black, green)
	textRect = text.get_rect()
	textRect.center = (dis[0] // 2, (dis[1]-300))
	win.blit(text, textRect)
	text = font.render('You are the pinnacle of mankind', True, black, green)
	textRect = text.get_rect()
	textRect.center = (dis[0] // 2, (dis[1]-200))
	win.blit(text, textRect)

while True:
	score()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_RETURN:
				if score_display == True:
					score_display = False
				else:
					quit()
	
	if score_display == True:
		if victory == True:
			won()
		elif victory == False:
			lost()

	pygame.display.update()
