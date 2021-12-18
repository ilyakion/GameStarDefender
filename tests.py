import unittest
from Functions import *
from object import *
from soldier import *


class Test(unittest.TestCase):
    def test_OutSideScrin(self):
        a = objectI("ship.png", position=(500, 500))
        self.assertEqual(a.OutSideScrin([1000, 1000]), False)
        a = objectI("ship.png", position=(-100, -100))
        self.assertEqual(a.OutSideScrin([1000,1000]), True)
        a = objectI("ship.png", position=(1100, 1100))
        self.assertEqual(a.OutSideScrin([1000, 1000]), True)

    def test_fire(self):
        a = soldier("ship.png")
        a.setGan()
        self.assertEqual(len(a.fire()), 1)
        self.assertEqual(type(a.fire()), list)
        a = soldier("ship.png")
        a.setGan(1,2)
        self.assertEqual(len(a.fire()), 2)

    def test_spawnStar(self):
        self.assertEqual(type(spawnStar([100, 100], 0)), objectI)
        self.assertEqual(spawnStar([100, 100], 0).position, [100, 100])

    def test_bullitFly(self):
        speed = 10
        a = bullit.bullit("bul.png", position=(0, 0), speed=speed)
        a.fly()
        self.assertEqual(a.position, (speed, 0))

    def test_objectGoTO(self):
        a = objectI("bul.png", position=(0, 0))
        a.goTo(10,10)
        self.assertEqual(a.position, (10, 10))

if __name__ == "__main__":
    unittest.main()