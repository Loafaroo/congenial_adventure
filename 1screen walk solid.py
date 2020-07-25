from tkinter import *
from time import sleep
from random import randint, choice, uniform

screen_width = 2550
screen_height = 1005

frame_width = 8250

quantum = 0.15

class MyBall():
    def __init__(self):
        self.center = [randint(-frame_width, screen_width + frame_width), randint(-frame_width, screen_height+frame_width)]    
        self.radius = choice([randint(1, 20), randint(60, 400)]) #choice([2]*50 + 30*[10] + 5*[randint(15, 450)])
        self.curvature = 1/self.radius
    
        self.x = [self.center[0] - self.radius, self.center[0] + self.radius]
        self.y = [self.center[1] - self.radius, self.center[1] + self.radius]

        self.velocity = [1.1, 0]
        self.displace = [None for _ in range(2)]

        self.color = choice(['#000000', '#FFFFFF'])

        self.linewidth = randint(1, 20)
        self.linewidth2 = randint(1, 10)
            
        self.Stamp()
        self.MoveIt()
        
    def option(self):
        if -frame_width <= self.center[0] < screen_width + frame_width and -frame_width <= self.center[1] < screen_height +frame_width:
            return True
        else:
            return False

    def wrap_xy(self):
        self.x = [self.center[0] - self.radius, self.center[0] + self.radius]
        self.y = [self.center[1] - self.radius, self.center[1] + self.radius]

    def PutCentBack(self):
        self.changeToFrameCoord()
        self.displace[0] = self.center[0] % (screen_width + 2*frame_width) - self.center[0]
        self.displace[1] = self.center[1] % (screen_height + 2*frame_width) - self.center[1]

        self.center[0] = self.center[0] % (screen_width + 2*frame_width)
        self.center[1] = self.center[1] % (screen_height + 2*frame_width)

        self.InverseToFrameCoord()

    def changeToFrameCoord(self):
        for i in range(2):
            self.x[i] += frame_width
            self.y[i] += frame_width
            self.center[i] += frame_width
            self.wrap_xy()

    def InverseToFrameCoord(self):
        for i in range(2):
            self.x[i] -= frame_width
            self.y[i] -= frame_width
            self.center[i] -= frame_width
            self.wrap_xy()

    def RadiusChange(self):
        if 2 < self.radius:
            self.konstant = randint(0, 13)/100
            self.chonk = uniform(1 - self.konstant, 1 + self.konstant/2)
        else:
            self.radius = randint(4, 32)
            self.chonk = 1
                   
        self.radius = int(self.chonk * self.radius)        
        
        self.wrap_xy()

    def BrownianV(self):
        if(randint(0,1) == 0):
            self.brownian_v = [.1*randint(-100,100)/100*self.velocity[1], .1*randint(-100,100)/100*self.velocity[0]]
            self.jerk = randint(3, 6)/2
            self.velocity[0] += self.jerk*self.brownian_v[0] + randint(-1, 1)
            self.velocity[1] += self.jerk*self.brownian_v[1]            

    def LineWidthChange(self):
        if self.linewidth < 1:
            self.widthchonk1 = randint(0, 2)
            self.widthchonk2 = randint(0, 2)
        else:
            self.widthchonk1 = randint(-2, 2)
            self.widthchonk2 = randint(-2, 2)

        self.linewidth += self.widthchonk1      

        self.linewidth2 += self.widthchonk2

    def MoveIt(self):
        """controls the representation of the box onscreen"""
        
        if not self.option():
            self.PutCentBack()                                                          ##### this puts the center back on the screen   #####

            self.wrap_xy()                                                              ##### this puts x and y back around the center  #####

            canvas.move(self.drawobj, self.displace[0], self.displace[1])              ##### this moves the representations back        #####
            canvas.move(self.drawobj2, self.displace[0], self.displace[1])             

        if randint(0,85) == 0:
            self.velocity = [0,0]

        self.center[0] += self.velocity[0]                                          #####  this updates the center now on the screen    #####
        self.center[1] += self.velocity[1]

        self.x[0] += self.velocity[0]
        self.x[1] += self.velocity[0]
        self.y[0] += self.velocity[1]
        self.y[1] += self.velocity[1]                                               #####  this updates x and y around the center       #####

        canvas.move(self.drawobj, self.velocity[0], self.velocity[1])
        canvas.move(self.drawobj2, self.velocity[0], self.velocity[1])             #####  this moves the representations back          #####
        
        self.BrownianV()

        #below is the execution of radius change and re wrap
        self.RadiusChange()

        self.LineWidthChange()
        
        #this part makes it more likely to draw ball if radius is small
        if randint(1, 1* self.radius) < 2:
            self.changeColor()
                    
        self._job = root.after(33, self.MoveIt )                                                    
                
    def cancel(self):
        if self._job is not None:
            root.after_cancel(self._job)
            self._job = None

    def changeColor(self):
        self.hex = self.color[1:]
        self.randswitch = randint(0, 5)
        self.bop = choice('0123456789ABCDEF')        
        
        if self.randswitch == 0:
            self.hex = self.bop + self.hex[1:]

        elif self.randswitch == 5:
            self.hex = self.hex[:5] + self.bop

        else:
            self.hex = self.hex[:self.randswitch] + self.bop + self.hex[self.randswitch + 1:]

        self.color = '#' + self.hex

        self.Stamp()

    def Stamp(self):
        try:    
            self.jig = randint(0, int(self.radius))
            self.jig2 = randint(0, int(self.radius))
            self.drawobj = canvas.create_line(self.x[0] - self.jig2, self.y[0] - self.jig,
                                              self.x[1] + self.jig2, self.y[1] + self.jig, fill = self.color, width= self.linewidth)
            self.switcharoo = randint(0, 2)
            if self.switcharoo == 0:
                self.drawobj2 = canvas.create_rectangle(self.x[0] - self.jig2, self.y[1] + self.jig,
                                                        self.x[1] + self.jig2, self.y[0] -  self.jig, outline = self.color, width = self.linewidth2)
            elif self.switcharoo == 1:
                self.drawobj2 = canvas.create_line(self.x[0] - self.jig2, self.y[1] + self.jig,
                                                   self.x[1] + self.jig2, self.y[0] -  self.jig, fill = self.color, width = self.linewidth2)
            elif self.switcharoo == 2:
                self.drawobj2 = canvas.create_oval(self.x[0] - self.jig2, self.y[1] + self.jig,
                                                   self.x[1] + self.jig2, self.y[0] -  self.jig, outline = self.color, width = self.linewidth2)
        except:
            pass
    
if __name__ == "__main__":
    root = Tk()

    canvas = Canvas(root, width = screen_width, height = screen_height, bg = 'white')                               #"#5b3f69")
    canvas.pack()        
    
    for j in range(345):
        b = MyBall()
        
    mainloop()
