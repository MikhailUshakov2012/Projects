import arcade
from data import SCREEN_HEIGHT, SCREEN_WIDTH


class Pipe(arcade.Sprite):
    def __init__(self, flipped = False):
        super(Pipe, self).__init__("./images/pipe.png", 0.45, flipped_vertically = flipped)
        self.setup()
        self.change_x = 7
        self.stop = False

    def setup(self):
        pass

    def update(self):
        self.center_x -= self.change_x
        self.stop = False
        if self.right < 0:
            self.left = SCREEN_WIDTH
            self.stop = True
