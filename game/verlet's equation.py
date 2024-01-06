import pygame

#basic shit
pygame.init()
dis = (500,500)
win = pygame.display.set_mode(dis)
game = True
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
clock = pygame.time.Clock()
gravity = -1.5
wind = 0
friction = 1

#points class
class points:

    points_list = [] # all points in a list

    def updatePoints():
        for i in points.points_list:
            vx = i.rect.x-i.oldx
            vy = i.oldy-i.rect.y
            i.oldx = i.rect.x
            i.oldy = i.rect.y
            i.rect.x += int(vx)
            i.rect.y -= int(vy)
            i.rect.y -= int(gravity)
            
            if (i.rect.x>=dis[0]):
                i.rect.x = dis[0]-5
                i.oldx = i.rect.x+vx*i.bounce
            if (i.rect.x<=0):
                i.rect.x = 0
                i.oldx = i.rect.x+vx*i.bounce
            if (i.rect.y>=dis[1]):
                i.rect.y = dis[1]-5
                i.oldy = i.rect.y-vy*i.bounce
            if (i.rect.y<=0):
                i.rect.y = 0
                i.oldy = i.rect.y-vy*i.bounce

    def constrainPoints():
        for i in points.points_list:
            vx = i.rect.x-i.oldx
            vy = i.oldy-i.rect.y

            if (i.rect.x>=dis[0]):
                i.rect.x = dis[0]-5
                i.oldx = i.rect.x+vx*i.bounce
            if (i.rect.x<=0):
                i.rect.x = 0
                i.oldx = i.rect.x+vx*i.bounce
            if (i.rect.y>=dis[1]):
                i.rect.y = dis[1]-5
                i.oldy = i.rect.y-vy*i.bounce*friction
            if (i.rect.y<=0):
                i.rect.y = 0
                i.oldy = i.rect.y-vy*i.bounce


    def renderPoints():
        for i in points.points_list:
            pygame.draw.rect(win,white,i.rect)
    
    def __init__(self,x,y,oldx,oldy,size = 5,bounce = 0.9):
        self.rect = pygame.Rect([x,y,size,size])
        self.oldx = oldx
        self.oldy = oldy
        points.points_list.append(self)
        self.bounce = bounce

#class sticks
class sticks:
    sticks_list = [] #all sticks in a list
    
    def __init__(self,p1,p2,hidden = False):
        sticks.sticks_list.append(self)
        self.p1 = p1
        self.p2 = p2
        self.size = self.distance()
        self.hidden = hidden

    def distance(self): #finds dist b/w two points of the stick(starting and ending point)
        dx = self.p1.rect.x-self.p2.rect.x
        dy = self.p1.rect.y-self.p2.rect.y
        dist = (dx**2+dy**2)**(1/2)
        return dist

    def updateSticks():#changes the sticks' points' location and maintsins stick size 
        for s in sticks.sticks_list:
            dist = s.distance()
            error = dist-s.size
            try:
                errorPercent = (error/dist)/2
            except:
                errorPercent = 0
            offsetx = (s.p1.rect.x-s.p2.rect.x)*errorPercent
            offsety = (s.p1.rect.y-s.p2.rect.y)*errorPercent
            s.p1.rect.y -= int(offsety)
            s.p1.rect.x -= int(offsetx)
            s.p2.rect.x += int(offsetx)
            s.p2.rect.y += int(offsety)

    def renderSticks():#draws sticks
        for s in sticks.sticks_list:
            if s.hidden == False:
                pygame.draw.line(win,white,(s.p1.rect.x,s.p1.rect.y),(s.p2.rect.x,s.p2.rect.y))

p1 = points(200,200,190,190)#point 1
p2 = points(250,200,200,190)#point 2
p3 = points(200,150,190,180)#point 3
p4 = points(250,150,200,180)#point 4
s1 = sticks(p2,p1)#stick 1
s2 = sticks(p1,p3)#stick 2
s3 = sticks(p3,p2)#stick 3

def gameRun():
    points.updatePoints()
    for i in sticks.sticks_list:
        sticks.updateSticks()
        points.constrainPoints()
    win.fill(black)
    sticks.renderSticks()
    pygame.display.update()
    clock.tick(60)


    

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    gameRun()

pygame.quit()

