import arcade
from random import randint
from data import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from bird import Bird
from pipe import Pipe


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg_color = (0, 184, 230)
        self.background = arcade.load_texture("./images/bg.png")
        self.grass = arcade.Sprite("./images/grass.png", 1.146)
        self.grass.center_x = SCREEN_WIDTH / 2
        self.grass.center_y = 600
        self.gameover = arcade.load_texture("./images/gameover.png")
        self.bird = Bird()
        self.pipes = arcade.SpriteList()
        self.stop = False
        for i in range(5):
            pipe_position = randint(-200, 200)
            pipe = Pipe()
            pipe.top = SCREEN_HEIGHT / 2 - 100 + pipe_position
            pipe.left = SCREEN_WIDTH + i * 480
            self.pipes.append(pipe)

            pipe = Pipe(flipped=True)
            pipe.bottom = SCREEN_HEIGHT / 2 + 100 + pipe_position
            pipe.left = SCREEN_WIDTH + i * 480
            self.pipes.append(pipe)

    def on_draw(self):
        self.clear(self.bg_color)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,
                                      SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      self.background)

        self.bird.draw()
        self.pipes.draw()

        if self.stop:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,
                                          SCREEN_HEIGHT / 2,
                                          SCREEN_WIDTH / 4,
                                          100,
                                          self.gameover)

        self.grass.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.bird.on_key_press(symbol)

    def update(self, delta_time: float):
        if self.stop:
            return
        self.bird.update(delta_time)
        self.pipes.update()
        if arcade.check_for_collision_with_list(self.bird, self.pipes) or \
                arcade.check_for_collision(self.bird, self.grass):
            self.stop = True


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()

# сделать остановку игры
