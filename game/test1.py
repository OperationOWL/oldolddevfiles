import pygame

pygame.init()
dis = (720,720)
win = pygame.display.set_mode(dis)
game = True
keyboard = {'r':0, 'l':0 ,'u':0, 'd':0}
rect1 = pygame.Rect(500, 500, 40, 40)
block = pygame.Rect(dis[0]//2, dis[1]//2, 80, 80)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
clock = pygame.time.Clock()

def gamerun():
    move()
    win.fill(black)
    pygame.draw.rect(win,white,rect1)
    pygame.draw.rect(win,red,block)
    pygame.display.update()

def collision():
    collide_list = {'r':0, 'l':0 ,'u':0, 'd':0}
    if rect1.colliderect(block):
        if abs(rect1.bottom-block.top) < 5:
            print('bottom collided')
            rect1.bottom = block.top
            collide_list['d'] = 1
        if abs(rect1.top-block.bottom) < 5:
            rect1.top = block.bottom
            collide_list['u'] = 1
        if abs(rect1.right-block.left) < 5:
            rect1.right = block.left
            collide_list['r'] = 1
        if abs(rect1.left-block.right) < 5:
            rect1.left = block.right
            collide_list['l'] = 1

    else:
        collide_list = {'r':0, 'l':0 ,'u':0, 'd':0}

    return collide_list



def move():
    collide_list = collision()
    if keyboard['r'] == 1:
        if collide_list['r'] == 0:
            rect1.x+=3
    if keyboard['l'] == 1:
        if collide_list['l'] == 0:
            rect1.x-=3
    if keyboard['u'] == 1:
        if collide_list['u'] == 0:
            rect1.y-=3
    if keyboard['d'] == 1:
        if collide_list['d'] == 0:
            rect1.y+=3

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