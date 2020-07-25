from tkinter import *

screen_w = 400
screen_h = 300

class WrappingScreen():    
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = screen_w, height = screen_h)
        self.canvas.pack()

class MovingBall():
    def __init__(self):
        self.x = int(screen_w / 2)
        self.y = 0
        self.dx = 0
        self.dy = 5
        
        self.screenList = [None for _ in range(9)]
        self.screenList[4] = True

    def multi_repr(self):
        """Each ball knows which screens it is being represented on"""
        if self.topleft():
            self.screenList = [False, False, False,
                               False, True, True,
                               False, True, True]
            
        if self.topright():
            self.screenList = [False, False, False,
                               True, True, False,
                               True, True, False]

        if self.botleft():
            self.screenList = [False, True, True,
                               False, True, True,
                               False, False, False]
            
        if self.botright():
            self.screenList = [True, True, False,
                               True, True, False,
                               False, False, False]       
            

    def left(self):
        return (0 < self.x < screen_w / 2)
    def right(self):
        return (screen_w / 2 < self.x < screen_w)
    def top(self):
        return(0 < self.y < screen_h / 2)
    def bottom(self):
        return (screen_h / 2 < self.y < screen_h)
    
    def topleft(self):
        return (self.top() and self.left())
    def topright(self):
        return (self.top() and self.right())
    def botleft(self):
        return (self.bottom() and self.left())
    def botright(self):
        return (self.bottom() and self.right())           

    def moveonscreen(self):
        pass

if __name__ == "__main__":
    screen = WrappingScreen()
    ball = MovingBall()
    ball.multi_repr()

    # if ball 

    #make ball fall from the top of the screen. by the time it gets to the bottom half of the screen, a copy of it should be created 
    
    mainloop()
