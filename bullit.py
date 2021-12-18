import unit

class bullit(unit.unit):
    def setDamage(self, damage):
        """
        :param damage: Количество урона который будет наносить пуля /int/
        """
        self.damage = damage

    def setAngle(self, angle):
        """
        :param angle: Угол полёта пули /int/
        """
        self.angle = angle

    def fly(self):
        self.go(self.angle)