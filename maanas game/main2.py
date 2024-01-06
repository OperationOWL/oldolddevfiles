import pygame
import csv
import logIn
import player2
import os

info = logIn.main()
victory = player2.main()
pygame.init()
dis = (500, 500)
win = pygame.display.set_mode(dis)
pygame.display.set_caption("Player 2")
red = (255, 100, 100)
black = (0, 0, 0)
green = (100, 255, 100)
blue = (120, 120, 255)
score_display = True
user = info['name']


def score():
    score_update(victory)
    f = open('gameInfo.csv', 'r', newline='')
    csv_r = csv.reader(f)
    for i in csv_r:
        if i[0] == user:
            win.fill(blue)
            font = pygame.font.Font("Roboto-ThinItalic.ttf", 36)

            text = font.render(i[0], True, black, blue)
            textRect = text.get_rect()
            textRect.center = (dis[0] // 2, (dis[1] - 350))
            win.blit(text, textRect)

            text = font.render('wins: ' + i[2], True, black, blue)
            textRect = text.get_rect()
            textRect.center = (dis[0] // 2, (dis[1] - 250))
            win.blit(text, textRect)

            text = font.render('losses: ' + i[3], True, black, blue)
            textRect = text.get_rect()
            textRect.center = (dis[0] // 2, (dis[1] - 150))
            win.blit(text, textRect)
    f.close()


# this function displays a lose
def lost():
    win.fill(red)
    font = pygame.font.Font("Roboto-ThinItalic.ttf", 36)
    text = font.render('You Lost', True, black, red)
    textRect = text.get_rect()
    textRect.center = (dis[0] // 2, (dis[1] - 300))
    win.blit(text, textRect)
    text = font.render('Haha you suck', True, black, red)
    textRect = text.get_rect()
    textRect.center = (dis[0] // 2, (dis[1] - 200))
    win.blit(text, textRect)

def score_update(victory):
    f2 = open('temp.csv', 'w', newline = '')
    f1 = open('gameInfo.csv', 'r', newline = '')
    csv_r = csv.reader(f1)
    csv_w = csv.writer(f2)
    for i in csv_r:
        if (i[0]==info['name']):
            if vicotry == True:
                csv_w.writerow([i[0], i[1], int(i[2])+1, int(i[2])])
            elif victory == False:
                csv_w.writerow([i[0], i[1], int(i[2]), int(i[2])+1])
        else:
            csv_w.writerow(i)
    f1.close()
    f2.close()
    os.remove('gameInfo.csv')
    os.rename('temp.csv', 'gameInfo.csv')

# this function ddisplays a win
def won():
    win.fill(green)
    font = pygame.font.Font("Roboto-ThinItalic.ttf", 36)
    text = font.render('You won', True, black, green)
    textRect = text.get_rect()
    textRect.center = (dis[0] // 2, (dis[1] - 300))
    win.blit(text, textRect)
    text = font.render('You are the pinnacle of mankind', True, black, green)
    textRect = text.get_rect()
    textRect.center = (dis[0] // 2, (dis[1] - 200))
    win.blit(text, textRect)


while True:
    score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if score_display:
                    score_display = False
                else:
                    quit()

    if score_display:
        if victory:
            won()
        elif not victory:
            lost()

    pygame.display.update()
