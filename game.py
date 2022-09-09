# Imports
from PPlay.sprite import *
from PPlay.window import *

# Game Window Initialization
gameWindow = Window(1200,800)
gameWindow.set_title("Pong")

# Ball Initialization
ball = Sprite("./assets/images/ball.png", 1)
ball.x = (gameWindow.width / 2) - (ball.width / 2)
ball.y = (gameWindow.height / 2) - (ball.height / 2)

# Ball Speed
ballSpeedX = 1
ballSpeedY = 1

# Game Loop
while (gameWindow):
    gameWindow.set_background_color((0, 0, 0))

    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if (((ball.x + ball.width) == gameWindow.width) or (ball.x == 0)):
        ballSpeedX = ballSpeedX * -1

    if (((ball.y + ball.height) == gameWindow.height) or (ball.y == 0)):
        ballSpeedY = ballSpeedY * -1

    ball.draw()

    gameWindow.update()
