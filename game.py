# Imports
from PPlay.sprite import *
from PPlay.window import *

# Game Window Initialization
gameWindow = Window(1200,800)
gameWindow.set_title("Pong")

# Keyboard Initialization
keyboard = gameWindow.get_keyboard()

# Ball Initialization
ball = Sprite("./assets/images/ball.png", 1)
ball.x = (gameWindow.width / 2) - (ball.width / 2)
ball.y = (gameWindow.height / 2) - (ball.height / 2)

# Pads Initialization
leftPad = Sprite("./assets/images/pad.png", 1)
leftPad.x = 0
leftPad.y = (gameWindow.height / 2) - (leftPad.height / 2)

rightPad = Sprite("./assets/images/pad.png", 1)
rightPad.x = gameWindow.width - rightPad.width
rightPad.y = (gameWindow.height / 2) - (rightPad.height / 2)

# Ball Speed
ballSpeedAbsolute = 200
ballSpeedX = ballSpeedAbsolute
ballSpeedY = ballSpeedAbsolute

# Pads Speed
padsSpeedAbsolute = 200
leftPadSpeedY = padsSpeedAbsolute
rightPadSpeedY = padsSpeedAbsolute

# Game Loop
while (gameWindow):
    gameWindow.set_background_color((0, 0, 0))

    # Ball X Axis Collision
    if (((ball.x + ball.width) >= gameWindow.width) and rightPad.collided(ball)):
        ball.x = gameWindow.width - ball.width
        ballSpeedX = -ballSpeedX
    elif (((ball.x + ball.width) >= gameWindow.width) and not rightPad.collided(ball)):
        ball.x = (gameWindow.width / 2) - (ball.width / 2)
        ball.y = (gameWindow.height / 2) - (ball.height / 2)
    
    if (ball.x <= 0 and leftPad.collided(ball)):
        ball.x = 0
        ballSpeedX = -ballSpeedX
    elif (ball.x <= 0 and not leftPad.collided(ball)):
        ball.x = (gameWindow.width / 2) - (ball.width / 2)
        ball.y = (gameWindow.height / 2) - (ball.height / 2)

    # Ball Y Axis Collision
    if ((ball.y + ball.height) >= gameWindow.height):
        ball.y = gameWindow.height - ball.height
        ballSpeedY = -ballSpeedY

    if (ball.y <= 0):
        ball.y = 0
        ballSpeedY = -ballSpeedY

    # Ball Movement
    ball.x += ballSpeedX * gameWindow.delta_time()
    ball.y += ballSpeedY * gameWindow.delta_time()

    #Pads Movement
    if (keyboard.key_pressed("w") and leftPad.y > 0):
        leftPad.y -= leftPadSpeedY * gameWindow.delta_time()

    if (keyboard.key_pressed("s") and leftPad.y < (gameWindow.height - leftPad.height)):
        leftPad.y += leftPadSpeedY * gameWindow.delta_time()

    if (keyboard.key_pressed("UP") and rightPad.y > 0):
        rightPad.y -= rightPadSpeedY * gameWindow.delta_time()

    if (keyboard.key_pressed("DOWN") and rightPad.y < (gameWindow.height - rightPad.height)):
        rightPad.y += rightPadSpeedY * gameWindow.delta_time()
    
    # Draw Game Objects
    ball.draw()
    leftPad.draw()
    rightPad.draw()

    # Update Window
    gameWindow.update()
