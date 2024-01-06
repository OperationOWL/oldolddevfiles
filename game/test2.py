import pygame

pygame.init()
dis = (720,720)
win = pygame.display.set_mode(dis)
game = True
keyboard = {'r':0, 'l':0 ,'u':0, 'd':0}
rect = pygame.Rect(dis[0]//2, 500, 28, 40)
blocks = [pygame.Rect(dis[0]//2, dis[1]//2, 40, 40),pygame.Rect(dis[0]//2+40, dis[1]//2+40, 40, 40)]
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
clock = pygame.time.Clock()

def gamerun():
    move(speed_control())
    win.fill(black)
    pygame.draw.rect(win,white,rect)
    for block in blocks:
        pygame.draw.rect(win,red,block)
    pygame.display.update()

def collisions(rect,blocks):
    collision_list = []
    for block in blocks:
        if rect.colliderect(block):
            collision_list.append(block)
    return collision_list

def move(speed):
    rect.x+=speed[0]
    collision_list = collisions(rect,blocks)
    for block in collision_list:
        if speed[0]>0:
            rect.right = block.left
        if speed[0]<0:
            rect.left = block.right
    rect.y-=speed[1]
    collision_list = collisions(rect,blocks)
    for block in collision_list:
        if speed[1]>0:
            rect.top = block.bottom
        if speed[1]<0:
            rect.bottom = block.top

speed = [0,0]
def speed_control():
    global speed
    if keyboard['l'] == 1:
        speed[0] += -20
    if keyboard['u'] == 1:
        speed[1] += 20
    if keyboard['r'] == 1:
        speed[0] += 20
    if keyboard['d'] == 1:
        speed[1] += -20
    return(speed)
     
while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                keyboard['l'] = 1
            if event.key == ord('d'):
                keyboard['r'] = 1
            if event.key == ord('w') or event.key == pygame.K_SPACE:
                keyboard['u'] = 1
            if event.key == ord('s'):
                keyboard['d'] = 1

        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                keyboard['l'] = 0
            if event.key == ord('d'):
                keyboard['r'] = 0
            if event.key == ord('w') or event.key == pygame.K_SPACE:
                keyboard['u'] = 0
            if event.key == ord('s'):
                keyboard['d'] = 0  

    gamerun()
    clock.tick(60)

pygame.quit()
