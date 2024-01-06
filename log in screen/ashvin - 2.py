#pregame
import imp
import csv,os
from graphics import *
import pygame



account = GraphWin('account',500,500)
#account.setBackground('black')

f=open('current.csv','r',newline='')
rec=csv.reader(f)
for i in rec:
    name=i[0]
f.close()

user = Text(Point(30,480),'USER : ')
user.draw(account)

username=Text(Point(80,480),name)
username.draw(account)

img=Image(Point(255,75),'logo.png')
img.draw(account)

play_=Rectangle(Point(160,170),Point(360,220))
play_.setWidth(5)
play_.draw(account)
play=Text(Point(260,195),'PLAY')
play.draw(account)
play.setSize(35)



hwtplay=Rectangle(Point(75,250),Point(425,300))
hwtplay.setWidth(5)
hwtplay.draw(account)
hwtplay=Text(Point(250,275),'HOW TO PLAY')
hwtplay.draw(account)
hwtplay.setSize(35)
#hwtplay.setStyle('bold')



leadbrd=Rectangle(Point(50,327),Point(450,377))
leadbrd.setWidth(5)
leadbrd.draw(account)
leadbrd=Text(Point(250,352),'LEADERBOARD')
leadbrd.draw(account)
leadbrd.setSize(35)
#leadbrd.setStyle('bold')


settings=Rectangle(Point(50,400),Point(450,450))
settings.setWidth(5)
settings.draw(account)
settings=Text(Point(250,425),'SETTINGS')
settings.draw(account)
settings.setSize(35)

logout=Rectangle(Point(350,470),Point(450,490))
logout.setWidth(5)
logout.draw(account)
logout=Text(Point(400,480),'LOGOUT')
logout.draw(account)

while True:
    try:
        mouse=account.getMouse()
        if mouse.x>(Point(160,170)).x and mouse.y>(Point(160,170)).y and mouse.x<(Point(360,220)).x and mouse.y<(Point(360,220)).y :
            play_.setFill('red')
            time.sleep(0.25)
            import game
        elif mouse.x>(Point(75,250)).x and mouse.y>(Point(75,250)).y and mouse.x<(Point(425,300)).x and mouse.y<(Point(425,300)).y :
            time.sleep(0.5)
            f=open('RULES.txt','r')
            rec=f.read()
            rls= GraphWin('HOW TO PLAY',1500,500)
            rlstext = Text(Point(800,250),rec)
            rlstext.draw(rls)
        elif mouse.x>(Point(50,327)).x and mouse.y>(Point(50,327)).y and mouse.x<(Point(450,377)).x and mouse.y<(Point(450,377)).y :
            time.sleep(0.5)
            f=open('players.csv','r',newline='')
            rec=csv.reader(f)
            l=''
            for i in rec:
                l+=str(i[0]) + ' : ' + str(i[3]) + '\n'

            led= GraphWin('LEADERBOARD',500,500)
            ledtext = Text(Point(200,250),l)
            ledtext.draw(led)
            
        elif mouse.x>(Point(50,400)).x and mouse.y>(Point(50,400)).y and mouse.x<(Point(450,450)).x and mouse.y<(Point(450,450)).y :
            time.sleep(0.5)
            try:
                imp.reload(settings)
            except:
                import settings
        elif mouse.x>(Point(350,470)).x and mouse.y>Point(350,470).y and mouse.x<(Point(450,490)).x and mouse.y<(Point(450,490)).y :

            pygame.init()
            dis = (500,500)
            win = pygame.display.set_mode(dis)
            red = (255,100,100)
            black = (0,0,0)
            green = (100,255,100)
            blue = (120,120,255)
            score_display = True
            def feedback():
                win.fill(blue)
                font = pygame.font.Font("Roboto-ThinItalic.ttf", 36)
                text = font.render('enter feedback', True, black, blue)
                textRect = text.get_rect()
                textRect.center = (dis[0] // 2, (dis[1]-450))
                win.blit(text, textRect)

                for i in range(1,11):
                    j = i*50 - 25
                    pygame.draw.rect(win, red, pygame.Rect(i*50-45, dis[1]-250-30, 40, 60)) 
                    text = font.render(f'{i}', True, black)
                    textRect = text.get_rect()
                    textRect.center = (j, (dis[1]-250))
                    win.blit(text, textRect)

            def main():
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key==pygame.K_RETURN:
                                if score_display == True:
                                    score_display = False
                                else:
                                    quit()
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                            for m in range(1,11):
                                j = m*50 - 25
                                if pygame.mouse.get_pos()[0] in range(j-20, j+20) and pygame.mouse.get_pos()[1] in range(dis[1]-250-18, dis[1]-250+18):
                                     f=open('current.csv','r',newline='')
                                     rec=csv.reader(f)
                                     for i in rec:
                                         current_user=i[0]
                                     f.close()
                                     mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='ashvin')
                                     cursor=mycon.cursor()
                                     sql='UPDATE Players SET feedback = %s WHERE name = %s'
                                     feed=((str(m)),current_user)
                                     cursor.execute(sql,feed)
                                     mycon.commit()
                                     exit()
                       
                    feedback()
                    pygame.display.update()
                pygame.quit()
                main()
                exit()

    except:
        pass