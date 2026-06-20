import pygame, pyautogui
WIDTH, HEIGHT= pyautogui.size()
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket")
space=pygame.image.load("pictures/space.png")
moon=pygame.transform.scale(pygame.image.load("pictures/onthemoon.jpg"), (WIDTH, HEIGHT))
ali=pygame.transform.scale(pygame.image.load("pictures/alien.png"), (300, 300))
bot=pygame.transform.scale(pygame.image.load("pictures/robot.png"), (300, 300))
ladder=pygame.transform.scale(pygame.image.load("pictures\ladder.png"), (20, HEIGHT))
border=pygame.Rect(WIDTH//2-10, 0, 20, HEIGHT)
def draw(cr, rc):
    screen.blit(moon, (0,0))
    screen.blit(ali, (cr.x-40, cr.y))
    screen.blit(bot, (rc.x-40, rc.y-70))
    screen.blit(ladder, (border.x, border.y))

def handlemovement(cr, rc, keys):
    if keys[pygame.K_a] and cr.x>0:
        cr.x-=10
    if keys[pygame.K_d] and cr.x+cr.width<border.x:
        cr.x+=10
    if keys[pygame.K_w] and cr.y>0:
        cr.y-=10
    if keys[pygame.K_s] and cr.y+cr.height<HEIGHT:
        cr.y+=10
    if keys[pygame.K_LEFT] and rc.x>border.x+border.width:
        rc.x-=10
    if keys[pygame.K_RIGHT] and rc.x+rc.width<WIDTH:
        rc.x+=10
    if keys[pygame.K_UP] and rc.y>0:
        rc.y-=10
    if keys[pygame.K_DOWN] and rc.y+rc.height<HEIGHT:
        rc.y+=10

def main():
    cr=pygame.Rect(300, HEIGHT//2, 200, 300)
    rc=pygame.Rect(WIDTH-300, HEIGHT//2, 300, 300)
    while True:
        draw(cr, rc)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_LSHIFT:
                    b=pygame.Rect(cr.x, cr.y, 80, 30)
                    cbullets.append(b)
                if i.key==pygame.K_RSHIFT:
                    g=pygame.Rect(rc.x, rc.y, 80, 30)
                    rbullets.append(g)
        keys=pygame.key.get_pressed()
        handlemovement(cr, rc, keys)
        pygame.display.update()
main()