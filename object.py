import pygame
import math


class objectI:
    def __init__(self, imgPath, position=(100, 100), size=(100, 100), speed=2, angle=0):
        """
        :param imgPath: Путь к скину /str/
        :param position: Позиция в пикселях /(int:x, int:y)/
        :param size: Размер в пикселях /(int:sizeX, int:sizeY)/
        :param speed: Скорость с которй будет двигаться обьекст /int/
        :param angle: Угол на который повернуть скин в градусах /int/
        """
        self.imgPath = imgPath
        self.speed = speed
        self.position = position
        self.positionRD = list(map(lambda x, y: x + y, position, size))
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.sizeX = size[0]
        self.sizeY = size[1]
        self.image = pygame.transform.scale(pygame.image.load(imgPath), size)
        self.angle = angle
        self.reDraw()

    def reDraw(self):
        """
        обновляет отрисовку обьект
        """
        self.rotImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(bottomright=(self.sizeX, self.sizeY))
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def output(self, screen):
        """
        :param screen: Экран на котором выводить обьект /pygame.display/
        """
        screen.blit(self.rotImage, self.rect)

    def go(self, angle):
        """
        :param angle: Угол в который будет двигаться обьект в градусах /int/
        """
        angle = math.radians(angle)

        y = math.sin(angle) * self.speed

        if angle > math.pi:
            x = math.cos(angle - math.pi) * self.speed
        else:
            x = math.cos(angle) * self.speed

        if x % 1 >= 0.5:
            x = int(x) + 1
        else:
            x = int(x)

        if y % 1 >= 0.5:
            y = int(y) + 1
        else:
            y = int(y)

        self.x += x
        self.y += y
        self.position = (self.x, self.y)
        self.rect.centerx += x
        self.rect.centery += y

    def goTo(self, ToX, ToY):
        """
        :param ToX: X на который переместиться
        :param ToY: Y на который переместиться
        """
        self.x = ToX
        self.y = ToY
        self.position = (self.x, self.y)
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def OutSideScrin(self, size, slog=0):
        """
        :param size: Длина и ширина прямоугольника с x и y в верхним углу экрана /(int:sizeX, int:sizeY)/
        :param slog: Расширение рамки на k пикселей со всех сторон /int:k/
        """
        if self.x < (-self.sizeX / 2) - slog or self.x > size[0] + (self.sizeX / 2) + slog or self.y < (-self.sizeY / 2) - slog or self.y > size[1] + (self.sizeY / 2) + slog:
            return True
        return False

    def setAlgleTo(self, i):
        """
        :param i: обьект с .x и .y
        """
        x = self.x - i.x
        y = self.y - i.y

        r = math.degrees(math.atan2(x, y))
        self.angle = r
        self.reDraw()
