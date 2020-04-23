import pygame
import random
import os

pygame.init()
szer=600
wys=600
screen = pygame.display.set_mode((szer,wys))
clock = pygame.time.Clock()
dt = clock.tick(30)
def napisz(tekst, x, y, rozmiar):
    cz=pygame.font.SysFont("Arial", rozmiar)
    rend=cz.render(tekst,1,(255, 83, 6))
    screen.blit(rend, (x,y))

class Gracz():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kolor = (255, 255, 255)
        self.wys = 20
        self.szer = 20
        self.ksztalt = pygame.Rect(self.x, self.y, self.szer, self.wys)
    def rysuj(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt, 0)
    def ruch(self, vx, vy):
        if self.x + vx > 0 and self.x + vx < szer-self.szer:
            self.x += vx
        if self.y + vy > 0 and self.y + vy < wys - self.wys:
            self.y +=vy
        self.ksztalt = pygame.Rect(self.x, self.y, self.szer, self.wys)

class Biedronki():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wys = 10
        self.szer = 10
        self.vx = random.randint(-2, 2)
        self.vy = random.randint(-2, 2)
        self.kolor = (255,0,0)
        self.ksztalt = pygame.Rect(self.x, self.y, self.szer, self.wys)
    def rysuj(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt, 0)
    def ruch(self):
        if self.x + self.vx > 0 and self.x + self.vx < szer-self.szer:
            self.x += self.vx
        else:
            self.vx = -self.vx
        if self.y + self.vy > 0 and self.y + self.vy < wys - self.wys:
            self.y +=self.vy
        else:
            self.vy = -self.vy
        self.ksztalt = pygame.Rect(self.x, self.y, self.szer, self.wys)
    def kolizja(self, player):
        if self.ksztalt.colliderect(player):
            return True
        else:
            return False


ile_biedronek = 12
bierdronki = []
for i in range(ile_biedronek):
    bierdronki.append(Biedronki(random.randint(0,500), random.randint(0,500)))

pokaz = "gra"
gracz = Gracz(250, 250)
rx = 0
ry = 0
punkty = 0

while True:
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ry = -1
            if event.key == pygame.K_DOWN:
                ry = 1
            if event.key == pygame.K_LEFT:
                rx = -1
            if event.key == pygame.K_RIGHT:
                rx = 1
            if event.key == pygame.K_SPACE:
                if pokaz != "gra":
                    for i in range(ile_biedronek):
                        bierdronki.pop()
                    for i in range(ile_biedronek):
                        bierdronki.append(Biedronki(random.randint(0, 500), random.randint(0, 500)))
                    gracz = Gracz(250, 250)
                    pokaz = "gra"
                    punkty = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ry = 0
            if event.key == pygame.K_DOWN:
                ry = 0
            if event.key == pygame.K_LEFT:
                rx = 0
            if event.key == pygame.K_RIGHT:
                rx = 0

    screen.fill((0, 0, 0))
    if pokaz == "gra":
        gracz.ruch(rx, ry)
        gracz.rysuj()
        punkty += 1
        for b in bierdronki:
            b.rysuj()
            b.ruch()
            if b.kolizja(gracz.ksztalt):
                pokaz = "koniec"
    if pokaz == "koniec":
        napisz("PRZEGRALES", 200, 200, 20)
        napisz(str(punkty), 200, 250, 20)
    pygame.display.update()