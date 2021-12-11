import unit

class bullit(unit.unit):
    def setDamage(self, damage):
        self.damage = damage

    def setAngle(self, angle):
        self.angle = angle

    def collision(self, obj, funct):
        if self.rect.colliderect(obj.rect):
            for i in funct:
                i()

    def fly(self):
        self.go(self.angle)