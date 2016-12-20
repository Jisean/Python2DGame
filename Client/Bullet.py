from pico2d import*


name = "Bullet"

class Bullet:

    image = None

    def __init__(self, x, y, dir, updown):

        self.x, self.y = x, y- 20
        self.updown = updown
        self.dir = dir
        if Bullet.image == None:
            if self.updown == 0:
                if dir == 1 :
                    self.image = load_image('Bullet.png')
                elif dir == -1:
                    self.image = load_image('Bullet2.png')
            elif self.updown == 1:
                self.image = load_image('Bullet3.png')


    def update(self,frame_time):
        if self.updown == 0:
            if self.dir == 1:
                self.x = self.x + 20
            elif self.dir == -1:
                self.x = self.x - 20
        elif self.updown == 1:
            self.y = self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)

    def SetPos(self, x, y):
        self.x, self.y = x, y

    def GetPosX(self):
        return self.x

    def GetPosY(self):
        return self.y

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
