import time
from playsound import playsound
from tkinter import *


class Application (Frame):
    def __init__(self , master=None , initialtime=25*60):
        super ().__init__ (master)

        self.initialtime = initialtime
        self.remaining = 0

        self.topFrame = Frame (self)
        self.bottomFrame = Frame (self)

        self.watchBox = Label (self.topFrame , text=self.secToMinSec (self.initialtime))

        self.startButton = Button (self.bottomFrame , text='Start')
        self.startButton['command'] = self.pressStart

        self.stopButton = Button (self.bottomFrame , text='Stop')
        self.stopButton['command'] = self.pressStop

        self.resetButton = Button (self.bottomFrame , text='Reset')
        self.resetButton['command'] = self.pressReset

        self.quitButton = Button (self.bottomFrame , text="QUIT")
        self.quitButton['command'] = self.closeWindow

        self.image1 = PhotoImage (file="c:\\pomodoro.gif")
        self.image2 = PhotoImage (file="c:\\pomodoro.gif")

        self.label1 = Label (image=self.image1)

        self.pack ()
        self.topFrame.pack ()
        self.watchBox.pack ()
        self.bottomFrame.pack ()
        self.startButton.pack (side="left")
        self.stopButton.pack (side="left")
        self.resetButton.pack (side="left")
        self.quitButton.pack (side="left")
        self.label1.pack ()
    def secToMinSec(self , seconds=0):
        minSecStr = str (divmod (seconds , 60)[0]) + "m " + str (divmod (seconds , 60)[1]) + "s"
        return minSecStr
    def pressStart(self):
        self.startCountdown (self.initialtime - self.remaining)
    def pressStop(self):
        if self.remaining == 0:
            pass
        else:
            previousstatus = self.remaining
            self.destroy ()
            self.topFrame.destroy ()
            self.watchBox.destroy ()
            self.bottomFrame.destroy ()
            self.startButton.destroy ()
            self.stopButton.destroy ()
            self.resetButton.destroy ()
            self.quitButton.destroy ()
            self.label1.destroy ()
            self.__init__ (master=root , initialtime=previousstatus)
    def pressReset(self):
        self.destroy ()
        self.topFrame.destroy ()
        self.watchBox.destroy ()
        self.bottomFrame.destroy ()
        self.startButton.destroy ()
        self.stopButton.destroy ()
        self.resetButton.destroy ()
        self.quitButton.destroy ()
        self.label1.destroy ()
        self.__init__ (master=root)
    def startCountdown(self , remaining=None , stopped=False):
        if stopped is False:
            if remaining is not None:
                self.remaining = remaining

            if self.remaining <= 0:

                self.watchBox.configure (text="time's up!")

                self.initialtime = 0
                self.label1.destroy ()
                self.label1 = Label (image=self.image2)

                self.label1.pack ()

                playsound ('bell.mp3')

            else:
                self.watchBox.configure (text=self.secToMinSec (self.remaining))

                # self.watchBox.configure (text="%d" % self.remaining)
                #            self.watchBox.pack ()
                self.remaining = self.remaining - 1
                self.after (1000 , self.startCountdown)
        else:
            self.watchBox.configure (text=self.secToMinSec (self.remaining))
    def closeWindow(self):
        print (str (time.ctime (time.time ())))
        root.destroy ()

if __name__ == '__main__':
    root = Tk ()
    # aFrame=Frame(root)
    # aButton=Button(aFrame,text="SCHIACCIAMI")
    # aButton.pack()
    # aFrame.pack()
    # root.mainloop()


    app = Application (master=root)
    app.master.title ("Pomodoro Timer")
    app.mainloop ()


