#Name: Soon Sam R Santos
#Date: January 18, 2017
#Session: Lecture 5 - Chapter 9
#Chapter9.py
import random
#*********************9.1*****************************
#***************Mutability and tuples*****************

#Recalling:
#1 - Strings are imutables    2 - Lists are mutable
#There is a third one: Tuple and they are imutable.

#I take them separeted by commas and between parenthses (Optional)
tuple= ('a','b','c','d','e')

#To put just one element I still need the comman
tuple = ('a',)
print type(tuple)
#<type 'tuple'>

tuple1=('a')
print type(tuple1)
#<type 'str'>

#The slice occurs in the same way
print tuple[1:3]
#('b','c')

print "-----------------------------------------------" #Organazing

#*********************9.2*****************************
#***************Tuple assignment*****************
a,b,c,d=1,2,3,4
print a #1
print b #2
print c #3
print d #4

a,b=b,a #a and b exchange their values
print a #2
print b #1

print "-----------------------------------------------" #Organazing

#*********************9.3*****************************
#***************Tuples as return values*****************

def swap(x,y):
    return y,x
# a,b=swap(a,b)
# a<--y / b<--x. Changing the values of a and b
def swap1(x,y):   #swap(a,b)
    x,y=y,x     #x<--a/ y<--b // x<--y/ y<--x
                #I am not changing the values of a and b as above
                #I am just changing the values of x and y.

print "-----------------------------------------------" #Organazing

#*********************9.4*****************************
#***************Random numbers*****************

#import random. In the beginning of the program

#This random function will print float random numbers between 0.0 and 1.0
#This for loop is just to do the samething 10 times
for i in range(10):
    x=random.random()
    print x

print "-----------------------------------------------" #Organazing

#As an exercise, generate a random number between low and high


print "-----------------------------------------------" #Organazing

#*********************9.5*****************************
#***************List of random numbers*****************
def list_randoms(n): #A function that receive the length
    s=[0]*n  #Create a list of n zeros
    for i in range(n): #Doing it n times
        #The list receive a random number between 0.0 and 1.
        s[i]=random.random()
    return s #Returning the whole list

print "-----------------------------------------------" #Organazing

#*********************9.6*****************************
#*********************Counting************************
#Counting the quantity of numbers between low and high
#I had a similar program in section 7.8 which counted the quantity of a specific
#letter in a string, I can reuse the programs to save time.
def inBucket(t, low, high): #list, lower values, higher value
    count = 0
    for num in t: #Passing through all the numbers in t.
        if low < num < high: #Checking whether the number is between low and high
            count = count + 1 #Counting if it is
    return count #Returning the quantity of numbers between low and high

print "-----------------------------------------------" #Organazing

#*********************9.6 and 9.7*****************************
#*********************Counting and Many Buckets************************

#bucket1 = inBucket(a, 0.0, 0.25)
#bucket2 = inBucket(a, 0.25, 0.5)
#bucket3 = inBucket(a, 0.5, 0.75)
#bucket4 = inBucket(a, 0.75, 1.0)
numBuckets=8   #Doing the same thing as above in a general way
bucketWidth=1.0/numBuckets #Determine the width of each range
#Example: numBuckets=4  bucketWidth=0.25
for i in range(numBuckets): #For [0,1,2,3] in range(4)
    low=i*bucketWidth  #0*0.25=0 / 1*0.25=0.25/ 2*0.25=0.5/ 3*0.25=0.75
    high=low+bucketWidth #0+0.25=0.25 / 0.25+0.25= 0.5 / 0.5+0.25=0.75/ 0.75+0.25=1.0
    print low,"to",high
    
print "-----------------------------------------------" #Organazing
#Determining the same length for the bucket
numBuckets=8
buckets=[0]*numBuckets #Creating a new list with 8 zeros
bucketWidth=1.0/numBuckets#Determining the width of my range
for i in range(numBuckets): #Doing the same thing 8 times
    low=i*bucketWidth #My low value at the first time will be 0
    #Then it will be the bucketWidth one time, then two times, then third times
    high=low+bucketWidth#The high value will be just the low plus the width
    #Each term of my list will receive the quantity of terms between low and high
    #By using my function above inBucket
    buckets[i]=inBucket(list_randoms(1000),low,high)
print buckets

print "-----------------------------------------------" #Organazing

#*************************9.8*******************************
#******************A Single-pass solution*******************

#Previous problem, multiply i by bucketWirdth to find the lower value. Now we want
#To take a value between 0.0 and 1.0 and see the index it falls.
#A list with 8 numbers between the values of the bucketsWidths
t=[0.123,0.0,0.564,0.435,0.524,0.75,0.75,0.01]
numBuckets=8
buckets=[0]*numBuckets
#i will pass throught my list t
for i in t:
    #The index is the lower integer of i times 8.
    index=int(i*numBuckets) #lower integer (i*8)
    #The buckets in the index= index will receive the quantity of terms + 1
    buckets[index]=buckets[index]+1
print buckets

#HISTOGRAM: A list of integers in which each element counts the number of
#times something happens.
    
