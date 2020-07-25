from tkinter import *
from time import sleep
import math

screen_w = 200
screen_h = 100
margin = int(screen_h/6)

def Ball():
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

def BallList():
    """Keeps track of all on- and off-screen balls, creates and destroys them"""
    def __init__(self, default):
        self.default = default
        if default == "":
            newBall = Ball(0, int(screen_h/2), 2, 0, 25)
            
        elif default == "Empty":
            pass
        
    def BallKeeper(self): ##what is this for? creating and destroying the right balls
        for ball in workingBallList:
            pass
    def BallMover(self):
        for ball in workingBallList:
            ball.x += ball.dx
            ball.y += ball.dy
    def reCreate(self):
        self.BallKeeper()
        self.BallMover()

def Screen():
    screen = Tk()
    canvas = Canvas(screen, width = screen_w, height = screen_h)
    canvas.pack()
    screen.mainloop()




screen = Screen()
        

    
