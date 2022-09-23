from curses import window


class AI:
    window = None
    pad = None

    def __init__(self, window, pad):
        self.window = window
        self.pad = pad
    
    def makeMove(self, ball):
        if (ball.gameObject.x < (self.window.width / 2)):
            return None
        else:
            if ((ball.gameObject.y > self.pad.gameObject.y) and (ball.ySpeed <= 0) and self.pad.gameObject.y >= 0):
                self.pad.moveUp()
            elif ((ball.gameObject.y < self.pad.gameObject.y) and (ball.ySpeed >= 0) and self.pad.gameObject.y <= self.window.height):
                self.pad.moveDown()
            else:
                return None
