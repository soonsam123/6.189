#Name: Soon Sam R Santos
#Date: January 23, 2017
#Session: Lecture 6 - Chapter 14
#Chapter14.py

#*********************14*****************************
#***************Classes and methods*****************

#*********************14.1*****************************
#************Object-oriented features***************
#Python is a object-oriented programming language because it provides ways to
#work with object-oriented programming.
#OBJECT-ORIENTED PROGRAMMING:
#1 - Programs are made up of object definitions and function definitions, and most
#of the computation is expressed in terms of operations and object.
#2 - Each object definition corresponds to some object or concept in the real world,
#and the functions that operate on that object correspond to the ways real-world
#objects interact.
#We didn't use Python supported object-oriented programming, they are used
#to do the same thing as we already did but in a more concise and more accurately
#way.

#Methods are associated with a class and is intended to be invoked on instances of
#that class.

#Methods are just like functions, with two differences:
#1 - Methods are defined inside a class definition in order to make the relation-
#ship between the class and the method explicit.
#2 - The syntax for invoking a method is different from the syntax for calling a
#function
class Time:
    def printTime(time):
        print str(time.hours)+":"+\
              str(time.minutes)+":"+\
              str(time.seconds)
#Note the difference?
#Opposite to the chapter 13, printTime is now inside class, so I have a method,
#instead of a function.
#Instantiate
#Making my object be a class time.
currentTime=Time()
#Giving the values
currentTime.hours= 9
currentTime.minutes= 54
currentTime.seconds= 11
#Calling my method is different from calling the function: printTime(currentTime)
print currentTime.printTime()
#Self: the first element that is the object
#Followed by a dot it comes the method.

print "----------------------------------------------"#Organazing

#*********************14.3*****************************
#************Another Example***************
#I just need to do it once in the beginning of the problem, after import.
#However, I am doing it more than once to learn.
class Time:
        #PURE FUNCTION (PURE METHOD)
        def printTime(time):
            print str(time.hours)+":"+\
                  str(time.minutes)+":"+\
                  str(time.seconds)
        #MODIFIER
        def increment(self,seconds):
            self.seconds= seconds + self.seconds
            while self.seconds>=60:
                self.seconds= self.seconds - 60
                self.minutes= self.minutes + 1
            while self.minutes>=60:
                self.minutes= self.minutes - 60
                self.hours= self.hours + 1
            return self.printTime()
        #convertToSeconds now as a method. PURE METHOD
        def convertToSeconds(time):
            minutes= time.hours*60 + minutes
            seconds= minutes*60 + time.seconds
            return seconds
currentTime=Time()
#Giving the values
currentTime.hours= 9
currentTime.minutes= 54
currentTime.seconds= 11
#Calling in a different way. Self: the object. Inside() the second parameter.
print currentTime.increment(500)

print "----------------------------------------------"#Organazing

#*********************14.4*****************************
#************A more complicated example***************

class Time:
        #PURE FUNCTION (PURE METHOD)
        def printTime(time):
            print str(time.hours)+":"+\
                  str(time.minutes)+":"+\
                  str(time.seconds)
        #MODIFIER
        def increment(self,seconds):
            self.seconds= seconds + self.seconds
            while self.seconds>=60:
                self.seconds= self.seconds - 60
                self.minutes= self.minutes + 1
            while self.minutes>=60:
                self.minutes= self.minutes - 60
                self.hours= self.hours + 1
            return self.printTime()
        #convertToSeconds now as a method. PURE METHOD
        def convertToSeconds(time):
            minutes= time.hours*60 + minutes
            seconds= minutes*60 + time.seconds
            return seconds
        def after(self,time2):
            if self.hours > time2.hours:
                return 1
            if self.hours < time2.hours:
                return 0
            if self.minutes > time2.minutes:
                return 1
            if self.minutes < time2.minutes:
                return 0
            if self.seconds > time2.seconds:
                return 1
            return 0
#If the donetime comes after the currentTime, than the bread is not done yet
#if doneTime.after(currentTime):
#    print "The bread is not done yet."

print "----------------------------------------------"#Organazing

#*********************14.5*****************************
#************Optional Arguments***************
#A function to find a letter in a string starting from a point
def find(string, char, start=0):
    #The third argument is optional because a default value of 0 was provided.
    #It will begin where the user choosed
    index= start
    while index< len(string):
        if string[index]==char:
            return index
        index = index + 1
    return -1
#A function to find a letter in a string between the position the user input
def findbe(string, char, start, end):
    #It will begin where the user choosed
    index= start
    #The range I will look for, just between the values from start to end.
    while index< end:
        if string[index]==char:
            return index
        index = index + 1
    return -1

print "----------------------------------------------"#Organazing

#*********************14.6*****************************
#************The initialization method***************

class Time:
        #PURE FUNCTION (PURE METHOD)
        def printTime(time):
            print str(time.hours)+":"+\
                  str(time.minutes)+":"+\
                  str(time.seconds)
        #MODIFIER
        def increment(self,seconds):
            self.seconds= seconds + self.seconds
            while self.seconds>=60:
                self.seconds= self.seconds - 60
                self.minutes= self.minutes + 1
            while self.minutes>=60:
                self.minutes= self.minutes - 60
                self.hours= self.hours + 1
            return self.printTime()
        #convertToSeconds now as a method. PURE METHOD
        def convertToSeconds(time):
            minutes= time.hours*60 + minutes
            seconds= minutes*60 + time.seconds
            return seconds
        def after(self,time2):
            if self.hours > time2.hours:
                return 1
            if self.hours < time2.hours:
                return 0
            if self.minutes > time2.minutes:
                return 1
            if self.minutes < time2.minutes:
                return 0
            if self.seconds > time2.seconds:
                return 1
            return 0
        
        #INITIALIZATION METHOD
        #If the user doesn't input, the default value will be 0 for all of them.
        def __init__(self, hours=0, minutes=0, seconds=0):
            self.hours= hours
            self.minutes= minutes
            self.seconds= seconds
#When we invoke the Time constructor, the arguments we provide are passed along
#to init.
#This is much easir than Instantiate
#I am going to the Class Time and putting the three arguments
currentTime=Time(9,14,30)        
#I don't need to write init. Note, I write self outside the parentheses and the
#others inside the parentheses.
print currentTime.printTime()
#9:14:30
#We can omit any of the arguments because they are optional
currentTime= Time(seconds=30,hours=9)
print currentTime.printTime()
#9:0:30
#It doesn't need to be ordered if I plug the name and the equal signal.

print "----------------------------------------------"#Organazing

#*********************14.7*****************************
#************Points revisited***************
#Rewriting the class point from chapter 12
class Point:
    #With __init__ I don't need to do self=Point() to recognize that self is
    #a class Point
    def __init__(self, x=0, y=0): #__initialization__ will not work
        self.x= x
        self.y= y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
#Instead of instantiating
p = Point(3,4)
#I am going to the class Point and inputting the arguments.
#p is the self
print str(p)
#It must be str, otherwise it will not work.
#Therefore, these are properties of python that I can work with. (str and init)

#We almost always use __init__ and __str__ for writing a new class.

print "----------------------------------------------"#Organazing

#*********************14.8*****************************
#************Operator overloading***************

#To overrride the addition operator +, we provide a method named __add__.
class Point:
    #With __init__ I don't need to do self=Point() to recognize that self is
    #a class Point
    def __init__(self, x=0, y=0): #__initialization__ will not work
        self.x= x
        self.y= y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    #To overrride the addition operator +, we provide a method named __add__.
    def __add__(self, other):
        #Returning making the result became another point
        return Point(self.x+ other.x, self.y + other.y)

    #Trying sub
    def __sub__(self, other):
        #Returning making the result became another point
        return Point(self.x - other.x, self.y - other.y)

    #Trying mul
    def __mul__(self, other):
        #Returning making the result became another point]
        #DOT PRODUCT (OUTPUTS A INTEGER)
        return (self.x * other.x) + (self.y * other.y)
    #Python invokes __rmul__ for scalar multiplication
    #SCALAR PRODUCT (OUTPUTS AN POINT)
    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)
p1 = Point(3,4)
p2 = Point(5,7)
#Using the __init__ propertie of Python to make my life easier
p3 = p1 + p2
#p1.__add__(p2)
#Python will see '+' and will invoke __add__
print p3
#(8,11)

#Trying to use __sub__ to see if it will overload the '-' operator.
p4 = p1 - p2
#p1.__sub__(p2)
print p4
#(-2,-3)
#As we would might expect, it worked.

#For multiplication. __mul__ or __rmul__
p1= Point(3,4)
p2=Point(5,7)
print p1*p2
#43
print 2*p2 #The order matters here
#(10,14)
#p2*2 will not work. For __mul__, Python takes 2 as the second argument

print "----------------------------------------------"#Organazing

#*********************14.9*****************************
#************Polymorphism***************
class Point:
    #With __init__ I don't need to do self=Point() to recognize that self is
    #a class Point
    def __init__(self, x=0, y=0): #__initialization__ will not work
        self.x= x
        self.y= y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    #To overrride the addition operator +, we provide a method named __add__.
    def __add__(self, other):
        #Returning making the result became another point
        return Point(self.x+ other.x, self.y + other.y)

    #Trying sub
    def __sub__(self, other):
        #Returning making the result became another point
        return Point(self.x - other.x, self.y - other.y)

    #Trying mul
    def __mul__(self, other):
        #Returning making the result became another point
        return (self.x * other.x) + (self.y * other.y)
    #Python invokes __rmul__ for scalar multiplication
    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)
    def multadd(x,y,z):
        return x*y + z
    
    #Adding the function reverse
    def reverse(self):
        self.x, self.y = self.y, self.x
        
    def frontAndBack(front):
        import copy
        #Do a copy to don't change my front list
        back = copy.copy(front)
        #This reverse the list.
        back.reverse()
        return str(front)+str(back)

#Receiving the points
p1= Point(3,4)
p2= Point(5,7)
#print multadd(3,2,1)
#7
#We can use it for points also
#print multadd(2,p1,p2)
#(2*p1) + p2
#rmul (6,8) + p2 = p1.__add__(p2)
#(11,15)
#print multadd(p1,p2,1)
#(p1*p2) + 1
#(Cross product, 15+28 + 1 = 44

#POLYMORPHIC: A function that can take arguments with different types.

#Method frontAndBack which prints a list twice, forward and backward.
#Method frontAndBack which prints a list twice, forward and backward.
    #Receiving a list
#As a function
def frontAndBack11(front):
    import copy
    #Do a copy to don't change my front list
    back = copy.copy(front)
    #This reverse the list.
    back.reverse()
    return str(front)+str(back)

myList=[1,2,3,4]
print frontAndBack11(myList)
#[1, 2, 3, 4][4, 3, 2, 1]

#If all of the operations inside the function can be applied to the type, the
#function can be applied to the type.
#The operations in the method include copy, reverse and print
#copy works for any object, I already did __str__. It remains only reverse.
#Add the function reverse to the point
p = Point(3,4)
