# Name: Soon Sam R Santos
# Date: February 02, 2017
# Session: Homework 4
# tetrominoes.py
from graphics import *
#Tetris board : 10x20 squares.  1 square: width of 30 pixels.
#Tetris board : 300x600 pixes.  1 square: 30x30 pixels
#A rectangle in the square 1x1. Is a rectangle inside the whole pixel 30x30. Rectangle(Point(0,0), Point(30,30))

#block = Block(Point(1,1), 'red')
        

        
class Block:
    #This method will create the blok. 
    def __init__(self, point_square, color):  #The parameters are self, the Point where it should be positioned in squares and the color.
        #Getting x and y from the Point given.
        x = point_square.getX()
        y = point_square.getY()
        #Creating the rectangle. 
        self.block = Rectangle(Point(30*x , 30*y), Point(30*(x+1), 30*(y+1)))  #The equations transform the points given in squared to pixels to create the rectangle.
        self.block.setFill(color)  #Setting the color to the block.
    def draw(self, win):
        self.block.draw(win)
#Uncoment to see the code running.
        
#new_win = GraphWin("Tetrominoes", 150, 150)
#square = Block(Point(3,4), 'red')
#square.draw(new_win)
#new_win.mainloop()
               
class Shape: #1 - Has a list of blocks as an attribute.
             #2 - Draw method.
    def __init__(self, coords, color):  #coords is a list of Points.
        #Point(1,1)Point(2,1)Point(3,1)Point(4,1)
        self.shape = []
        for point in coords:  #I will pass throughout these points and I'll create Blocks.
            self.shape.append(Block(point, color))
    def draw(self, win):      #Drawing each block that are in my list self.shape.
        for block in self.shape:
            block.draw(win)

class I_shape(Shape):
    #This class will create the I horizontally shape.
    def __init__(self, center):  #Center is a Point that holds the position of the central block in the shape. In this case, of the third block. (In squares)
        #Creating the coords points.
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),]
        #Shape'll take care of drawing each square on the window.
        Shape.__init__(self, coords, 'blue')
#Uncoment to see the code running.

#new_win = GraphWin("Tetrominoes", 150, 150)
#shape = I_shape(Point(4,2))
#shape.draw(new_win)
#new_win.mainloop()

class J_shape(Shape):
    #Creating the L shape. Inherits from Shape class.
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1),]
        Shape.__init__(self, coords, 'orange')
#new_win = GraphWin("Tetrominoes", 150, 150)
#shape = L1_shape(Point(4,2))
#shape.draw(new_win)
#new_win.mainloop()

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x - 1, center.y    ),
                  Point(center.x    , center.y    ),
                  Point(center.x + 1, center.y    ),]
        Shape.__init__(self, coords, 'pink')
#new_win = GraphWin("Tetrominoes", 150, 150)
#shape = L_shape(Point(3,3))
#shape.draw(new_win)
#new_win.mainloop()

class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'red')

#new_win = GraphWin("Tetrominoes", 150, 150)
#shape = O_shape(Point(3,3))
#shape.draw(new_win)
#new_win.mainloop()

class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y + 1),
                  Point(center.x    , center.y    ),
                  Point(center.x + 1, center.y    )]
        Shape.__init__(self, coords, 'green')

#new_win = GraphWin("Tetrominoes", 150, 150)
#shape = S_shape(Point(3,3))
#shape.draw(new_win)
#new_win.mainloop()

class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y    ),
                  Point(center.x    , center.y    ),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y    )]
        Shape.__init__(self, coords, 'green')

#new_win = GraphWin("Tetrominoes", 150, 150)
#shape = T_shape(Point(3,3))
#shape.draw(new_win)
#new_win.mainloop()

class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y    ),
                  Point(center.x    , center.y    ),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, 'green')

#new_win = GraphWin("Tetrominoes", 150, 150)
#shape = Z_shape(Point(3,3))
#shape.draw(new_win)
#new_win.mainloop()

new_win= GraphWin("Tetrominoes", 900, 150)  #Win of 30x5 squares.
tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
x = 3
for tetromino in tetrominoes:
    shape = tetromino(Point(x, 1))   #This will be to initializate each class.
    shape.draw(new_win)
    x += 4
new_win.mainloop()
