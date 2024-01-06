import pygame
import csv
import os

pygame.init()
dis = (500,500)
win = pygame.display.set_mode(dis)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
size = 1
clock = pygame.time.Clock()
login = {'start':0,'name':1, 'password':1, 'startover':1, 'error':1}
info = {'name':'', 'password':''}

def expandingCircle():
	global size
	pygame.draw.circle(win, white, (dis[0]//2,dis[1]//2), size, 1)
	if size<250:
		size+=1
		return False
	else:
		return True

def shrinkingCircle():
	global size
	pygame.draw.circle(win, white, (dis[0]//2,dis[1]//2), size, 1)
	if size>1:
		size-=1
		return False
	else:
		return True

def start():
	global login
	finished = expandingCircle()
	if finished == True:
		font = pygame.font.Font("Roboto-ThinItalic.ttf", 32) 
		text = font.render('press enter to start', True, white, black)
		textRect = text.get_rect()   
		textRect.center = (dis[0] // 2, dis[1] // 2)
		win.blit(text, textRect)

def name():
	global login
	finished = expandingCircle()
	if finished == True:
		font = pygame.font.Font("Roboto-ThinItalic.ttf", 32) 
		if info['name'] == '':
			text = font.render('enter name here', True, white, black)
		else:
			text = font.render(info['name'], True, white, black)
		textRect = text.get_rect()   
		textRect.center = (dis[0] // 2, dis[1] // 2)
		win.blit(text, textRect)

def password():
	global login
	finished = expandingCircle()
	if finished == True:
		font = pygame.font.Font("Roboto-ThinItalic.ttf", 32) 
		if info['password'] == '':
			text = font.render('enter password here', True, white, black)
		else:
			text = font.render(info['password'], True, white, black)
		textRect = text.get_rect()   
		textRect.center = (dis[0] // 2, dis[1] // 2)
		win.blit(text, textRect)

def startover():
	global login
	finished = expandingCircle()
	if finished == True:
		font = pygame.font.Font("Roboto-ThinItalic.ttf", 22) 
		text = font.render('press backspace to edit info or enter to continue', True, white, black)
		textRect = text.get_rect()   
		textRect.center = (dis[0] // 2, dis[1] // 2)
		win.blit(text, textRect)

def nameAndPasswordCheck():
	f2 = open('temp.csv', 'w', newline = '')
	f1 = open('gameInfo.csv', 'r', newline = '')
	csv_r = csv.reader(f1)
	csv_w = csv.writer(f2)
	for i in csv_r:
		csv_w.writerow(i)
		if (i[0]==info['name'] and i[1]==info['password']):
			f1.close()
			f2.close()
			return True
		elif i[0] == info['name'] and i[1] != info['password']:
			f1.close()
			f2.close()
			return False
	csv_w.writerow([info['name'], info['password'], 0, 0])
	f1.close()
	f2.close()
	os.remove('gameInfo.csv')
	os.rename('temp.csv', 'gameInfo.csv')
	return True


def error():
	global login
	win.fill(red)
	font = pygame.font.Font("Roboto-ThinItalic.ttf", 22) 
	text = font.render('You have entered wrong password', True, black, red)
	textRect = text.get_rect()
	textRect.center = (dis[0] // 2, (dis[1]-30)//3)
	win.blit(text, textRect)
	text = font.render('for the given username', True, black, red)
	textRect = text.get_rect()
	textRect.center = (dis[0] // 2, (dis[1]-30)*2 // 3)
	win.blit(text, textRect)
	text = font.render('Login again. Press enter to continue', True, black, red)
	textRect = text.get_rect()
	textRect.center = (dis[0] // 2, dis[1]-30)
	win.blit(text, textRect)
	if login['error'] == 0:
		login = {'start':0, 'name':1, 'password':1, 'startover':1, 'error':1}

def main():
	global login
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
			    if event.key==pygame.K_RETURN:
			    	if login['start'] == 0:
			    		login['start'] = 1
			    	elif login['name'] == 0:
			    		login['name'] = 1
			    	elif login['password'] == 0:
			    		login['password'] = 1
			    	elif login['startover'] == 0:
			    		login['startover'] = 1
			    	elif login['error'] == 1:
			    		login['error'] = 0
			    elif login['name'] == 0:
			    	if event.key==pygame.K_BACKSPACE:
			    		info['name'] = info['name'][0:-1]
			    	else:
			    		info['name'] += event.unicode
			    elif login['password'] == 0:
			    	if event.key==pygame.K_BACKSPACE:
			    		info['password'] = info['password'][0:-1]
			    	else:
			    		info['password'] += event.unicode
			    elif login['startover'] == 0:
			    	if event.key == pygame.K_BACKSPACE:
			    		login = {'start':0, 'name':1, 'password':1, 'startover':1, 'error':1}
		win.fill(black)
		if login['start'] == 0:
			start()
		elif login['name'] == 0:
			name()
		elif login['password'] == 0:
			password()
		elif login['startover'] == 0:
			startover()
		elif login['start'] == 1:
			if shrinkingCircle():
				login['name'] = 0
				login['start'] = 2
		elif login['name'] == 1:
			if shrinkingCircle():
				login['password'] = 0
				login['name'] = 2
		elif login['password'] == 1:
			if shrinkingCircle():
				login['startover'] = 0
				login['password'] = 2
		elif login['startover'] == 1:
			shrinkingCircle()
			if nameAndPasswordCheck() == True:
				return info
				break
			else:
				error()
		pygame.display.update()
		clock.tick(600)
	pygame.display.quit()