from graphics import *

class Wheel():

    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, wheel_radius)

    def draw(self, win): 
        self.tire_circle.draw(win) 
        self.wheel_circle.draw(win) 

    def move(self, dx, dy): 
        self.tire_circle.move(dx, dy) 
        self.wheel_circle.move(dx, dy)

    def set_color(self, wheel_color, tire_color):
        self.tire_circle.setFill(tire_color) 
        self.wheel_circle.setFill(wheel_color)

    def undraw(self): 
        self.tire_circle .undraw() 
        self.wheel_circle .undraw() 

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_center(self):
        return self.tire_circle.getCenter()

    def animate(self, win, dx, dy, n):
        #4 parameters --> a GraphWin, units to move in x and y, and the number of times to call the animated method.
        if n>0:    #When the numbers of time is zero if will finish.
            self.move(dx,dy)
            win.after(100, self.animate, win, dx, dy, n-1)    #After method of GraphicWin object. 1 - Time in milliseconds after which GraphWin will call animated again.(100)
                                                                                                # 2 - The function object Graphwin needs to call.(self.animate)
                                                                                                # 


# Define a main function; if you want to display graphics, run main()
# after you load code into your interpreter
def main():
    # create a window with width = 700 and height = 500
    new_win = GraphWin('Wheel', 700, 500) 

    # What we'll need for the wheel...
    wheel_center = Point(200, 200) # The wheel center is a Point at (200, 200)
    tire_radius = 100  # The radius of the outer tire is 100

    # Make a wheel object
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)

    # Set its color
    new_wheel.set_color('red', 'black')

    # And finally, draw it 
    new_wheel.draw(new_win)
    new_wheel.animate(new_win, 1, 0, 1000)
    # Run the window loop (must be the *last* line in your code)
    new_win.mainloop()
    
# Comment this call to main() when you import this code into
#  your car.py file - otherwise the Wheel will pop up when you
#  try to run your car code.
main()