import pygame

pygame.init()
dis = (1280,720)
game = True
win = pygame.display.set_mode(dis)
gravity = -1
blocks = []
blocksFull = 0
clock = pygame.time.Clock()

class player:

    global gravity

    def __init__(self):
        self.body_width = 56
        self.body_height = 80
        self.keyboard = {'r':0,'u':0,'l':0} #[r,u,l]
        self.body = pygame.transform.scale(pygame.image.load('sprite-0001.png'),(self.body_width,self.body_height))
        self.velocity = 1
        self.velocitx = 0
        self.acceleration = gravity
        self.collision_list = {'r':0, 'l':0, 'u':0, 'd':0}
        self.rect = pygame.Rect(360,360,self.body_width,self.body_height)
        self.scroll = [0,0]
        self.jump = 0
        self.jump_limiter = 2
        
    def move(self):

        
        if self.keyboard['r'] == 1:
            self.velocitx = 5
        elif self.keyboard['l'] == 1:            
            self.velocitx = -5
        elif self.keyboard['r'] == 0:
            self.velocitx = 0
        elif self.keyboard['l'] == 0:
            self.velocitx = 0
        self.collisionsx()

        if self.keyboard['u'] == 1:
            if self.jump!=self.jump_limiter:
                self.jump+=1
                self.acceleration = 20
                if self.velocity < 20 and self.velocity > -20:
                    self.velocity += self.acceleration
                if self.velocity >= 20:
                    self.velocity = 19
                if self.velocity <= -20:
                    self.velocity = -19
                self.keyboard['u'] = 0
            
        elif self.jump==self.jump_limiter or self.keyboard['u'] == 0:
            self.acceleration = -1
            if self.velocity < 20 and self.velocity > -20:
                self.velocity += self.acceleration
            if self.velocity >= 20:
                self.velocity = 19
            if self.velocity <= -20:
                self.velocity = -19
        self.collisionsy()
        self.scroll_modifier()
    

    def appear(self):
            win.blit(p.body, (self.rect.x-self.scroll[0], self.rect.y-self.scroll[1]))

    def collisionsy(self):
        self.rect.y -= int(self.velocity)
        collision_list = []
        for block in blocks:
            if self.rect.colliderect(block):
                collision_list.append(block)
        for block in collision_list:
            if self.velocity>0:
                self.rect.top = block.bottom
                self.velocity=0
            if self.velocity<0:
                self.rect.bottom = block.top
                self.velocity=0
                self.jump_limiter = 2
                self.jump = 0

    def scroll_modifier(self):
        self.scroll[0] += self.rect.x-self.scroll[0]-dis[0]//2
        self.scroll[1] += self.rect.y-self.scroll[1]-dis[1]//2

    def collisionsx(self):
        self.rect.x += int(self.velocitx)
        collision_list = []
        for block in blocks:
            if self.rect.colliderect(block):
                collision_list.append(block)
        for block in collision_list:
            if self.velocitx>0:
                self.rect.right = block.left
            if self.velocitx<0:
                self.rect.left = block.right


        
def map_printer():

    global dis
    global blocks
    global blocksFull

    file = r'C:\Users\suren\OneDrive\Desktop\game\maap.txt'

    f = open(file, 'r')
    r = f.readlines()
    r = r[-1::-1]

    pic1 = pygame.Surface((40, 40))
    pic1.fill((255, 255, 255))

    pic2 = pygame.Surface((40, 40))
    pic2.fill((255, 255, 255))

    block_size = 40

    pic1 = pygame.image.load('sprite-0002.png')
    pic2 = pygame.image.load('sprite-0002.png')
    pic1 = pygame.transform.scale(pic1, (block_size, block_size))
    pic2 = pygame.transform.scale(pic1, (block_size, block_size))
    x = 0
    y = (dis[1] - block_size)

    x_offset = block_size
    y_offset = block_size

    for i in r:
        for j in i:
            if j == '0':
                x += x_offset
            if j == '1':
                win.blit(pic1, (x-p.scroll[0], y-p.scroll[1]))
                if blocksFull == 0:
                    blocks.append(pygame.Rect(x,y,block_size,block_size))
                x += x_offset
            if j == '2':
                win.blit(pic2, (x-p.scroll[0], y-p.scroll[1]))
                if blocksFull == 0:
                    blocks.append(pygame.Rect(x,y,block_size,block_size))
                x += x_offset
            if j == "\n":
                y -= y_offset
                x = 0

    f.close()
    blocksFull = 1




p = player()

def gamerun():
    p.move()
    win.fill((0,0,0))
    p.appear()
    map_printer()
    pygame.display.update()



while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                p.keyboard['l'] = 1
            if event.key == ord('d'):
                p.keyboard['r'] = 1
            if event.key == ord('w') or event.key == pygame.K_SPACE:
                p.keyboard['u'] = 1
                p.velocity = 0

        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                p.keyboard['l'] = 0
            if event.key == ord('d'):
                p.keyboard['r'] = 0
            if event.key == ord('w') or event.key == pygame.K_SPACE:
                p.keyboard['u'] = 0

    gamerun()
    clock.tick(60)

pygame.quit()
