import tkinter
import tkinter.messagebox as messagebox

def helloCallBack(num = None):
    messagebox.showinfo( "Hello tk", f"Just saying hello{num}")                     #creates a message prompt

class numberbutton():
    def __init__(self, frame, num):
        self.number = num
        self.frame = frame
        self.button = tkinter.Button(self.frame, text = f"Hello {self.number}",     ##notice lambda function (used to wait until button click to evaluate
                                     command = lambda: helloCallBack(self.number))  ##hellocallback at self.number, without it would evaluate automatically)
        self.button.pack()

def main():
    top = tkinter.Tk()
    Frame = tkinter.Frame(top)
    Frame.pack()
    
    for i in range(10):
        B = numberbutton(Frame, i)

    top.mainloop()

if __name__ == "__main__":
    main()
