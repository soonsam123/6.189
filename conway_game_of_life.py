from graphics import *
import random

## Written by Sarina Canelake & Kelly Casteel, August 2010
## Revised January 2011

############################################################
# GLOBAL VARIABLES
############################################################
    
BLOCK_SIZE = 40
BLOCK_OUTLINE_WIDTH = 2
BOARD_WIDTH = 12
BOARD_HEIGHT = 12

neighbor_test_blocklist = [(0,0), (1,1)]
toad_blocklist = [(4,4), (3,5), (3,6), (5,7), (6,5), (6,6)]
beacon_blocklist = [(2,3), (2,4), (3,3), (3,4), (4,5), (4,6), (5,5), (5,6)]
glider_blocklist = [(1,2), (2,3), (3,1), (3,2), (3,3)]
pulsar_blocklist = [(2,4), (2,5), (2,6), (4,2), (4,7), (5,2), (5,7),
                    (6,2), (6,7), (7,4), (7,5), (7,6), ]
# for diehard, make board at least 25x25, might need to change block size
diehard_blocklist = [(5,7), (6,7), (6,8), (10,8), (11,8), (12,8), (11,6)]

############################################################
# TEST CODE (don't worry about understanding this section)
############################################################

def test_neighbors(board):
    '''
    Code to test the board.get_block_neighbor function
    '''
    for block in board.block_list.values():
        neighbors = board.get_block_neighbors(block)
        ncoords = [neighbor.get_coords() for neighbor in neighbors]
        if block.get_coords() == (0,0):
            zeroneighs = [(0,1), (1,1), (1,0)]
            for n in ncoords:
                if n not in zeroneighs:
                    print "Testing block at (0,0)"
                    print "Got", ncoords
                    print "Expected", zeroneighs
                    return False

            for neighbor in neighbors:
                if neighbor.get_coords() == (1, 1):
                    if neighbor.is_live() == False:
                        print "Testing block at (0, 0)..."
                        print "My neighbor at (1, 1) should be live; it is not."
                        print "Did you return my actual neighbors, or create new copies of them?"
                        print "FAIL: get_block_neighbors() should NOT return new Blocks!"
                        return False

        elif block.get_coords() == (1,1):
            oneneighs = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1),(2,2)]
            for n in ncoords:
                if n not in oneneighs:
                    print "Testing block at (1,1)"
                    print "Got", ncoords
                    print "Expected", oneneighs
                    return False
            for n in oneneighs:
                if n not in ncoords:
                    print "Testing block at (1,1)"
                    print "Got", ncoords
                    print "Expected", oneneighs
                    return False
    print "Passed neighbor test"
    return True


############################################################
# BLOCK CLASS (Read through and understand this part!)
############################################################

class Block(Rectangle):
    ''' Block class:
        Implement a block for a tetris piece
        Attributes: x - type: int
                    y - type: int
        specify the position on the board
        in terms of the square grid
    '''

    def __init__(self, pos, color):
        '''
        pos: a Point object specifing the (x, y) square of the Block (NOT in pixels!)
        color: a string specifing the color of the block (eg 'blue' or 'purple')
        '''
        self.x = pos.x    # The Block x coordinates is receiving the Point x coordinates.
        self.y = pos.y    # The Block y coordinates is receiving the Point y coordinates.
        #Convertis the square inputed to pixels in order to draw on the screen.
        p1 = Point(pos.x*BLOCK_SIZE,
                   pos.y*BLOCK_SIZE)
        p2 = Point(p1.x + BLOCK_SIZE, p1.y + BLOCK_SIZE)

        Rectangle.__init__(self, p1, p2)
        self.setWidth(BLOCK_OUTLINE_WIDTH)
        self.setFill(color)
        # The block created begins as dead (white) and the new_status begins as 'None'.
        self.status = 'dead'
        self.new_status = 'None'
        
    def get_coords(self):
        # It just get the coords of the Block.
        return (self.x, self.y)

    def set_live(self, canvas):
        '''
        Sets the block status to 'live' and draws it on the grid.
        Be sure to do this on the canvas!
        '''
        # This method is executed only if the block is dead, then the status is changed to live and raw on the canvas.
        # Notice: The new_status is not altered here.
        if self.status=='dead':
          self.status = 'live'
          self.draw(canvas)

    def set_dead(self):
        '''
        Sets the block status to 'dead' and undraws it from the grid.
        '''
        # This method is executed only if the block is alive, then the status is changed to dead and undraw on the canvas.
        # As you undraw the block it will become White, which is dead. The new_status again is no altered here.
        if self.status=='live':
          self.status = 'dead'
          self.undraw()

    def is_live(self):
        '''
        Returns True if the block is currently 'live'. Returns False otherwise.
        '''
        # This method is just to check whether the Block is live or not.
        if self.status == 'live':
            return True
        return False

    def reset_status(self, canvas):
        '''
        Sets the new_status to be the current status
        '''
        # It takes the information of the new_status and append it into the block (status).
        # Summarazing, the current status will change to new_status.
        # If the block is already dead and the new_status is dead, it will just do nothing to save time.
        if self.new_status=='dead':
            self.set_dead()
        elif self.new_status=='live':
            self.set_live(canvas)
        

###########################################################
# BOARD CLASS (Read through and understand this part!)
# Print out and turn in this section.
# Name:
# Recitation:
###########################################################

class Board(object):
    ''' Board class: it represents the Game of Life board

        Attributes: width - type:int - width of the board in squares
                    height - type:int - height of the board in squares
                    canvas - type:CanvasFrame - where the blocks will be drawn
                    block_list - type:Dictionary - stores the blocks for a given position
    '''
    
    def __init__(self, win, width, height):
        self.width = width
        self.height = height
        self.win = win
        # self.delay is the number of ms between each simulation. Change to be
        # shorter or longer if you wish!
        self.delay = 1000

        # create a canvas to draw the blocks on
        self.canvas = CanvasFrame(win, self.width * BLOCK_SIZE,
                                       self.height * BLOCK_SIZE)
        self.canvas.setBackground('white')

        # initialize grid lines
        # draw_gridline is a method which translated pixels to square just to draw a line.
        # My line is been drawn in (Point(1,0),Point(1,12)) / (Point(2,0),Point(2,12)) / (Point(3,0),Point(3,12))
        # which turns out to be vertical lines begining in first x block.
        for x in range(1,self.width):
            self.draw_gridline(Point(x, 0), Point(x, self.height))
        # This is the same thing as above, but for horizontal lines.
        for y in range(1,self.height):
            self.draw_gridline(Point(0, y), Point(self.width, y))

        # For each square on the board, we need to initialize
        # a block and store that block in a data structure. A
        # dictionary (self.block_list) that has key:value pairs of
        # (x,y):Block will be useful here.
        self.block_list = {}

        ####### YOUR CODE HERE ######
        # Draw one block in each square of the board 12x12 = 144 squares.
        # My dictionary is storing each of the blocks in the position (x,y).
        # The blocks will be outputed on the screen randomly.
        for x in range(self.width):    #x goes from 0 to 11.
            for y in range(self.height):  #y goes from 0 to 11. 
                self.block_list['('+str(x)+','+str(y)+')'] = Block(Point(x,y), 'black')  #Blocks Values --> (0,0);(0,1);(0,2);(0,3);(0,4)
        # Properly working (OK).
                
        


    def draw_gridline(self, startp, endp):
        ''' Parameters: startp - a Point of where to start the gridline
                        endp - a Point of where to end the gridline
            Draws two straight 1 pixel lines next to each other, to create
            a nice looking grid on the canvas.
        '''
        #Converts to square.  (1 square * BLOCK_SIZE = 40) = 40 Pixels
        line = Line(Point(startp.x*BLOCK_SIZE, startp.y*BLOCK_SIZE), \
                    Point(endp.x*BLOCK_SIZE, endp.y*BLOCK_SIZE))
        line.draw(self.canvas)
        
        line = Line(Point(startp.x*BLOCK_SIZE-1, startp.y*BLOCK_SIZE-1), \
                    Point(endp.x*BLOCK_SIZE-1, endp.y*BLOCK_SIZE-1))
        line.draw(self.canvas)


    def random_seed(self, percentage):
        ''' Parameters: percentage - a number between 0 and 1 representing the
                                     percentage of the board to be filled with
                                     blocks
            This method activates the specified percentage of blocks randomly.
        '''
        for block in self.block_list.values():
            if random.random() < percentage:
                block.set_live(self.canvas)
    

    def seed(self, block_coords):
        '''
        Seeds the board with a certain configuration.
        Takes in a list of (x, y) tuples representing block coordinates,
        and activates the blocks corresponding to those coordinates.
        '''

        #### YOUR CODE HERE #####
        for coordinates in block_coords:   # block_coords = toad_blocklist = [(4,4), (3,5), (3,6), (5,7), (6,5), (6,6)] list of tuples.
            # coordinates is going to be each tuple. (4,4) ; (3,5) ; (3,6)
            # I will get the 0 th and the 1 th term of the tuple.
            x = coordinates[0]
            y = coordinates[1]
            #Now I have x = 4 and y = 4 / x = 3 and y = 5 / x = 3 and y = 6
            block = self.block_list['('+str(x)+','+str(y)+')']  #And this is exactly the keys of block list to access the values.
            block.set_live(self.canvas)
            #Properly Working (OK).
    


    def get_block_neighbors(self, block):   #block is each value in self.block_list.values(). 
        '''
        Given a Block object, returns a list of neighboring blocks.
        Should not return itself in the list.
        '''
        # Return a list of all the neighbors, it works for everysingle block on the board.
        #### YOUR CODE HERE #####
        #### Think about edge conditions!
        #Block coordinates x,y in squares.
        self.list_neighbors = []
        x = block.x
        y = block.y

        # I made a new copy of the neighbors, I should return them.
        # (6,6), Do not make a Block(Point(5,6)) and so forward, but return the Block at the side of (6,6).

        # Condition for the block in the upper left corner.
        if (x==0 and y==0):
            self.list_neighbors.append(self.block_list['('+str(x+1)+','+str(y)+')'])
            self.list_neighbors.append(self.block_list['('+str(x+1)+','+str(y+1)+')'])
            self.list_neighbors.append(self.block_list['('+str(x)+','+str(y+1)+')'])
        # Condition for the blocks in the lower left corner.
        elif (x==0 and y==11):
            self.list_neighbors.append(self.block_list['('+str(x+1)+','+str(y)+')'])
            self.list_neighbors.append(self.block_list['('+str(x+1)+','+str(y-1)+')'])
            self.list_neighbors.append(self.block_list['('+str(x)+','+str(y-1)+')'])
        # Condition for the block in the upper right corner.
        elif (x==11 and y==0):
            self.list_neighbors.append(self.block_list['('+str(x-1)+','+str(y)+')'])
            self.list_neighbors.append(self.block_list['('+str(x-1)+','+str(y+1)+')'])
            self.list_neighbors.append(self.block_list['('+str(x)+','+str(y+1)+')'])
        # Condition for the block in the lower right corner.
        elif (x==11 and y==11):
            self.list_neighbors.append(self.block_list['('+str(x-1)+','+str(y)+')'])
            self.list_neighbors.append(self.block_list['('+str(x-1)+','+str(y-1)+')'])
            self.list_neighbors.append(self.block_list['('+str(x)+','+str(y-1)+')'])

        # Condition for the blocks in the left edge.
        elif x==0 and y in range(1,11): # y goes from 1 to 10. Exclude 0 and 11.
            for i in range(-1,2): # i is -1,0,1.
                # Appending the three blocks in the right side.
                self.list_neighbors.append(self.block_list['('+str(x+1)+','+str(y+i)+')'])
                # Appending the upper and lower blocks. Condition to exclude the block itself.
                if (i != 0):
                    self.list_neighbors.append(self.block_list['('+str(x)+','+str(y+i)+')'])
        # Condition for the block in the right edge.
        elif x==11 and y in range(1,11): # y goes from 1 to 10. Exclude 0 and 11.
            for i in range(-1,2): # i is -1,0,1.
                # Appending the three blocks in the left side.
                self.list_neighbors.append(self.block_list['('+str(x-1)+','+str(y+i)+')'])
                # Appending the upper and lower blocks. Condition to exclude the block itself.
                if i != 0:
                    self.list_neighbors.append(self.block_list['('+str(x)+','+str(y+i)+')'])
        # Condition for the block in the lower edge.
        elif y==11 and x in range(1,11): # x goes form 1 to 10. Exclude 0 and 11.
            for i in range(-1,2): # i is -1,0,1.
                # Appending the three blocks in the upper side.
                self.list_neighbors.append(self.block_list['('+str(x+i)+','+str(y-1)+')'])
                # Appending the right and left blocks. Condition to exclude the block itself.
                if i != 0:
                    self.list_neighbors.append(self.block_list['('+str(x+i)+','+str(y)+')'])
        
        # Condition for the block in the upper edge.
        elif y==0 and x in range(1,11): # x goes form 1 to 10. Exclude 0 and 11.
            for i in range(-1,2): # i is -1,0,1.
                # Appending the three blocks in the lower side.
                self.list_neighbors.append(self.block_list['('+str(x+i)+','+str(y+1)+')'])
                # Appending the right and left blocks. Condition to exclude the block itself.
                if i != 0:
                    self.list_neighbors.append(self.block_list['('+str(x+i)+','+str(y)+')'])
                                           
        # Loop to return list of neighbors of the blocks in the middle.
        else:
            for i in range(-1,2):  # i is -1,0,1 / When executing the code the first Block will fall here, (6,6).
                # Appending the three left neighbors.
                self.list_neighbors.append(self.block_list['('+str(x-1)+','+str(y+i)+')'])
                # Appending the three right neigbors.
                self.list_neighbors.append(self.block_list['('+str(x+1)+','+str(y+i)+')'])
                # Appending the upper and lower neighbors.
                if i != 0:  # Conditing to avoid appending (x,y). The block itself.
                    self.list_neighbors.append(self.block_list['('+str(x)+','+str(y+i)+')'])
        return self.list_neighbors
       

    def simulate(self):
        '''
        Executes one turn of Conways Game of Life using the rules
        listed in the handout. Best approached in a two-step strategy:
        
        1. Calculate the new_status of each block by looking at the
           status of its neighbors.

        2. Set blocks to 'live' if their new_status is 'live' and their
           status is 'dead'. Similarly, set blocks to 'dead' if their
           new_status is 'dead' and their status is 'live'. Then, remember
           to call reset_status(self.canvas) on each block.
        '''

        #### YOUR CODE HERE #####
        for block in self.block_list.values():  # These are all the blocks on the board.
            # 1 - I will need to get their neighbors.
            # 2 - Apply the rules.
            # 3 - Attached the status of the block to new_status.
            # 4 - Change the status of the blocks.

            # Neighbors is a list with the neighbors. 
            neighbors = self.get_block_neighbors(block)
            live = 0
            dead = 0
            # Checking each neighbor and checking whether they are live or dead.
            for n in neighbors:
                if n.status == 'live':
                    live = live + 1
                if n.status == 'dead':
                    dead = dead + 1
            # Any live cell.
            if block.status == 'live':
                # with fewer than two live neighbours dies.
                if (live == 1) or (live == 0):
                    block.new_status = 'dead'
                # with more than three live neighbours dies.
                if (live == 4) or (live == 5) or (live == 6) or (live == 7) or (live == 8):
                    block.new_status = 'dead'
                # with exactly two or three live neighbours lives.
                if (live == 2) or (live == 3):
                    block.new_status = 'live'
            # Any dead cell.
            if block.status == 'dead':
                # with exactly three live neighbours becomes a live cell.
                if (live == 3):
                    block.new_status = 'live'
            

        # I will change the status now.
        for block in self.block_list.values():
            # Setting the new_status of the block.
            if block.new_status == 'live' and block.status == 'dead':
                block.set_live(self.canvas)
            if block.new_status == 'dead' and block.status == 'live':
                block.set_dead()
            # The blocks now were setted to dead or live.
            # I reset the status now to change its. 
            
            # I claim block.reset_status is doing nothing here, unless of doublechecking.
            block.reset_status(self.canvas)

        # Completely.        

    def animate(self):
        '''
        Animates the Game of Life, calling "simulate"
        once every second
        '''
        self.simulate()
        self.win.after(self.delay, self.animate)



################################################################
# RUNNING THE SIMULATION
################################################################

if __name__ == '__main__':    
    # Initalize board
    win = Window("Conway's Game of Life")
    board = Board(win, BOARD_WIDTH, BOARD_HEIGHT)

    ## PART 1: Make sure that the board __init__ method works    
    board.random_seed(.5)

    ## PART 2: Make sure board.seed works. Comment random_seed above and uncomment
    ##  one of the seed methods below
    #board.seed(toad_blocklist)

    ## PART 3: Test that neighbors work by commenting the above and uncommenting
    ## the following two lines:
    # board.seed(neighbor_test_blocklist)
    # test_neighbors(board)


    ## PART 4: Test that simulate() works by uncommenting the next two lines:
    #board.seed(toad_blocklist)
    # win.after(2000, board.simulate)

    ## PART 5: Try animating! Comment out win.after(2000, board.simulate) above, and
    ## uncomment win.after below.
    win.after(2000, board.animate)
    # Another blocklists.

    ## Yay, you're done! Try seeding with different blocklists (a few are provided at the top of this file!)
    
    win.mainloop()
                
