#Name: Soon Sam R Santos
#Date: January 4, 2017
#Session: Lecture 2
#zellers.py

#Showing what the program will do
print "This program will output the day of the week,"
print "for any date your provide"

name=raw_input("Enter your full name: ")

#Teaching how to input the month by numbers
print "\nThe month of the year should be given by numbers"
print "Following the sequence bellow"
print "1 - March"
print "2 - April"
print "3 - May"
print "........"
print "11 - January"
print "12 - February"

A=input("Enter the month of the year: ")

B=input("\nEnter the date of the month: ")
print "\nWrite the first two numbers of the year"
print "Example--> 19 for the year 1989"

#Instead of asking the year and the century
#I prefered to ask the firt two numbers and then
#The last two numbers of the year

D=input("Enter the first two numbers: ")
print "\nWrite jut the final two numbers of the year"
print "Example--> Year=89 for the year 1989"

C=input("Enter the year: ")

#If the month is January or February I will take the
#preceding year righ here
if A==11 or A==12:
    C-=1

#The formulas to calculate R
W=(13*A - 1)/5
X=C/4
Y=D/4
Z=W+X+Y+B+C - 2*D
R=Z%7

#Printing the name of the user
print "\n",name,",\n"

#If the month is 11 or 12 it would show the precedng date
#Therefore I created this if to add 1 to the year showed
if A==11 or A==12:
    print A,"/",B,"/",D,C+1
#Otherwise, just show the year    
else:
    print A,"/",B,"/",D,C 

#Sequences of if to show the date of the week
#Being 0=Sunday and 6=Saturday
if R==0:
    print "will be SUNDAY"
if R==1:
    print "will be MONDAY"
if R==2:
    print "will be TUESDAY"
if R==3:
    print "will be WEDNESDAY"
if R==4:
    print "will be THURSDAY"
if R==5:
    print "will be FRIDAY"
if R==6:
    print "will be SATURDAY"
