# Name: Soon Sam R Santos
# Date: February 01, 2017
from graphics import *       #Using the graphics.py
def main():
    win = GraphWin("My Circle", 100, 100)       # Name, dimensions of the screen.
    c = Circle(Point(50,50),10)                 #Circle in the middle, Radius 10.
    c.draw(win)                                 #Drawing something in the window.
    win.getMouse()                              #pause for click in window
    win.close()
main() #Draw a circle in the middle of a square.

#GraphWin Objects (win.object()) <-- to be invoked.

#GraphWin(title, width, height, autoflush)   Default Values --> title 'Graphics Window' / widthxheight = 200x200 / False.
#plot(x, y, color) Default Values --> Color 'black' / Draws the pixel at (x,y) in the window. Note: Inefficient.
#plotPixel(x, y, Color) Draw the pixel at the 'raw' position(x,y). Note: Inefficient.
#setBackground(color) Window's background color. Default Value --> Gray.
#close() Closes the on screen window. Further operations will cause error.    
#isClosed() Return a Boolean --> If it was closed by close or by click in the close box.
#getMouse() Pauses for the user to click in the window and returns where the mouse was clicked. IF i don't use the window'll just open and close.
#setCoords(xll, yll, xur, yur) Sets the coordinate system of the window.Lower Left corner -> ll /Upper Right corner -> ur
#update() Causes any pending window operations to be performed. Useful for animation.

#3 - Graphics Objects (Point, Line, Circle, Oval, Rectangle, Polygon and Text).

#setFill(color) The interior of the object color.
#setOutline(color) The outline of the object color.
#setWidth(pixels)  Sets the width of the outline of the object to this many pixels.
#draw(aGraphWin) Draws the object into the given window. An object may be drawn in onlo one window at each time.
#undraw()  Undraw the object.
#move(dx, dy) Move dx units in the x-axes and dy units in y-axes.
#clone() Returns a duplicate of the object.

#3.1 - Point Methods
#Point(x, y) Contructs a point with the given coordinates.
#getX()  Returns the x coordinate of a point.
#getY()  Returns the y coordinate of a point.

#3.2 - Line Methods
#Line(point1, point2)   Line segment from point 1 to point2
#setArrow(string)  Sets the arrowhead status of a line. string --> 'first', 'last', 'both', 'none'<..Default Value.
#getCenter()   Clone of the midpoint of the line segment.    
#getP1(), getP2()  Clone of the corresponding endpoint of the segment.

#3.3 - Circle Methods
#Circle(centerPoint, radius) Constructs a circle.
#getCenter()  Clone of the center point of the circle.
#getRadius()  Returns the radius of the circle.
#getP1(), getP2() Returns a clone of the corresponding corner of the circle's bounding box. Opposito cornes of the square that cirumscribes the circle.

#3.4 - Rectangle Methods
#Rectangle(point1, point2)  Constructs a rectangle, values -- > opposite corners.
#getCenter()  Returns a clone of the center point.
#getP1(), getP2()  Returns a clone of the corners used to construc the rectangle.

#3.5 - Oval Methods
#Oval(point1, point2)  Constructs an oval delimeted bu the points.
#getCenter()  Returns a clone of the center of the oval.
#getP1(), getP2()   Returns a clone of the points used to construct the oval.


#3.6 - Polygon Methods
#Polygon(point1, point2, point3...) Just construc a polygon with the coordinates given. Can be 1 (list of the vertices) or as many as you can.
#getPoints()    Returns a list containing the clone of the points used to construct the polygon.

#3.7 - Text Methods
#Text(anchorPoint, string)   The string(text) is centered in the anchorPoint.
#setText(string)             Set the text of the object to a string.
#getText()                   Returns the current string
#getAnchor()                Returns a clone of the anchorpoint.
#setFace(family)            Changes the font of the text to family. Values --> 'helvetica', 'courier', 'times roman', 'arial'
#setSize(point)             Change the font size. 5 to 36 are acceptable.
#setStyle(style)            Changes the style of the font. Values --> 'normal', 'bold', 'italic', 'bold italic'
#setTextColor(color)        Sets the color of the text to the color. setFill is the samething.

#4 - Entry Objects
#Displayed as text entry boxes that can be edited by the user
#Supports the generic graphics move(), draw(graphwin), undraw(), setFill(color), clone().
#Entry(centerPoint, width)   Constructs an Entry, width is specificied in the number of carhacteres it can have.
#getAnchor()         Returns clone of the point where the Entry is centered.
#getText()          Returns the string of the text that is currently in the netry box.
#setText(string)    Set the text to a specific string. Can change the font. Values --> 'helvetica', 'courier', 'times roman', 'arial'
#setSize(point)     Font size. 5 to 36 are accepatable values.
#setStyle(style)    Changes the style of the font. Values --> 'normal', 'bold', 'italic', 'bold italic'
#setTextColor(color)  Color of the text.

#5 - Displaying images

#Can generate an image in a file. Supports bitmap, PPM, GIF images.
#Suppots the generic methods move(dx,dy), draw(graphwin), undraw(), clone().
#Image(centerPoint, filename) Constructs an image from the content of the given file, centered at the given point.
#getAnchor()         Returns a clone of the point where the image is centered.

#6 - Generating Colors
#For commun colors you just type the name as strings 'red', 'purple', 'green', 'cyan'... 
#For the intensity of the color 'red1', 'red2', 'red3'....
#Your own color ::> color_rgb(red, green, blue) will return a string representing a color that is the mixture of these ones.
#These should be ints 0-255. color_rgb(255, 0, 0) --> bright red
#color_rgb(130, 0, 130) is a medium magneta

#7 - Using an IDE
#IDLE will be unresponsive during getMouse operations.
