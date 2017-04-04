# Name: Soon Sam R Santos
# Date: February 1, 2017
# Session: Homework4
# car.py

from graphics import *
#from Mywheel import *   If I use it I don't need to make the class for wheel again.
#win = GraphWin('My first car', 300,300)
#rect = Rectangle(Point(10,10), Point(200,100))   #Left Upper corner to the Lower Right corner.
#rect.setFill('blue')
#rect.draw(win)

#win.mainloop()

class Wheel:
    #This method wil create the Circle of the tire and of the wheel.
    def __init__(self, center, tire_radius, wheel_radius=0):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, tire_radius*0.6)  #Don't need to input the wheel_radius, it'll be just 60% of the tire radius.

    #This methos will actually draw the wheel.
    def draw(self, win):
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    #Set colors to the wheel.
    def set_color(self, tire_color, wheel_color='black'):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)

    #Method to move the wheel.
    def move(self, dx, dy):
        self.tire_circle.move(dx, dy)
        self.wheel_circle.move(dx, dy)

    #Method to undraw the wheel.
    def undraw(self):
        self.tire_circle.undraw()
        self.wheel_circle.undraw()

    #To get the radius
    def get_size(self):
        return self.tire.circle.getRadius()

    #To get the center.
    def get_center(self):
        return self.tire_circle.getCenter()
    
    #Method to make my wheel move.
    def animate(self, win, dx, dy, n):
        if n>0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)  #GraphWin will execute self.animate again after 100 milliseconds and will subtract 1 from n.
#Defining a function to construct my wheel.
def main():
    #Creating the GraphWin.
    new_win = GraphWin("My Wheel", 500, 500)

    #Parameters to initializate Wheel.
    center = Point(250,250)
    tire_radius = 100

    #Initializating my wheel.
    new_wheel= Wheel(center, tire_radius, 0.6*tire_radius)

    #Setting the color to it.
    new_wheel.set_color('blue','yellow')

    #Drawing it on the screen
    new_wheel.draw(new_win)

    #Making the wheel move.
    new_wheel.animate(new_win, 1, 0, 50)
        
    #Loop in the last line
    new_win.mainloop()
#main() Creates a moving wheel.
#Now I am going to construct the class for the car.
#Car will contain 3 attributes. Two Wheel objects and one Rectangle object
#car1 = Car(Point(50,50), 15, Point(100,50), 15, 40)   40 --> height of the rectangle
class Car:
    #Initializating the Car variables.
    def __init__(self, center1, radius1, center2, radius2, height):
        self.wheel1 = Wheel(center1, radius1)
        self.wheel2 = Wheel(center2, radius2)
        x1 = center1.getX()
        x2 = center2.getX()
        y1 = center1.getY()
        y2 = center2.getY()
        self.rect = Rectangle(Point(x1, y1 - height), Point(x2, y2))  #Rectangle from (x = center of the first wheel, y = Y of the wheel minus the heigh)
                                                                      #Rectangle from (x = center of the second wheel, y = the same y for the second wheel)
        
    #Drawing it on the screen.
    def draw(self, win):
        self.rect.draw(win)
        self.wheel1.draw(win)
        self.wheel2.draw(win)

    #A method to move the variables.
    def move_car(self, dx, dy):
        self.wheel1.move(dx, dy)
        self.wheel2.move(dx, dy)
        self.rect.move(dx, dy)

    #A method to animate thecar.
    def animate_car(self, win, dx, dy, n):
        self.move_car(dx, dy)
        win.after(50, self.animate_car, win, dx, dy, n-1)    #My GraphWin is going to execute the next movement 100milliseconds after and will subtract one from n.

    def set_color_car(self, wheel1_color, wheel2_color, rect_color):
        self.wheel1.set_color(wheel1_color)
        self.wheel2.set_color(wheel2_color)
        self.rect.setFill(rect_color)
def main():
    #Creating the window.        
    new_win= GraphWin("My first car", 500, 500)

    #Creating the car.
    car = Car(Point(50,50), 15, Point(100,50), 15, 40)

    #Drawing the car.
    car.draw(new_win)

    #Setting color to the car.
    car.set_color_car('blue','yellow','black')

    #Making the car move.
    car.animate_car(new_win, 1, 0, 100)

    #Last line to make the code run.
    new_win.mainloop()

main()
