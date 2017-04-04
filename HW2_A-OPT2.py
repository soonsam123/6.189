#Name: Soon Sam R Santos
#Session: Lecture 4 - Homework 2 - OPT.2
#Date: January 17, 2017
#HW2_A-OPT2.py
import math
#What isinstance does.
#isinstance(object,type) --> bool(True or False)
#Example : isinstance(13,int) --> True
#isinstance(soon,int) --> False

#Part 1
#Defining the function
#This lists will contain elements of different types, as int, float and str.
def integers(lists):
    #This new list will contain 'all' the elements of the old list, but just if
    #they are int. By using the isinstance statement
    new_list=[x for x in lists if isinstance(x,int)==True]
    #Returning the new list.
    return new_list
#Test Case
print integers([13,5,7,8.6,7.4,'son','sam'])#Should outputs [13,5,7]

print "--------------------------------------" #Separating functions

#Part 2
#y=(x**2)+1
#My list will receive
#[x,y] in the domain of x [-5,5]
#But just if it is in the range of y [0,10]
#(-5,6) Because I want to include 5.
equation=[[x,(x**2)+1] for x in range(-5,6) if (x**2)+1 in range(10)]
print equation

print "--------------------------------------" #Separating functions

#Part 3
#Circle of radius 5 --> (x**2) + (y**2) = 25
#Solving for x.
#Printing [x,y] OBS= I am not writing y, I am writing the value of y
#Printing this for the domain of x
#In this time I don't need to restrict the range of y because no value of y gets
#smaller than 0 or greater than 10.
circle=[[x,math.sqrt(25-(x**2))] for x in range(-5,6)]
print circle
print "----------------------------------------------"
#Part 4
#Prime numbers
def primenumber(x):
    ct=0
    j=1
    while j<=x:
        if x%j==0:
            ct=ct+1
        j+=1
    if ct==2:
        return "Prime number"
    else:
        return "This is not a prime number"
#**************************************************
#The x will be a list of numbers
def prime(lista):
    newlist=[0]*len(lista)
    i=0
    for num in lista:
        j=1
        ct=0
        while j<=num:
            if num%j==0:
                ct+=1
            j+=1
        if ct==2:
            newlist[i]=num
            i+=1
    x=0
    while x<len(newlist):
        if newlist[i]==0:
            newlist[i]==15
        else:
            newlist[i]=newlist[i]
        x+=1
    print newlist
#Test Case
print prime([3,4,5,6,7])
#**************************************************
#My program will receive a list of numbers and will output
#The even numbers
#The odd numbers
#The prime numbers

#Explaining how the user should input his numbers
print "Add a comma between the numbers"
print "For example: 3,4,5,6,7
#Asking for the list of numbers
list=input("Write your list of numbers:\n")
#Using list comprehension to put all the even numbers inside another list
evenlist=[num for num in list if num%2==0]
#Using list comprehension to put all odd numbers inside another list
oddlist=[num for num in list if num%2!=0]
#Using list comprehension to put all prime numbers inside another list
primelist=[num for num in list if num not in [j for i in range(2,8) for j in range(i*2,50,i)]]
#Outputting all the new lists
print evenlist
print oddlist
print primelist
