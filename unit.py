import pygame
import object
import math

class unit(object.objectI):
    """
    objectI с очками жизни
    """
    def sethealth(self, health=100):
        """
        :param health: Количество очков жизнин /int/
        """
        self.health = health