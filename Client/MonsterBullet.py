from pico2d import*


name = "MonsterBullet"

class MonsterBullet:

    image = None

    def __init__(self, x, y, dir):

        self.x, self.y = x, y - 20
        self.dir = dir
        if MonsterBullet.image == None:
            self.image = load_image('MobBullet.png')


    def update(self,frame_time):
        if self.dir == 1:
            self.x = self.x + 10
        elif self.dir == -1:
            self.x = self.x - 10

    def draw(self):
        self.image.draw(self.x, self.y)

    def SetPos(self, x, y):
        self.x, self.y = x, y

    def GetPosX(self):
        return self.x

    def GetPosY(self):
        return self.y

    def get_bb(self):
        return self.x - 10, self.y, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
