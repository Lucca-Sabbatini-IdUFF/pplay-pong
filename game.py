from PPlay.sprite import *
from PPlay.window import *

gameWindow = Window(1200,800)
gameWindow.set_title("Pong")
gameWindow.set_background_color ((0,0,0))

ball = Sprite("./assets/images/ball.png", 1)
ball.x = (gameWindow.width / 2) - (ball.width / 2)
ball.y = (gameWindow.height / 2) - (ball.height / 2)

while (gameWindow):
    ball.draw()
    gameWindow.update()
