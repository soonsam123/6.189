# Name: Soon Sam R Santos
# Date: February 1, 2017
# Session: Homework 4
# Mywheel.py

from graphics import *
class Wheel:
    def __init__(self, center, wheel_radius, tire_radius):
        self.wheel_circle = Circle(center, wheel_radius)
        self.tire_circle = Circle(center, tire_radius)

    def draw(self, win):
        self.tire_circle.draw(win)   #The one you draw the first'll be the one that will subrepor the color of the other.
        self.wheel_circle.draw(win)

    def move(self, dx, dy):
        self.tire_circle.move(dx, dy)
        self.wheel_circle.move(dx, dy)

    def set_color(self, tire_color, wheel_color):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)

    def undraw(self):
        self.tire_circle.undraw()   #OBS : There is a space between undraw and the point in the other file.
        self.wheel_circle.undraw

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_center(self):
        return self.tire_circle.getCenter()

    def animate(self, win, dx, dy, n):
        if n>0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)
#Define a main function to run the code. You just type main() in the end of the code.
def main():
    #Creating a window.
    new_win = GraphWin('My Wheel', 700, 500)

    #What we'll need for the wheel.
    wheel_center = Point(200, 200)
    tire_radius = 180
    wheel_radius = 120
    
    #Creating a wheel.
    new_wheel = Wheel(wheel_center, wheel_radius, tire_radius)

    #Set its colors
    new_wheel.set_color('blue','yellow')

    #And finally draw it.
    new_wheel.draw(new_win)
    new_wheel.animate(new_win, 1, 0, 100)
    #Run the window loop (must be the *last* line in your code)
    new_win.mainloop()
main()
