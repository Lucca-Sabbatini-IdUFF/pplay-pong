# Imports
from PPlay.sprite import *
from PPlay.window import *
from classes.Ball import *
from classes.Pad import *
from classes.AI import *

# Game Window Initialization
gameWindow = Window(1200,800)
gameWindow.set_title("Pong")

# Keyboard Initialization
keyboard = gameWindow.get_keyboard()

# Ball Initialization
ball1 = Ball(gameWindow, "./assets/images/ball.png", 200)

# Pads Initialization
leftPad = Pad(gameWindow, keyboard, "./assets/images/pad.png", 200, "left")
rightPad = Pad(gameWindow, keyboard,"./assets/images/pad.png", 200, "right")

# Scoreboard
leftScore = 0
rightScore = 0

# AI
padAI = AI(gameWindow, rightPad)

# Game Loop
while (gameWindow):
    gameWindow.set_background_color((0, 0, 0))

    # Ball X Axis Collision
    ball1.xAxisCollisionCheck()

    # Ball Y Axis Collision
    ball1.yAxisCollisionCheck(leftPad, rightPad)

    # Ball Movement
    ball1.move()

    #Pads Movement
    leftPad.controlMove()
    # rightPad.controlMove()
    padAI.makeMove(ball1)
    
    # Draw Game Objects
    ball1.gameObject.draw()
    leftPad.gameObject.draw()
    rightPad.gameObject.draw()

    # Update Window
    gameWindow.update()
