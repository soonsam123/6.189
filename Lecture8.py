# Name: Soon Sam R Santos
# Date: January 30, 2017
# Session: Lecture 8
# Lecture8.py

#Defining a computer class.
class Computer:
    #Initializing with two parameters, the computer's color and mnftr.
    def __init__(self, color, mnftr):
        self.compu_color = color
        self.mnftr = mnftr
        self.os = ""
    #Installing the os.
    def install_os(self, new_os):
        self.os = new_os
    #Showing the os the computer is using.    
    def which_os(self):
        return self.os
c = Computer("black", "lenovo")
print c.which_os()
#Output nothing.

class Apple(Computer):
    #This class inherits from Computer because it is a Computer -
    #it is a specialized subset of computer.
    def __init__(self, color):
        #Inherit Computer's init method
        #So, call the init method of our superclass
        Computer.__init__(self, color, "Macintosh")
        self.ilife_installed = False
    def install_ilife(self):
        self.ilife_installed = True

my_computer = Apple("silver")
your_computer = Apple("white")
print my_computer.compu_color #silver
print your_computer.compu_color #white
print my_computer.mnftr #Macintosh
print your_computer.mnftr #Macintosh

my_computer.install_os("OS X")
print my_computer.which_os() #OS X
