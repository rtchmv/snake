import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_SNAKEBLOCK = .3125
SPRITE_SCALING_APPLE = 0.1

INITIAL_SNAKE_LENGTH = 10

class Snake_Block(arcade.Sprite):
    pass

class Snake(arcade.SpriteList):
    
    def __init__(self):
        super().__init__()
        block = Snake_Block ("element_green_square.png", SPRITE_SCALING_SNAKEBLOCK)
        block.center_x = random.randrange(5, SCREEN_WIDTH-5, 10)
        block.center_y = random.randrange(5, SCREEN_HEIGHT-5, 10)
        block.delta_x = -1
        block.delta_y = 0
        self.append(block)

        for i in range(1, INITIAL_SNAKE_LENGTH):
            block = Snake_Block ("element_red_square.png", SPRITE_SCALING_SNAKEBLOCK)
            block.center_x = self[0].center_x + 10*(i)
            block.center_y = self[0].center_y
            block.delta_x = -1
            block.delta_y = 0
            self.append(block)

        self.delta_x = -1
        self.delta_y = 0

        self.score = 0

    def update(self):
        temp_x = []
        temp_y = []

        for i in range(len(self)):
            temp_x.append(self[i].center_x)
            temp_y.append(self[i].center_y)

        self[0].center_x += 10 * self.delta_x
        self[0].center_y += 10 * self.delta_y

        for i in range(1, len(self)):
            self[i].center_x = temp_x[i-1]
            self[i].center_y = temp_y[i-1]

class Apple(arcade.Sprite):
    pass

class MyGame(arcade.Window):
    def __init__(self):
        """ Initializer """
        # Конструктор
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Snake", update_rate = 0.2)

        # Variables that will hold sprite lists.
        self.apple_list = None

        # Не показывать курсор
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):

        self.apple_list = arcade.SpriteList()
        self.snake = Snake()

        # Создаем apple объект
        apple = Apple("coin_01.png", SPRITE_SCALING_APPLE)

        # Генерируем случайные координаты apple
        apple.center_x = random.randrange(5, SCREEN_WIDTH-5, 10)
        apple.center_y = random.randrange(5, SCREEN_HEIGHT-5, 10)

        # Добавляем яблок в list
        self.apple_list.append(apple)

    def on_draw(self):
        arcade.start_render()
        
        self.apple_list.draw()
        self.snake.draw()
        
        output = f"Score: {len(self.snake)}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.snake.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT and self.snake.delta_x != 1:
            self.snake.delta_x = -1
            self.snake.delta_y = 0
        elif key == arcade.key.RIGHT and self.snake.delta_x != -1:
            self.snake.delta_x = 1
            self.snake.delta_y = 0
        elif key == arcade.key.UP and self.snake.delta_y != -1:
            self.snake.delta_x = 0
            self.snake.delta_y = 1
        elif key == arcade.key.DOWN and self.snake.delta_y != 1:
            self.snake.delta_x = 0
            self.snake.delta_y = -1

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
