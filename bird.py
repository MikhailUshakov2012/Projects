import arcade
from animate import Animate
from data import SCREEN_HEIGHT, SCREEN_WIDTH, GRAVITI


class Bird(Animate):
    def __init__(self):
        super(Bird, self).__init__("./images/bird/redbird-midflap.png", 2)
        self.textures.extend([
            arcade.load_texture("./images/bird/redbird-upflap.png"),
            arcade.load_texture("./images/bird/redbird-downflap.png")
        ])
        self.setup()
        self.stop = False

    def setup(self):
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2

    def on_key_press(self, symbol: int):
        if symbol == arcade.key.UP:
            self.change_y = 10

    def update(self, delta_time):
        super(Bird, self).update()
        self.center_y += self.change_y
        self.change_y -= GRAVITI * delta_time
        self.angle = self.change_y * 2
