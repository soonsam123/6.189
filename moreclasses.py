from graphics import *

class Wheel():
    #Method to instantiate my class.
    def __init__(self, center, wheel_radius, tire_radius):
        #The tire circle will receive the center and the radius of the tire
        self.tire_circle= Circle(center, tire_radius)
        self.wheel_circle= Circle(center, wheel_radius)

    def draw(self, win):
        #Using recursion to in both tire and wheel
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    def move(self, dx, dy):
        self.tire_circle.move(dx, dy)
        self.wheel_circle.move(dx, dy)

    def set_color(self, wheel_color, tire_color):
        #set Fill add a color.
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)

    def undraw(self):
        self.tire_circle.undraw()
        self.wheel_circle.undraw()

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_center(self):
        return self.tire_circle.getCenter()
def main():
    # create a window with width = 700 and height = 500
    new_win= GraphWin('wheel',700,500)

    #What we'll need for the wheel...
    wheel_center = Point(200,200) #The wheel center is a Point at (200,200)
    tire_radius = 100 #The radius of the outer tire is 100
    
    #Make a wheel object
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)

    #Set its color
    new_wheel.set_color('red', 'black')

    #And finally, draw it
    new_wheel.draw(new_win)

    #Run the window loop (must be the *last* line in your code
    new_win.mainloop()
main()
