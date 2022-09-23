from PPlay.sprite import *

class Ball:
    window = None
    gameObject = None
    absoluteSpeed = None
    xSpeed = None
    ySpeed = None

    def __init__(self, window, spritePath, initialSpeed):
        self.window = window
        self.gameObject = Sprite(spritePath, 1)

        self.gameObject.x = (self.window.width / 2) - (self.gameObject.width / 2)
        self.gameObject.y = (self.window.height / 2) - (self.gameObject.height / 2)

        self.absoluteSpeed = initialSpeed
        self.xSpeed = initialSpeed
        self.ySpeed = initialSpeed

    def xAxisCollisionCheck(self):
        if ((self.gameObject.y + self.gameObject.height) >= self.window.height):
            self.gameObject.y = self.window.height - self.gameObject.height
            self.ySpeed = -self.ySpeed

        if (self.gameObject.y <= 0):
            self.gameObject.y = 0
            self.ySpeed = -self.ySpeed

    def yAxisCollisionCheck(self, leftPad, rightPad):
        if (((self.gameObject.x + self.gameObject.width) >= self.window.width) and not rightPad.gameObject.collided(self.gameObject)):
            self.gameObject.x = (self.window.width / 2) - (self.gameObject.width / 2)
            self.gameObject.y = (self.window.height / 2) - (self.gameObject.height / 2)
        elif (((self.gameObject.x + self.gameObject.width) >= self.window.width) and rightPad.gameObject.collided(self.gameObject)):
            self.gameObject.x = self.window.width - self.gameObject.width
            self.xSpeed = -self.xSpeed
        
        if (self.gameObject.x <= 0 and leftPad.gameObject.collided(self.gameObject)):
            self.gameObject.x = 0
            self.xSpeed = -self.xSpeed
        elif (self.gameObject.x <= 0 and not leftPad.gameObject.collided(self.gameObject)):
            self.gameObject.x = (self.window.width / 2) - (self.gameObject.width / 2)
            self.gameObject.y = (self.window.height / 2) - (self.gameObject.height / 2)
    
    def move(self):
        self.gameObject.x += self.xSpeed * self.window.delta_time()
        self.gameObject.y += self.ySpeed * self.window.delta_time()  