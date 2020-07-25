from tkinter import *
from time import sleep
screen_width = 400
screen_height = 600

class MyBall():
    def __init__(self):
        self.center = [screen_width / 2, screen_height / 2]    
        self.radius = 12
    
        self.x = [self.center[0] - self.radius, self.center[0] + self.radius]
        self.y = [self.center[1] - self.radius, self.center[1] + self.radius]

        self.velocity = [5, 5]

        self.color = "black"
        self.drawobj = canvas.create_rectangle(self.x[0], self.y[0], self.x[1], self.y[1], fill = self.color)      

    def option(self):
        if 0 < self.center[0] < screen_width and 0 < self.center[1] < screen_height:
            return True
        else:
            return False

    def MoveIt(self):
        """when it hits the edge of the screen, move the drawing back to the other side of the screen!"""        
        if self.option():
            canvas.move(self.drawobj, self.velocity[0], self.velocity[1])
            self.Update()
        else:
            self.cancel()

        self._job = root.after(33, self.MoveIt)

    def Update(self):
        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

        self.x = [self.center[0] - self.radius, self.center[0] + self.radius]
        self.y = [self.center[1] - self.radius, self.center[1] + self.radius]

        

    def cancel(self):
        if self._job is not None:
            root.after_cancel(self._job)
            self._job = None
    

if __name__ == "__main__":
    root = Tk()

    canvas = Canvas(root, width = screen_width, height = screen_height)
    canvas.pack()

    masterball = MyBall()
    
    masterball.MoveIt()
    
    mainloop()
