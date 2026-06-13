import pygame, pyautogui
WIDTH, HEIGHT= pyautogui.size()
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket")
space=pygame.image.load("pictures/space.png")
moon=pygame.transform.scale(pygame.image.load("pictures/onthemoon.jpg"), (WIDTH, HEIGHT))
ali=pygame.transform.scale(pygame.image.load("pictures/alien.png"), (300, 300))
bot=pygame.transform.scale(pygame.image.load("pictures/robot.png"), (300, 300))

def draw(cr, rc):
    screen.blit(moon, (0,0))
    screen.blit(ali, (cr.x, cr.y))
    screen.blit(bot, (rc.x, rc.y))

def handlemovement(cr, rc, keys):
    if keys[pygame.k_a]:
        cr.x-=10

def main():
    cr=pygame.Rect(300, HEIGHT//2, 300, 300)
    rc=pygame.Rect(WIDTH-300, HEIGHT//2, 300, 300)
    while True:
        draw(cr, rc)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
        keys=pygame.key.getpressed()
        handlemovement(cr, rc, keys)
        pygame.display.update()
main()