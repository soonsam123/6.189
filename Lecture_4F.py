#Name: Soon Sam R. Santos
#Date: January 10, 2017
#Session: 6.189 Lecture 4 (Part F)
#Lecture_4F.py

#While/else.
#Here is a possible implementation, but it is buggy.
#Counting down positive numbers
n=input("Enter a nonnegative number")
while n>=0:
    print n
    n-=1
else:
    print "You've failed to enter a nonnegative number."
#If a print -1. It will not pass in the while statement becuase -1>=0 is not True.
#So it would go to the else and Fail.
#However, If I input a 1 for n. The program would output:
#1
#0
#You've failed to enter a nonnegative number.
#That is because the loop exited normally; when n=-1 the while is False and
#then it goes to the else and print the error message.
#How to fix it ?
n=input("Enter a nonnegative number")
if n<0:
    print "You've failed to enter a nonnegative number."
while n>=0:
    print n
    n-=1
###

# Just to mention, loops can also be exited via 'break' statements or
# exceptions, which we covered briefly in Lecture 4 and you can read about 
# in the textbook. If a loop were exited because of these, the 'else' block
# would not execute since the loop was not terminated normally.

# For what it's worth, I don't ever use 'while/else' blocks, so this
# isn't even an issue for me; there are always ways to get around them.
