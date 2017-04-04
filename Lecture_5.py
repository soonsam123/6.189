#Name: Soon Sam R Santos
#Date: January 20, 2017
#Session: Lecture 5 
#Lecture_5.py

#Tuples are imutables. ()
#Tuples     /   Lists
#imutables  /   mutables
#parentheses/   brackets
new_tuple=(5,6,7,8)
print "new_tuple is:", new_tuple
#(new_tuple is: 5,6,7,8)

#Indexing tuples
print "new_tuple[0] is:", new_tuple[0]
#new_tuple[0] is: 5

#And iterate through them:
for item in new_tuple:
    print item
#5
#6
#7
#8

for item in new_tuple:
    print item,
#5 6 7 8

#Show how long they are
print "\n", len(new_tuple)
#4

#And iterate through indicies
#The index goes from 0 to 3.
for index in range(len(new_tuple)):
    print "Index is:", index
    print "Value at that index is:", new_tuple[index]

#IMMUTABLES
#for index in range(len(new_tuple)):
#    new_tuple[index]=0 #Error

#Unpacking a tuple
#I reverse the side, The left side is receiving the variables from the right side
#(a,b,c,d)=(5,6,7,8)
(a,b,c,d)=new_tuple
print "a is:", a #5
print "b is:", b #6
print "c is:", c #7
print "d is:", d #8
#Make sure there is the same number of variables and terms.
#Now I am changing the value of b
b=77
new_tuple=(a,b,c,d)
#As tuples are imutables, the b that is 77 will not receive the value of 6.
#Therefore it will keep being 77
print new_tuple
#(5, 77, 7, 8)
