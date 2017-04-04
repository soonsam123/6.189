# Name: Soon Sam R Santos
# Date: February 03, 2017
# Session: Homework 4
# dig_clock.py
from graphics import *

#How to draw text on the board.
#new_win = GraphWin("Digital Clock", 300, 300)

#Create a text object centered at (100, 100)
#msg1 = Text(Point(100,100), "Hello World")   #Text(Anchor_point, string)

#Setting some attributes to the text.
#msg1.setSize(25)
#msg1.setStyle('italic')
#msg1.setTextColor('gray')
#msg1.setFace('times roman')
#msg1.draw(new_win)

#Process events.
#new_win.mainloop()

# 2 - Drawing a Digital Clock!
# new_win...
# clock = DigitalClock(15, 30, 23)   #Brazilian time to receive, USA time to output. 15-->3pm 16--4pm
class DigitalClock:
    def __init__(self, hours, minutes, seconds):
        #Converting military hours to American hours.
        if 0<=hours<=12:
            self.hours = str(hours)
            #pm_am = "AM"
        if 12<hours<=24:
            self.hours = str(hours - 12)
            #pm_am = "PM"
        #Attributing each value.
        self.minutes = str(minutes)
        self.seconds = str(seconds)
        #Creating the text for the whole time.
        

    def draw(self, win):
    
        #Creating the Text.
        self.time = Text(Point(win.width*0.5,win.height*0.5), self.hours + ":" + self.minutes + ":" + self.seconds )
        self.time.setSize(25)

        #Creating the face rectangle.
        self.face_rectangle = Rectangle(Point(0.1*win.width, 0.1*win.height), Point(0.9*win.width, 0.9*win.height))
        self.face_rectangle.setFill("black")

        #Creating the inside rectangle.
        self.inside_rectangle = Rectangle(Point(0.2*win.width, 0.2*win.height), Point(0.8*win.width, 0.8*win.height))
        self.inside_rectangle.setFill("brown")

        #Drawing each one.
    
        self.face_rectangle.draw(win)
        self.inside_rectangle.draw(win)
        self.time.draw(win)
new_win = GraphWin("Digital Clock", 300, 300)
clock = DigitalClock(15, 30, 23)
clock.draw(new_win)
new_win.mainloop()
