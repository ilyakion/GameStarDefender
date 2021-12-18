import random
from object import *
import ctypes

user32 = ctypes.windll.user32
sizescreen = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

def spawnStar(position,angle,size=(0,30)):
    """
    :param position: Позиция звезды /(int:x, int:y)/
    :param angle: Угол отклонения /int/
    :param size: Размер в пикселях /(int:sizeX, int:sizeY)/
    :return: objectI
    """
    coef = 3
    if random.randint(0,10)>8:
        s = random.randint(int(size[1]/coef), size[1])
    else:
        s = random.randint(size[0], int(size[1]/coef))
    return objectI("star.png", size=(s, s),
                             position=position,
                             angle=angle,
                             speed=random.randint(1,int(s/7)+1)
                             )