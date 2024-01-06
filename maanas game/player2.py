import pygame, network


class player:

    def __init__(self):
        self.health = 640
        self.body_width = 42
        self.body_height = 60
        self.keyboard = {'r': 0, 'u': 0, 'l': 0}  # [r,u,l]
        self.body = pygame.Surface((self.body_width, self.body_height))
        self.body.fill((0, 0, 255))
        self.velocity = 1
        self.velocitx = 0
        self.acceleration = -1
        self.collision_list = {'r': 0, 'l': 0, 'u': 0, 'd': 0}
        self.rect = pygame.Rect(480, 360, self.body_width, self.body_height)
        self.scroll = [0, 8640]
        self.jump = 0
        self.jump_limiter = 2

    def move(self, blocks):

        if self.keyboard['r'] == 1:
            self.velocitx = 8
        elif self.keyboard['l'] == 1:
            self.velocitx = -8
        elif self.keyboard['r'] == 0:
            self.velocitx = 0
        elif self.keyboard['l'] == 0:
            self.velocitx = 0
        self.collisionsx(blocks)

        if self.keyboard['u'] == 1:
            if self.jump == self.jump_limiter:
                self.acceleration = -1
                if 25 > self.velocity > -25:
                    self.velocity += self.acceleration
                if self.velocity >= 25:
                    self.velocity = 24
                if self.velocity <= -25:
                    self.velocity = -24
            else:
                self.jump += 1
                self.acceleration = 25
                if 25 > self.velocity > -25:
                    self.velocity += self.acceleration
                if self.velocity >= 25:
                    self.velocity = 24
                if self.velocity <= -25:
                    self.velocity = -24
                self.keyboard['u'] = 0

        elif self.keyboard['u'] == 0:
            self.acceleration = -1
            if 25 > self.velocity > -25:
                self.velocity += self.acceleration
            if self.velocity >= 25:
                self.velocity = 24
            if self.velocity <= -25:
                self.velocity = -24
        self.collisionsy(blocks)
        self.scroll_modifier()

    def appear(self, win):
        win.blit(self.body, (640, 360))

    def collisionsy(self, blocks):
        self.rect.y -= int(self.velocity)
        collision_list = []
        for block in blocks:
            if self.rect.colliderect(block):
                collision_list.append(block)
        for block in collision_list:
            if self.velocity > 0:
                self.rect.top = block.bottom
                self.velocity = 0
            if self.velocity < 0:
                self.rect.bottom = block.top
                self.velocity = 0
                self.jump_limiter = 2
                self.jump = 0

    def scroll_modifier(self):
        self.scroll[0] += self.rect.x - self.scroll[0] - 640
        self.scroll[1] += self.rect.y - self.scroll[1] - 360

    def collisionsx(self, blocks):
        self.rect.x += int(self.velocitx)
        collision_list = []
        for block in blocks:
            if self.rect.colliderect(block):
                collision_list.append(block)
        for block in collision_list:
            if self.velocitx > 0:
                self.rect.right = block.left
            if self.velocitx < 0:
                self.rect.left = block.right


def map_printer(win, dis, blocks, blocksFull, p):
    file = r'maap.txt'

    f = open(file, 'r')
    r = f.readlines()
    r = r[-1::-1]

    block_size = 60

    pic1 = pygame.Surface((block_size, block_size))
    pic1.fill((255, 255, 255))

    pic2 = pygame.Surface((block_size, block_size))
    pic2.fill((255, 255, 255))

    pic1 = pygame.Surface((block_size, block_size))
    pic1.fill((100, 100, 100))
    x = 0
    y = (dis[1] - block_size)

    x_offset = block_size
    y_offset = block_size

    for i in r:
        for j in i:
            if j == '0':
                x += x_offset
            if j == '1':
                win.blit(pic1, (x - p.scroll[0], y - p.scroll[1]))
                if blocksFull == 0:
                    blocks.append(pygame.Rect(x, y, block_size, block_size))
                x += x_offset
            if j == '2':
                win.blit(pic2, (x - p.scroll[0], y - p.scroll[1]))
                if blocksFull == 0:
                    blocks.append(pygame.Rect(x, y, block_size, block_size))
                x += x_offset
            if j == "\n":
                y -= y_offset
                x = 0

    f.close()
    blocksFull = 1
    return blocksFull


def recvl(ch):
    x = ch.split(",")
    return [int(x[0]), int(x[1]), int(x[2])]


def sendtpl(t):
    return str(t[0]) + ',' + str(t[1]) + ',' + str(t[2])


def main():
    pygame.init()
    size = (1280, 720)
    game = True
    win = pygame.display.set_mode(size)
    pygame.display.set_caption("Player 2")
    blocks = []
    blocksFull = 0
    clock = pygame.time.Clock()
    p = player()
    p2 = pygame.Surface((42, 60))
    p2.fill((255, 0, 0))
    net = network.Network()
    spos = net.pos
    damage = 0
    damage_counter = 0

    while game:
        aim = False
        pos2 = recvl(net.send(sendtpl((p.rect.x, p.rect.y, damage))))

        if p.health <= 0:
            pygame.quit()
            return False
        if damage >= 640:
            pygame.quit()
            return True

        trial = pygame.mouse.get_pos()
        p2_rect = pygame.Rect((pos2[0] - p.scroll[0], pos2[1] - p.scroll[1]), (42, 60))

        if p2_rect.collidepoint(trial[0], trial[1]):
            aim = True

        mouse_down = pygame.mouse.get_pressed()
        if mouse_down[0] == 1 and aim:
            if 8 <= damage_counter < 32:
                damage += 8
            if 32 <= damage_counter < 64:
                damage += 64
            if 64 <= damage_counter < 128:
                damage += 320
            if 128 <= damage_counter:
                damage += 640
            damage_counter = 0

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

        if aim:
            damage_counter += 1
        else:
            damage_counter = 0
        p.health = 640 - pos2[2]
        p.move(blocks)
        win.fill((0, 0, 0))
        p.appear(win)
        win.blit(p2, (pos2[0] - p.scroll[0], pos2[1] - p.scroll[1]))
        blocksFull = map_printer(win, size, blocks, blocksFull, p)
        pygame.draw.rect(win, (255, 20, 147), (0, 0, p.health * 2, 20))
        pygame.draw.rect(win, (0, 255, 0), (0, 20, damage_counter * 10, 20))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
