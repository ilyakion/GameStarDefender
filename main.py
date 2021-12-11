import pygame
import random
from Functions import *
from object import *
from button import *
from unit import *
from colors import *
from soldier import *


def off():
    global running
    running = False
    return


user32 = ctypes.windll.user32
sizescreen = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
print(sizescreen)

WIDTH = 360
HEIGHT = 480
FPS = 30

backgraund = BLACK

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(sizescreen, pygame.FULLSCREEN)
pygame.display.set_caption("FirstGame")
clock = pygame.time.Clock()

countGuns = 2
screenShot = 1
chanceSpawnStar = 10
chanceSpawnEnemy = 10
chanceSpawnBoost = 10
speedOfUpChanceSpawnEnemy = 10000  # 10000
gameLength = 10000

ship = soldier("1.png", size=(100, 100), position=(int(sizescreen[0] / 2), sizescreen[1] - 200), speed=10)
ship.sethealth(3)
ship.setGan(1, 1)
end = button("Выход", (-1, -1), 30, WHITE, BLACK)
health = button(str(ship.health), (-1, end.sizeY), 40, WHITE, BLACK)
coins = button(str(screenShot), (-1, end.sizeY+health.sizeY), 40, WHITE, BLACK)
gameOverButton = button("GAMEOVER", (sizescreen[0]//2, sizescreen[1]//2), 100, WHITE, BLACK)
gameOverButton.x = sizescreen[0]//2 - gameOverButton.sizeX//2
gameOverButton.y = sizescreen[1]//2 - gameOverButton.sizeY//2
gameOverButton.change_text("VIKTORY!", WHITE, BLACK)
stars = []

for i in range(random.randint(int(sizescreen[0] * sizescreen[1] / chanceSpawnStar / 2),
                              int(sizescreen[0] * sizescreen[1] / chanceSpawnStar))):
    stars.append(spawnStar(position=(random.randint(0, sizescreen[0]), random.randint(0, sizescreen[1])),
                           angle=random.randint(-3, 3)))

firstBoost = objectI("5.png", size=(50, 50), position=(random.randint(0, sizescreen[0]), -50), speed=5, angle=random.randint(0, 180))

buttons = [health, coins, end]
Enemys = []
bullits = []
Boosts = [firstBoost]

print("start")
# Цикл игры
gameOver = False
running = True
while running:

    # отслеживание событий
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            off()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                end.click(pygame.mouse.get_pos(), off)
        if event.type == pygame.KEYDOWN and not gameOver:
            if event.key == pygame.K_SPACE:
                bullits += ship.fire()

    if not gameOver and screenShot < speedOfUpChanceSpawnEnemy:
        if random.randint(0, int(chanceSpawnBoost)) <= 0:
            b = objectI("5.png", size=(50, 50), position=(random.randint(0, sizescreen[0]), -50), speed=5, angle=random.randint(0, 180))
            Boosts.append(b)

        if random.randint(0, int(chanceSpawnEnemy)) <= 0:
            pos = random.randint(25, 100)
            e = soldier("4.png", size=(pos, pos), position=(random.randint(0, sizescreen[0]), -50), speed=5,
                        angle=random.randint(0, 180))
            e.sethealth(pos//25)
            Enemys.append(e)

        chanceSpawnEnemy = speedOfUpChanceSpawnEnemy/screenShot

        screenShot += 1
        coins.change_text(screenShot, WHITE, BLACK)

        # Управление стрелачками
        if pygame.key.get_pressed()[pygame.K_LEFT] and ship.x > 0:
            ship.go(180)
        if pygame.key.get_pressed()[pygame.K_RIGHT] and ship.x < sizescreen[0]:
            ship.go(0)
        if pygame.key.get_pressed()[pygame.K_UP] and ship.y > 0:
            ship.go(270)
        if pygame.key.get_pressed()[pygame.K_DOWN] and ship.y < sizescreen[1]:
            ship.go(90)

        # процесс игры
        for i in range(len(Boosts)):
            Boosts[i].go(90)
            if i < len(Boosts) and Boosts[i].OutSideScrin(sizescreen, slog=50):
                del Boosts[i]
                break

        for i in stars:
            i.go(90)
            if i.y > sizescreen[1]:
                i.goTo(i.x, -15)

        for i in range(len(Enemys)):
            Enemys[i].go(90)
            if i < len(Enemys) and Enemys[i].OutSideScrin(sizescreen, slog=50):
                del Enemys[i]
                break

        for i in bullits:
            i.fly()

        for i in range(len(Enemys)):
            if i < len(Enemys) and Enemys[i].rect.colliderect(ship.rect):
                ship.health -= 1
                if ship.health <= 0:
                    gameOverButton.change_text("GAMEOVER", WHITE, BLACK)
                    gameOver = True
                health.change_text(ship.health, WHITE, BLACK)
                del Enemys[i]
            for j in range(len(bullits)):
                if j < len(bullits) and i < len(Enemys) and Enemys[i].rect.colliderect(bullits[j].rect):
                    Enemys[i].health -= bullits[j].damage
                    del bullits[j]
                    if Enemys[i].health <= 0:
                        del Enemys[i]

        for i in range(len(Boosts)):
            if i < len(Boosts) and Boosts[i].rect.colliderect(ship.rect):
                if random.randint(0,1):
                    ship.setGan(1, ship.gunLvl+1)
                else:
                    ship.setGan(random.randint(1,countGuns), ship.gunLvl)
                del Boosts[i]

        for i in range(len(bullits)):
            if i < len(bullits) and bullits[i].OutSideScrin(sizescreen, slog=50):
                del bullits[i]

    # Рендеринг
    screen.fill(backgraund)

    for i in stars:
        i.output(screen)

    for i in bullits:
        i.output(screen)

    ship.output(screen)

    for i in Enemys:
        i.output(screen)

    for i in Boosts:
        i.output(screen)

    for i in buttons:
        i.output(screen)

    if gameOver or screenShot >= gameLength:
        gameOverButton.output(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
