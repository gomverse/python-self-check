# 실습용
import pygame
from pygame.locals import *


class Bullet:

    img_src = None

    def __init__(self, x, y):

        if Bullet.img_src == None:
            Bullet.img_src = pygame.image.load(
                "present-gift-box-reward-full.png"
            ).convert_alpha()
            w, h = Bullet.img_src.get_size()
            Bullet.img_src = pygame.transform.scale(Bullet.img_src, (w // 10, h // 10))
        self.img = Bullet.img_src
        self.vx = 10.0
        self.vy = 0.0
        self.x = x
        self.y = y
        self.angle = 0.0
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.angle -= 20.0
        self.img = pygame.transform.rotate(Bullet.img_src, self.angle)
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.img, self.rect)


class Santa:

    img_src_run = None
    img_src_dead = None

    def __init__(self):
        if Santa.img_src == None:
            Santa.img_src = pygame.image.load()


pygame.init()

screen = pygame.display.set_mode((1024, 768))  # 윈도우 크기
clock = pygame.time.Clock()

bullet_group = []  # 총알의 그룹

scorefont = pygame.font.SysFont("system", 48)
ground_y = 512  # 바닥 위치

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
            bullet_group.append(Bullet(240, 400))

    """업데이트"""
    screen.fill((255, 255, 255))
    pygame.draw.rect(
        screen, color=(128, 128, 128), rect=pygame.Rect(0, 64 * 8, 1024, 64 * 4)
    )

    """화면에 그리기"""

    # pygame.draw.rect(screen, color=(128, 128, 128), rect=pygame.Rect(0, 64*8, 1024, 64*4))

    for b in bullet_group.copy():
        b.update()
        b.draw(screen)
        if b.rect.left > 1024:
            bullet_group.remove(b)

    # 디버깅 용도
    scoretext = scorefont.render(f"Num bullets = {len(bullet_group)}", 1, (0, 0, 0))
    screen.blit(scoretext, (700, 10))

    pygame.display.flip()
    clock.tick(30)


pygame.quit()
