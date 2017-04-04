#Name: Soon Sam R Santos
#Date: January 20, 2017
#Session: Lecture 5
#Mistakes.py

#Difference between variables and values.

some_list=[1,3,6,7]
print 3 in some_list
#True
print 5 in some_list
#False
print 5 not in some_list
#True
print [3] in some_list
#False
#This last example is False because 3 is a number, and it is in some_list
#[3] is a list and it is not in some_list

#Boolean types
#Return True / not Return 'True'
#Boolean type/ string

#Return exits the function immediately

def is_prime(num):
    for divisor in range(2,num):
        #If there is just one number between 2 and the (number - 1) that is
        #divisible, I already return false. I don't need to check the others
        #The program will imediately stop.
        if (num%divisor)==0:
            return False
    #If it didn't do the previous
        #The code will get until here and I will return True
    return True
print "-----------------------------------------------------"
# is and ==. is not and !=
a=[1,2]
b=[1,2]
#Now a is b
c=a
#Now as is not b anymore
#b is c.
print a is b
#False
print a is c
#True
print b is c
#False
#They all have the same value, but they are not the other
#Imagine three people with 70kg. They have the same weight, but they are not
#the same person
print a, b, c

#Division bt integer and float
x=7
print 1/x #integer
print 1.0/x #float
print 1/float(x) #float
