#Name: Soon Sam R Santos
#Date: January 5, 2016


#****************LECTURE 3***********************
#****************HOMEWORK 2***********************
#****************WEDNESDAY***********************



# ***************Section 3.1*********************
#****************TYPE OF FUNCTIONS***********************

#Testing if I can put the type of the function equal to the name
#type("32")--> str if a='str', therefore a=type("32")
a=type(32)
print a
if a==int:
    print 'yes'

#Making an if statement to replace all the characteres for x, but not the
#signals: ! , ; : ?
a='Hello World!'
for letter in a:
    if letter.isalpha():
        print 'x'
    else:
        print letter
print "-----------------------------------------------"

#I tried to do the same thing as the above example, however,
#it didn't work in this way because "!" is recognized as str.
b=raw_input("Write a phrase")
for c in b:
    if type(c)==str:
        print 'x'
    else:
        print c
print "----------------------------------------------------"

# ***************Section 3.6/3.7*********************
#****************ADDING NEW FUNCTIONS***********************
#Using def to print blank lines
#One def can be inside another def
def threeLines():
    newLine()
    newLine()
    newLine()
    
def nineLines():
    threeLines()
    threeLines()
    threeLines()
def twentysevenLines():
    nineLines()
    nineLines()
    nineLines()
    
def newLine():
    print
print "----------------------------------------------------"

# ***************Section 3.9*********************
#****************ARGUMENTS***********************
#See what an arguments means
import math
#Argument ---> x
def printTwice(x):
    print x,x
    
#****************Section 3.10***********************
#****************VARIABLES AND PARAMETERS ARE LOCAL***********************
#Using more than one argument in a functions
#Notice that it is the same command python already has in his calculator
    #to the sum of numbers. (This one is useful for strings too)
def sum(x,y):
    sum123=x+y
    print sum123

#****************Section 3.12***********************
#****************FUNCTIONS WITH RESULTS***********************

def printThird(x):
    print x,x,x

#****************Section 6.5***********************
#****************ENCAPSULATION AND GENERALIZATION***********************
    
#Print multiples numbers, multiply each number by i
def printMultiples(n):
    i=1
    while i<=6:
        print n*i, "\t", 
        i+=1
    print

#Multiplication table
i=1
while i<=6:
    printMultiples(i)
    i+=1

#Function to the multiplication table
def printMultTable():
    i=1
    while i<=6:
        printMultiples(i)
        i+=1
#I am using i twice but they will not affect each other
#That's why one i is inside one function and the another i
#is inside another function. The variables just affect each other
#if they are inside the same function.

#****************Section 6.8***********************
#****************MORE GENERALIZATION***********************

#Printing Multiple Tables with the high I choose!
def printMultTable(high):
    i=1
    while i<=high:
        printMultiples(i)
        i+=1

    
