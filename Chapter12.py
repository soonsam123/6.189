#Name: Soon Sam R Santos
#Date: January 21, 2017
#Session: Lecture 6 - Chapter 12
#Chapter12.py

#*********************12*****************************
#***************Classes and Objects*****************

#*********************12.1*****************************
#************User-defined compound types***************
#How to input a point in anywhere in the screen (x,y)
#Usually we put in the beginning of the program (after the imports)
#Create a new class called Point
class Point:
    #Pass statement has no effect.
    #Just because a compound system must have something in its body
    pass

#Members of this type: instances
#Creating a new instance: instantiation
blank=Point()
#Constructor

#*********************12.2*****************************
#************Attributes***************

#To add new data to an instance
blank.x=3.0
blank.y=4.0
#Attributes

print blank.y
#4.0
x=blank.x
print x
#3.0

#Exercise
#Creating a Point called Soon
class Soon:
    pass
id=Soon()
print id

print "----------------------------------------------"#Organazing
#*********************12.3*****************************
#************Instances as arguments***************

#Instances can be an argument in a function
def printPoint(p):
    print "("+str(p.x)+","+str(p.y)+")"
#Using the function
print printPoint(blank)
#(3.0,4.0)
distanceSquared=blank.x*blank.x+blank.y*blank.y
print distanceSquared

print "----------------------------------------------"#Organazing
#*********************12.4*****************************
#************Sameness***************

p1=Point()
p1.x=3
p1.y=4
p2=Point()
p2.x=3
p2.y=4
print p1==p2
#False
#Same coordinates, but not the same object
#Assigning the value of p2 to p1
p1=p2
print p1==p2
#True
#Now they are the same object
#SHALLOW EQUALITY: Compare the references, not the contents of the objects

#DEEP EQUALITY: To compare the content of the objects
def samePoint(p1,p2):
    return (p1.x==p1.x) and (p1.y==p2.y)
#Making my variable p3 be a point
p3=Point()
p3.x=3
p3.y=4
#Making my variable p4 be a point
p4=Point()
p4.x=3
p4.y=4
print samePoint(p3,p4)
#True
#Now I am checking the content of the points, and they are equal
#But warn, it does not refer to the same object.
#Of course, if they refer to the same object, they will have both shallow and deep eq

print "----------------------------------------------"#Organazing
#*********************12.5*****************************
#************Rectangles***************

#To define a rectangle I will define its upper-left corner and size.
#Just horizontal and vertically sides.
#Define a new class
class Rectangle:
    pass
#Instantiate it
box=Rectangle()
box.width=100.0
box.height=200.0
#to specifh the upper-left corner. I can embed an object within an object!!
box.corner=Point()
box.corner.x=0.0
box.corner.y=0.0


#*********************12.6*****************************
#************Instances as return values***************
#Functions can return instances
#Finding the center of a rectangle
def findCenter(box):
    #I will denominate p as a point
    p=Point()
    #And I'll make p be my center coordinates
    #X coordinate of the center = upper-left.x + width/2
    p.x = box.corner.x + box.width/2.0
    #Y coordinate of the center = upper-left.y + height/2
    p.y = box.corner.y - box.height/2.0
    return p
print findCenter(box)
#This will not return the coordinates of the center, because when I return p
#it appears the id of it
#<__main__.Point instance at 0x0000000003EB9BC8>
#If I want to see the point I must the my printPoint function
center=findCenter(box)
#Center is receiving p
print printPoint(center)
#Now it is printing center that contains the value of p
#(50.0,-100.0)

print "----------------------------------------------"#Organazing
#*********************12.7*****************************
#************Objects are mutable***************

#We can change the values of the object
#Defining a function to grow my rectangel
def growRect(box, dwidth, dheight): #the recantangle, how much I want to grow.
    box.width= box.width+dwidth
    box.height= box.height+dheight
    return box.width, box.height
#Testcase
print growRect(box, 100, 100)
#(200.0, 300.0)

#Exercise
#Move the position of the rectange
def moveRect(box, dx, dy):
    #Move x in the corner dx units
    box.corner.x= box.corner.x + dx
    #Move y in the corner dy units
    box.corner.y= box.corner.y + dy
    #Returning the new values
    return box.corner.x, box.corner.y
print moveRect(box, 2, 3)
#(2.0,3.0)

print "----------------------------------------------"#Organazing
#*********************12.8*****************************
#************Copying***************
#Copying an object is often an alternative to aliasing
#import copy
import copy
#Making p1 be a point
p1=Point()
#Instantiate
p1.x=3
p1.y=4
p2=copy.copy(p1)
#Shallow equality
print p1==p2
#False
#Deep equality
print samePoint(p1,p2)
#True
#Same content but not the same object
#I can change p1 without worrying about p2.

#This is a SHALLOW COPY.
#For the rectangle, if I use the copy module, I could change the with and height
#and the copy would not change. But if I change x and y, it would change both.
#For DEEP COPY
b2=copy.deepcopy(box)
#Now b2 and box are completely separate objects.

#We can use deepcopy to rewrite a new rectangle and the grow it.
#Without changing my ond rectangle.
#First of all, I will create another rectangle
#Instantiate it.
Rect=Rectangle()
Rect.width=50.0
Rect.height=70.0
Rect.corner=Point()
Rect.corner.x=0.0
Rect.corner.y=0.0
#PURE FUNCTION
def growRectangle(box, width, height):
    #import copy (Don't need to import it again)
    Rectangle_copy=copy.deepcopy(box)
    Rectangle_copy.width = Rectangle_copy.width + width
    Rectangle_copy.height = Rectangle_copy.height + height
    return Rectangle_copy.width, Rectangle_copy.height
#Growing my new rectangle (Rect) by 100 in the width and 100 in the height
print growRectangle(Rect,100,100)
#(150.0, 170.0)
