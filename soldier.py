import unit
import bullit


class soldier(unit.unit):
    def setGan(self, type=1, lvl=1):
        self.pointsToFire = []
        self.gunLvl = lvl
        self.gunTypeNomber = type
        if self.gunTypeNomber == 1:
            self.gunType = self.pistol(self.gunLvl)
        if self.gunTypeNomber == 2:
            self.gunType = self.bigGun(self.gunLvl)

    def fire(self):
        c = []
        for i in self.pointsToFire:
            b = bullit.bullit(self.imgBullit, position=(self.x + i[0], self.y + i[1]), size=self.gunSize,
                              speed=self.gunSpeed, angle=i[2])
            b.setDamage(self.damage)
            c.append(b)
        return c

    def pistol(self, lvl):
        self.imgBullit = "3.png"
        self.damage = 1
        self.gunX = 4
        self.gunY = -15
        self.gunAngle = 270
        self.gunSize = (10, 2)
        self.gunSpeed = 20
        if lvl <= 1:
            self.pointsToFire = [(self.gunX, self.gunY, self.gunAngle)]
        elif lvl == 2:
            self.pointsToFire = [(self.gunX + 16, self.gunY, self.gunAngle), (self.gunX - 16, self.gunY, self.gunAngle)]
        elif lvl == 3:
            self.pointsToFire = [(self.gunX + 16, self.gunY, self.gunAngle), (self.gunX, self.gunY, self.gunAngle),
                                 (self.gunX - 16, self.gunY, self.gunAngle)]
        elif lvl == 4:
            self.pointsToFire = [(self.gunX + 16, self.gunY, self.gunAngle), (self.gunX - 16, self.gunY, self.gunAngle),
                                 (self.gunX + 16, self.gunY, self.gunAngle - 6),
                                 (self.gunX - 16, self.gunY, self.gunAngle + 9)]
        elif lvl == 5:
            self.pointsToFire = [(self.gunX, self.gunY, self.gunAngle), (self.gunX + 16, self.gunY, self.gunAngle - 6),
                                 (self.gunX + 16, self.gunY, self.gunAngle - 12),
                                 (self.gunX - 16, self.gunY, self.gunAngle + 9),
                                 (self.gunX - 16, self.gunY, self.gunAngle + 15)]
        else:
            self.pointsToFire = [(self.gunX + 16, self.gunY, self.gunAngle), (self.gunX, self.gunY, self.gunAngle),
                                 (self.gunX - 16, self.gunY, self.gunAngle),
                                 (self.gunX + 16, self.gunY, self.gunAngle - 6),
                                 (self.gunX + 16, self.gunY, self.gunAngle - 12),
                                 (self.gunX - 16, self.gunY, self.gunAngle + 9),
                                 (self.gunX - 16, self.gunY, self.gunAngle + 15)]

    def bigGun(self, lvl):
        self.imgBullit = "3.png"
        self.gunX = 4
        self.gunY = -15
        self.gunAngle = 270
        self.gunSpeed = 12
        if lvl <= 2:
            self.gunSize = (20, 4)
            self.damage = 2
            self.pointsToFire = [(self.gunX, self.gunY, self.gunAngle)]
        elif lvl == 3:
            self.gunSize = (20, 4)
            self.damage = 2
            self.pointsToFire = [(self.gunX + 16, self.gunY, self.gunAngle), (self.gunX - 16, self.gunY, self.gunAngle)]
        elif lvl == 4:
            self.gunSize = (20, 4)
            self.damage = 3
            self.pointsToFire = [(self.gunX + 16, self.gunY, self.gunAngle), (self.gunX - 16, self.gunY, self.gunAngle)]
        elif lvl == 5:
            self.gunSize = (30, 6)
            self.damage = 5
            self.pointsToFire = [(self.gunX + 16, self.gunY, self.gunAngle), (self.gunX - 16, self.gunY, self.gunAngle)]
        else:
            self.gunSize = (30, 6)
            self.damage = 5
            self.pointsToFire = [(self.gunX, self.gunY, self.gunAngle), (self.gunX + 16, self.gunY, self.gunAngle - 6),
                                 (self.gunX - 16, self.gunY, self.gunAngle + 9)]
