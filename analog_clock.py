# Name: Soon Sam R. Santos
# Date: February 03, 2017
# Session: Homework 4
# analog_clock.py
from graphics import *
import math
class AnalogClock:
    #Initializating my method. Here I need to receive the variables and execute the other methods.
    def __init__(self, hours, minutes, seconds, win):
        if 0<=hours<=12:
            self.hours = hours
        if 12< hours <=23:
            self.hours = hours - 12
        self.minutes = minutes
        self.seconds = seconds
        self.face_circle(win)
        self.Circunference_lines(win)
        self.Pointers_lines(win)
        
    def face_circle(self, win):
        #Creating the face Circle in the middle of the window with 40%  of height as the radius.
        self.Face = Circle(Point(0.5*win.width, 0.5*win.height), 0.4*win.height)
        #Setting the inside color.
        self.Face.setFill('pink')
        #Setting the outer width.
        self.Face.setWidth(5)

    def draw(self, win):
        #Defining the method to draw everything together.
        #Drawing the Circle Face.
        self.Face.draw(win)
        self.Pointersmin.draw(win)
        self.Pointershr.draw(win)
        #Drawing the middle point of the clock.
        self.middle_point.draw(win)
        #Drawing all the 60 lines.
        for line in self.Lines:
            line.draw(win)
        
    def Circunference_lines(self, win):
        #This method'll create the 60 lines that stay in the circunference.
        #Some variables that I'll use frequently.
        R = self.Face.getRadius()
        halfy = 0.5*win.height
        halfx = 0.5*win.width
        

        #GENERAL FORMULA FOR DRAWING ALL THE POINTS INSIDE THE CIRCLE.
        #A list to append all the points, the list is related with self.
        self.Lines = []
        #i will begin as pi/2 and finish as -3pi/2 to make the 60 lines of the circle.
        i= math.pi/2
        #Supporting variable to make me possible to draw bigger some points.
        j=0
        while (i > -(3*math.pi)/2):
            #Drawing a little bigger the lines that represent 12,3,6 and 9 hours.
            if (j== 0 or j== 15 or j== 30 or j== 45):
                #The calculus is just to add half of the width plus the length of the cos in that place (x), and halfy - the length of the sin in that place (y). The
                #second point of the line will be the samething, but as it was a smaller circle.
                self.Lines.append(Line(Point(halfx + math.cos(i)*R, halfy - math.sin(i)*R),Point(halfx + math.cos(i)*0.85*R, halfy - math.sin(i)*0.85*R)))
                #Making these points a little larger.
                self.Lines[j].setWidth(3)
                #Going to the next angle.
                i = i - (math.pi/30)
                j = j + 1

            #Drawing a little bigger the lines that represent 5,10,20,25,35,40,50 and 55.
            elif (j== 5 or j== 10 or j== 20 or j== 25 or j== 35 or j== 40 or j== 50 or j== 55):
                #The calculus is the same, but the line will be a little smaller than the previous if statement.
                self.Lines.append(Line(Point(halfx + math.cos(i)*R, halfy - math.sin(i)*R),Point(halfx + math.cos(i)*0.88*R, halfy - math.sin(i)*0.88*R)))
                #Making these points a littler larger, but smaller than the previous if statement.
                self.Lines[j].setWidth(2)
                #Going to the next angle.
                i = i - (math.pi/30)
                j = j + 1

            else:
                #Else, these are the other points in the clock, as 1,2,3,4,6..
                #The same calculus, but the lines are a little smaller than the previous if statement.
                self.Lines.append(Line(Point(halfx + math.cos(i)*R, halfy - math.sin(i)*R),Point(halfx + math.cos(i)*0.9*R, halfy - math.sin(i)*0.9*R)))
                #Going to the next angle.
                i = i - (math.pi/30)
                j = j + 1
    def Pointers_lines(self, win):
        #Defining the variables I'll use the most.
        R = self.Face.getRadius()
        halfy = 0.5*win.height
        halfx = 0.5*win.width

        #These is to create the point in the middle of the clock. I created a circle to make the point bigger.
        self.middle_point = Circle(Point(halfx, halfy), 4)
        self.middle_point.setFill('black')

        #These list will have all the angles. 0 to 60. (61 position because I am counting the 12 point twice.
        self.angles = []
        i = math.pi/2
        while (i >= - ((3*math.pi)/2)):
            self.angles.append(i)
            i = i - (math.pi/30)
        #Hours
        anglehr = self.angles[self.hours*5]      
        self.Pointershr = Line(Point(halfx, halfy), Point(halfx + math.cos(anglehr)*0.5*R, halfy - math.sin(anglehr)*0.5*R))
        self.Pointershr.setWidth(3)
        
        #Minutes
        self.min_support = self.minutes 
        anglemin = self.angles[self.minutes]    
        self.Pointersmin = Line(Point(halfx, halfy), Point(halfx + math.cos(anglemin)*0.7*R, halfy - math.sin(anglemin)*0.7*R))
        self.Pointersmin.setWidth(2)

        #Seconds
        self.sec_support = self.seconds 
        anglesec = self.angles[self.seconds]    
        self.Pointerssec = Line(Point(halfx, halfy), Point(halfx + math.cos(anglesec)*0.7*R, halfy - math.sin(anglesec)*0.7*R))
        self.Pointerssec.setWidth(1)
        #Receiving the first second the user typed.

    def animate(self, win, n, j, z):
        #Defining the variables I'll use the most.
        R = self.Face.getRadius()
        halfy = 0.5*win.height
        halfx = 0.5*win.width

        #Seconds.
        self.Pointerssec.undraw()

        anglesec = self.angles[self.seconds]         #It will point towards the second the user typed.
        self.Pointerssec = Line(Point(halfx, halfy), Point(halfx + math.cos(anglesec - (n*(math.pi/30)))*0.7*R, halfy - math.sin(anglesec - n*(math.pi/30))*0.7*R))
        self.Pointerssec.draw(win)
        self.sec_support = self.sec_support + 1
        #If there is in the 60 seconds.
        #Minutes.
        if ((self.sec_support + (2*j)) % 62) == 0 :
            j = j + 1
            self.min_support = self.min_support + 1
            self.Pointersmin.undraw()
            #Chossing where the minute pointer is pointed.
            anglemin = self.angles[self.minutes]  
            self.Pointersmin = Line(Point(halfx, halfy), Point(halfx + math.cos(anglemin - (j*(math.pi/30)))*0.7*R, halfy - math.sin(anglemin - (j*(math.pi/30)))*0.7*R))
            self.Pointersmin.setWidth(2)
            self.Pointersmin.draw(win)
        if (((self.min_support + (2*z)) % 62) == 0):
            z = z + 1
            self.Pointershr.undraw()
            anglehr = self.angles[self.hours*5]      
            self.Pointershr = Line(Point(halfx, halfy), Point(halfx + math.cos(anglehr - (z*(math.pi/30)))*0.5*R, halfy - math.sin(anglehr - (z*(math.pi/30)))*0.5*R))
            self.Pointershr.setWidth(3)
            self.Pointershr.draw(win)

        win.after(1, self.animate, win, n + 1, j, z)
        
#Testing the code in a 500x500 screen.
new_win=GraphWin("Analog Clock", 500, 500)
clock = AnalogClock(17, 47, 50, new_win)
clock.draw(new_win)
clock.animate(new_win, 0, 0, 0)
new_win.mainloop()


