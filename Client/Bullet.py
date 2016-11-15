from pico2d import*


name = "Bullet"

class Bullet:

    image = None

    def __init__(self, x, y, dir):

        self.x, self.y = x, y- 20
        self.dir = dir
        if Bullet.image == None:
            Bullet.image = load_image('Bullet.png')


    def update(self):
        if self.dir == 1:
            self.x = self.x + 20
        elif self.dir == -1:
            self.x = self.x - 20

    def draw(self):
        self.image.draw(self.x, self.y)

    def SetPos(self, x, y):
        self.x, self.y = x, y
    def GetPosX(self):
        return self.x
    def GetPosY(self):
        return self.y