import arcade


class Animate(arcade.Sprite):
    def __init__(self, sprite, scale):
        super(Animate, self).__init__(sprite, scale)
        self.i = 0
        self.timer = 0

    def update(self):
        self.update_animation()

    def update_animation(self, delta_time: float = 1 / 60):
        self.timer += delta_time
        if self.timer > 0.15:
            self.timer = 0
            self.i += 1
            if self.i == len(self.textures):
                self.i = 0
            self.texture = self.textures[self.i]
