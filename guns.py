import unit
import bullit

class gun():
    def __init__(self, type=1, lvl=1):
        self.pointsToFire = []
        if type==1:
            self.gunType = self.pistol(lvl)

    def fire(self):
        b = bullit.bullit(self.imgBullit, position=(self.x + self.gunX, self.y + self.gunY), size=self.gunSize,
                          speed=self.gunSpeed, angle=self.gunAngle)
        b.setDamage(self.damage)
        return b

    def pistol(self, lvl):
        self.imgBullit = "3.png"
        self.damage = 1
        if lvl <= 1:
            self.gunX = 0
            self.gunY = 0
            self.gunAngle = 270
            self.pointsToFire = [(self.gunX, self.gunY, self.gunAngle)]
            self.gunSize = (10, 2)
            self.gunSpeed = 10
        elif lvl == 2:
            self.gunX = 0
            self.gunY = 0
            self.gunAngle = 270
            self.pointsToFire = [(self.gunX+8, self.gunY, self.gunAngle),(self.gunX-8, self.gunY, self.gunAngle)]
            self.gunSize = (10, 2)
            self.gunSpeed = 10
        elif lvl == 3:
            self.gunX = 0
            self.gunY = 0
            self.gunAngle = 270
            self.pointsToFire = [(self.gunX + 10, self.gunY, self.gunAngle), (self.gunX, self.gunY, self.gunAngle), (self.gunX - 10, self.gunY, self.gunAngle)]
            self.gunSize = (10, 2)
            self.gunSpeed = 10
        elif lvl ==4:
            self.gunX = 0
            self.gunY = 0
            self.gunAngle = 270
            self.pointsToFire = [(self.gunX+8, self.gunY, self.gunAngle),(self.gunX-8, self.gunY, self.gunAngle),(self.gunX-8, self.gunY, self.gunAngl-3),(self.gunX-8, self.gunY, self.gunAngle+3)]
            self.gunSize = (10, 2)
            self.gunSpeed = 10
        elif lvl ==5:
            self.gunX = 0
            self.gunY = 0
            self.gunAngle = 270
            self.pointsToFire = [(self.gunX + 10, self.gunY, self.gunAngle), (self.gunX, self.gunY, self.gunAngle), (self.gunX - 10, self.gunY, self.gunAngle),(self.gunX-8, self.gunY, self.gunAngl-3),(self.gunX-8, self.gunY, self.gunAngle+3)]
            self.gunSize = (10, 2)
            self.gunSpeed = 10
        else:
            self.gunX = 0
            self.gunY = 0
            self.gunAngle = 270
            self.pointsToFire = [(self.gunX + 10, self.gunY, self.gunAngle), (self.gunX, self.gunY, self.gunAngle), (self.gunX - 10, self.gunY, self.gunAngle),(self.gunX-8, self.gunY, self.gunAngl-2),(self.gunX-8, self.gunY, self.gunAngle+2),(self.gunX-12, self.gunY+3, self.gunAngl-2),(self.gunX+12, self.gunY+3, self.gunAngle+2)]
            self.gunSize = (10, 2)
            self.gunSpeed = 10
