import pygame
import math


class objectI:
    def __init__(self, imgPath, position=(100, 100), size=(100, 100), speed=2, angle=0):
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
        self.rotImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(bottomright=(self.sizeX, self.sizeY))
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def output(self, screen):
        screen.blit(self.rotImage, self.rect)

    def go(self, angle):

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
        self.x = ToX
        self.y = ToY
        self.position = (self.x, self.y)
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def delit(self):
        del self

    def OutSideScrin(self, size, slog=0):
        """
        print(self.x < (-self.sizeX / 2) - slog)
        print(self.x > size[0] + (self.sizeX / 2) + slog)
        print(self.y < (-self.sizeY / 2) - slog)
        print(self.y > size[1] + (self.sizeY / 2) + slog)
        """
        if self.x < (-self.sizeX / 2) - slog or self.x > size[0] + (self.sizeX / 2) + slog or self.y < (-self.sizeY / 2) - slog or self.y > size[1] + (self.sizeY / 2) + slog:
            return True
        return False

    def setAlgleTo(self, i):
        x = self.x - i.x
        y = self.y - i.y

        r = math.degrees(math.atan2(x, y))
        self.angle = r
        self.reDraw()
