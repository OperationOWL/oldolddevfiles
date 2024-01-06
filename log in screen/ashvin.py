import pygame

pygame.init()
dis = (500,250)
win = pygame.display.set_mode(dis)
red = (255,100,100)
blue = (120,120,255)
black = (0,0,0)

def feedback():
    win.fill(blue)
    font = pygame.font.Font("Roboto-ThinItalic.ttf", 36)
    text = font.render('enter feedback', True, black, blue)
    textRect = text.get_rect()
    textRect.center = (dis[0] // 2, (dis[1]-200))
    win.blit(text, textRect)

    for i in range(1,11):
        j = i*50 - 25
        pygame.draw.rect(win, red, pygame.Rect(i*50-45, dis[1]//2-30, 40, 60)) 
        text = font.render(f'{i}', True, black)
        textRect = text.get_rect()
        textRect.center = (j, (dis[1]//2))
        win.blit(text, textRect)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                pos = pygame.mouse.get_pos()
                for i in range(1,11):
                    j = i*50 - 25
                    if pos[0] in range(j-20, j+20) and pos[1] in range(dis[1]//2-29, dis[1]//2+29):
                        print(i)
        feedback()
        pygame.display.update()

if __name__ == "__main__":
    main()