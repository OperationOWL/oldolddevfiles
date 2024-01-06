#pregame
import imp
import csv,os
import graphics as g
import mysql.connector
account = g.GraphWin('account',500,500)
#account.setBackground('black') 
user =g.Text(g.Point(30,480),'USER: ')
user.draw(account)

##username=Text(Point(90,480),name)
##username.draw(account)

img=g.Image(g.Point(255,75),'logo.png')
img.draw(account)

play_=g.Rectangle(g.Point(160,170),g.Point(360,220))
play_.setWidth(5)
play_.draw(account)
play=g.Text(g.Point(260,195),'PLAY')
play.draw(account)
play.setSize(35)



hwtplay=g.Rectangle(g.Point(75,250),g.Point(425,300))
hwtplay.setWidth(5)
hwtplay.draw(account)
hwtplay=g.Text(g.Point(250,275),'HOW TO PLAY')
hwtplay.draw(account)
hwtplay.setSize(35)
#hwtplay.setStyle('bold')



leadbrd=g.Rectangle(g.Point(50,327),g.Point(450,377))
leadbrd.setWidth(5)
leadbrd.draw(account)
leadbrd=g.Text(g.Point(250,352),'LEADERBOARD')
leadbrd.draw(account)
leadbrd.setSize(35)
#leadbrd.setStyle('bold')


settings=g.Rectangle(g.Point(50,400),g.Point(450,450))
settings.setWidth(5)
settings.draw(account)
settings=g.Text(g.Point(250,425),'SETTINGS')
settings.draw(account)
settings.setSize(35)

logout=g.Rectangle(g.Point(350,470),g.Point(450,490))
logout.setWidth(5)
logout.draw(account)
logout=g.Text(g.Point(400,480),'LOGOUT')
logout.draw(account)

while True:
    try:
        mouse=account.getMouse()
        if mouse.x>(g.Point(160,170)).x and mouse.y>(g.Point(160,170)).y and mouse.x<(g.Point(360,220)).x and mouse.y<(g.Point(360,220)).y :
            play_.setFill('red')

            print('gg')
            import game
        elif mouse.x>(g.Point(75,250)).x and mouse.y>(g.Point(75,250)).y and mouse.x<(g.Point(425,300)).x and mouse.y<(g.Point(425,300)).y :
            time.sleep(0.5)
            f=open('RULES.txt','r')
            rec=f.read()
            rls= g.GraphWin('HOW TO PLAY',1500,500)
            rlstext = g.Text(g.Point(800,250),rec)
            rlstext.draw(rls)
        elif mouse.x>(g.Point(50,327)).x and mouse.y>(g.Point(50,327)).y and mouse.x<(g.Point(450,377)).x and mouse.y<(g.Point(450,377)).y :
            time.sleep(0.5)
            f=open('players.csv','r',newline='')
            rec=csv.reader(f)
            l=''
            for i in rec:
                l+=str(i[0]) + ' : ' + str(i[3]) + '\n'

            led= g.GraphWin('LEADERBOARD',500,500)
            ledtext = g.Text(g.Point(200,250),l)
            ledtext.draw(led)
            
        elif mouse.x>(Point(50,400)).x and mouse.y>(Point(50,400)).y and mouse.x<(Point(450,450)).x and mouse.y<(Point(450,450)).y :
            time.sleep(0.5)
            try:
                imp.reload(settings)
            except:
                import settings
        elif mouse.x>(g.Point(350,470)).x and mouse.y>(g.Point(350,470)).y and mouse.x<(g.Point(450,490)).x and mouse.y<(g.Point(450,490)).y :
            print('gg')
            del g
            print('gg')
            import feedback
                  

    except:
        pass





##            import pygame
##            pygame.init()
##            dis = (500,500)
##            win = pygame.display.set_mode(dis)
##            red = (255,100,100)
##            black=(0,0,0)
##            blue = (120,120,255)
##            white=(255,255,255)
##
##            def feedback():
##                win.fill(white)
##                font = pygame.font.Font("Roboto-ThinItalic.ttf", 36)
##                text = font.render('FEEDBACK', True, black, white)
##                textRect = text.get_rect()
##                textRect.center = (dis[0] // 2, (dis[1]-450))
##                win.blit(text, textRect)
##
##                for i in range(1,11):
##                    j = i*50 - 25
##                    pygame.draw.rect(win, red, pygame.Rect(i*50-45, dis[1]-250-30, 40, 60)) 
##                    text = font.render(f'{i}', True, black)
##                    textRect = text.get_rect()
##                    textRect.center = (j, (dis[1]-250))
##                    win.blit(text, textRect)
##
##            def main():
##                while True:
##                    for event in pygame.event.get():
##                        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
##                            pos=pygame.mouse.get_pos()
##                            for m in range(1,11):
##                                j = m*50 - 25
##                                if pos[0] in range(j-20, j+20) and pos[1] in range(dis[1]-250-29, dis[1]-250+29):
##                                     f=open('current.csv','r',newline='')
##                                     rec=csv.reader(f)
##                                     for i in rec:
##                                         current_user=i[0]
##                                     f.close()
##                                     mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='ashvin')
##                                     cursor=mycon.cursor()
##                                     sql='UPDATE Players SET feedback = %s WHERE name = %s'
##                                     feed=((str(m)),current_user)
##                                     cursor.execute(sql,feed)
##                                     mycon.commit()
##                                     exit()
##                       
##                    feedback()
##                    pygame.display.update()
##                pygame.quit()
##            main()
##          




















