import pygame
import math
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

# подготовка к запуску. Использовал материал из https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie
user32 = ctypes.windll.user32
sizescreen = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
print(sizescreen)

FPS = 30

backgraund = BLACK

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(sizescreen, pygame.FULLSCREEN)
pygame.display.set_caption("FirstGame")
clock = pygame.time.Clock()
# Конец: Использовал материал из https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie

# пораметры игры
countGuns = 2
screenShot = 1  # 1000
chanceSpawnStar = 1000  # 1000
chanceSpawnEnemy = 10  # 10
chanceSpawnBoost = 1000  # 1000
speedOfUpChanceSpawnEnemy = 10000  # 10000
countCoinsToHealth = 10000  # 10000
asteroidHealthMultiplier = 1000  # gameLength/1000
gameLength = 10000  # 10000
coins = 0

# создаю корабь
ship = soldier("ship.png", size=(100, 100), position=(int(sizescreen[0] / 2), sizescreen[1] - 200), speed=10)
ship.sethealth(3)
ship.setGan(1, 1)
# создаю кнопки сверху слева
end = button("Выход", (-1, -1), 30, WHITE, BLACK)
health = button(str(ship.health), (-1, end.sizeY), 40, WHITE, BLACK)
gameDuration = button("gameDuration", (-1, end.sizeY + health.sizeY), 40, WHITE, BLACK)
tabletCoins = button("0", (-1, end.sizeY + health.sizeY + gameDuration.sizeY), 40, WHITE, BLACK)
gameOverButton = button("GAMEOVER", (sizescreen[0] // 2, sizescreen[1] // 2), 100, WHITE, BLACK)
gameOverButton.x = sizescreen[0] // 2 - gameOverButton.sizeX // 2
gameOverButton.y = sizescreen[1] // 2 - gameOverButton.sizeY // 2
gameOverButton.change_text("VIKTORY!", WHITE, BLACK)
stars = []

# генерация звёзд
for i in range(random.randint(int(sizescreen[0] * sizescreen[1] / chanceSpawnStar / 2),
                              int(sizescreen[0] * sizescreen[1] / chanceSpawnStar))):
    stars.append(spawnStar(position=(random.randint(0, sizescreen[0]), random.randint(0, sizescreen[1])),
                           angle=random.randint(-3, 3)))

firstBoost = objectI("box.png", size=(50, 50), position=(random.randint(0, sizescreen[0]), -50), speed=5,
                     angle=random.randint(0, 180))

# массивы с обьектами
buttons = [health, gameDuration, end, tabletCoins]
Enemys = []
bullits = []
Boosts = [firstBoost]

print("start")
# Цикл игры
gameOver = False
running = True

# основной цикл
while running:

    # отслеживание событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            off()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                end.click(pygame.mouse.get_pos(), off)
        if event.type == pygame.KEYDOWN and not gameOver:
            if event.key == pygame.K_SPACE:
                bullits += ship.fire()

    # проверка на конец игры
    if not gameOver and screenShot < speedOfUpChanceSpawnEnemy:
        # генерация коробок с улучшениями
        if random.randint(0, int(chanceSpawnBoost)) <= 0:
            b = objectI("box.png", size=(50, 50), position=(random.randint(0, sizescreen[0]), -50), speed=5,
                        angle=random.randint(0, 180))
            Boosts.append(b)

        # генерация метиоритов
        if random.randint(0, int(chanceSpawnEnemy)) <= 0:
            pos = random.randint(25, 100)
            e = soldier("asteroid.png", size=(pos, pos), position=(random.randint(0, sizescreen[0]), -50), speed=5,
                        angle=random.randint(0, 180))
            if screenShot >= asteroidHealthMultiplier:
                e.sethealth((pos / 25) * (screenShot / asteroidHealthMultiplier) // 1)
            else:
                e.sethealth((pos / 25) // 1)
            Enemys.append(e)

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
        # движение обьектов
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

        # отслеживание столкновений
        for i in range(len(Enemys)):
            if i < len(Enemys) and Enemys[i].rect.colliderect(ship.rect):
                ship.health -= 1
                if ship.health <= 0:
                    gameOverButton.change_text("GAMEOVER", WHITE, BLACK)
                    gameOver = True
                del Enemys[i]
            for j in range(len(bullits)):
                if j < len(bullits) and i < len(Enemys) and Enemys[i].rect.colliderect(bullits[j].rect):
                    Enemys[i].health -= bullits[j].damage
                    del bullits[j]
                    if Enemys[i].health <= 0:
                        coins += Enemys[i].sizeY
                        del Enemys[i]
                        if coins >= countCoinsToHealth:
                            coins -= countCoinsToHealth
                            ship.health += 1

        for i in range(len(Boosts)):
            if i < len(Boosts) and Boosts[i].rect.colliderect(ship.rect):
                if random.randint(0, 1):
                    ship.setGan(1, ship.gunLvl + 1)
                else:
                    ship.setGan(random.choice([x for x in range(1, countGuns + 1) if x != ship.gunTypeNomber]), ship.gunLvl)
                del Boosts[i]

        for i in range(len(bullits)):
            if i < len(bullits) and bullits[i].OutSideScrin(sizescreen, slog=50):
                del bullits[i]

        # Посткадровые изменения
        screenShot += 1
        chanceSpawnEnemy = speedOfUpChanceSpawnEnemy / screenShot

        gameDuration.change_text(str(screenShot) + "/" + str(gameLength), WHITE, BLACK)
        tabletCoins.change_text(str(coins) + "/" + str(countCoinsToHealth), WHITE, BLACK)
        health.change_text(ship.health, WHITE, BLACK)

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

    # проверка на конец игры
    if gameOver or screenShot >= gameLength:
        gameOverButton.output(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()