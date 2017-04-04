#Name: Soon Sam R. Santos
#Date: January 8, 2017
#Session: 6.189 Lecture 4 (Chapter 8)
#Chapter8.py

#*******************8.1*************************
#*******************List Values*************************
#A list can stroe strings, integers, nothing or float numbers
vocabulary=["Soon Sam", "MIT", "App"]
numbers=[4,14]
empty=[]
print vocabulary, numbers, empty

print "--------------------------------------------------"

#*******************8.3*************************
#*******************List Values*************************
#Going through each elements in the list
horsemen=["war", "famine", "pestilence", "death"]
i=0
while i<len(horsemen): #As in the strings we can use len
    print horsemen[i] #As in the strings [] to capture each element
    i+=1
print "--------------------------------------------------"
#Exercise
list=['spam!',1,['Brie','Roquefort','Pol le Veque'],[1,2,3]]
#j=0
#while j<len(list):
#    Length_each=len(list[j])
#    print Length_each
#    j+=1

#*******************8.4*************************
#*******************Membership*************************
#Testing if the value is inside the list
#'Brie' in list = True.
#1 in list = True.
#"soonsam" not in list = True

#*******************8.5*************************
#*******************For Loop*************************
#As 7.3, it also works here
for elements in list:
    print elements
#For numbers
for numbers in range(10):
    if numbers%2==0:
        print numbers, "is even"
print "--------------------------------------------------"

#*******************8.6*************************
#concatenating lists
a=[1,2,3]
b=[4,5,6]
c=a+b
print c
#Works for * too.
print "--------------------------------------------------"

#*******************8.6*************************
#Slices in Section 7 also works here
list2=['a','b','c','d','e','f']
print list2[1:3]
#Outputs ['b', 'c'] From 1 to 2
print list2[:4]
#Outputs ['a','b','c','d'] from 0 to 3
print list2[3:]
#Outputs ['d','e','f'] from 3 to the last
print list2[:]
#Outputs the whole list--> print list2[:]==print list2
print "--------------------------------------------------"

#*******************8.8*************************
#*******************Lists are Mutable*************************
#When working with range I must use the brackets []
#When I am working just with one element in the list, I just input the letter
#without the brackets []
# Replace another element
list1=['a','b','c','d','e','f']
list1[0]='b'
print list1
#Outputs ['b','b','c','d','e','f']

#Replace a range of elements
list2=['a','b','c','d','e','f']
list2[1:4]=['x','y','z']
print list2
#Outputs ['a','x','y','z','e','f']

#Remove one element
list3=['a','b','c','d','e','f']
list3[1:3]=[]
print list3
#Outputs ['a','c','d','e','f']

#Add elements
list4=['a','b','c','d','e','f']
list4[1:1]=['j','k']
print list4
#Outputs ['a','j','k','c','d','e','f']
print "--------------------------------------------------"

#*******************8.9*************************
#*******************DEL*************************
#An easier way to delete elements from a list
list5=['a','b','c','d','e','f']
del list5[1:4]
print list5
#Outputs ['a','e','f']
print "--------------------------------------------------"

#*******************8.10*************************
#*******************Objects and Values*************************
a="banana"
b="banana"
print id(a)
print id(b)
#Out puts: 63172976
#          63172976
#It is the same string for a and b
c=[1,2,3]
d=[1,2,3]
print id(c)
print id(d)
#Outputs: 69846024
#         56906632
#Lists work different from string, now we have one list for each variable
#although they are located in different places, they have the same value
print "--------------------------------------------------"

#*******************8.11*************************
#*******************Aliasing*************************
a=[1,2,3]
b=a
print id(a)
print id(b)
#In this case they have the same output: 63227144
#                                        63227144
#Now we have just one list for both variables
b[0]=5
print a
#Outputs [5,2,3]. One is influencing in the another

print "--------------------------------------------------"

#*******************8.12*************************
#*******************Cloning lists*************************
#To avoid the mistake above we can clone the lists
a=[1,2,3]
b=a[:]
#b receives the whole string a, using the brackets make it clone the list
#different from the example above
print b  #This is the cloned list
#Outputs [1,2,3]
#Now I can make changes in b without worrying about a
b[0]=4
print b
print a

print "--------------------------------------------------"

#*******************8.13*************************
#*******************List parameters*************************
#An list as a parameters (argument)
def Head(list):
    print list[0]
def DeleteHead(list):
    del list[0]
    print list

print "--------------------------------------------------"

#*******************8.14*************************
#*******************Nested lists*************************
lists=['Hello,World!',1,2.0,[10,20]]
#[10,20 is the nested list. To take the first element of it we can do 2steps
#First
lists2=lists[3]
print lists2[0]
#Second
print lists[3][0]

print "--------------------------------------------------"

#*******************8.15*************************
#*******************Matrices*************************
#Nested lists is a way to represent matrices
# A matriz 3x3
Matrix=[[1,2,3],[4,5,6],[7,8,9]]
#To take a the first row of the matriz
print Matrix[0]
#Outputs [1,2,3]
#And to take a single element of the matrix
print Matrix[0][0]
#Outputs 1  (Without brackets)

print "--------------------------------------------------"

#*******************8.16*************************
#*******************String and lists*************************
#Importing the string module
import string
#Creating a string
promisse='Soon Sam will get into MIT'
#Transforming the string into a list by using the string module(split)
print string.split(promisse)
#Outputs ['Soon', 'Sam', 'will', 'get', 'into', 'MIT']

#Another way is to use a delimeter instead of the whitespace
print string.split(promisse,'o')
#Outputs ['S', '', 'n Sam will get int', ' MIT']
#The delimeter doesn't appear in the list.

#The join function is the opposite. list --> strings
list=['Soon', 'Sam', 'will', 'get', 'into', 'MIT']
print string.join(list)
#Outputs Soon Sam will get into MIT
#I add the delimeter I want too.
print string.join(list, '_')
#Outputs Soon_Sam_will_get_into_MIT

#Example
#string.split will break the string into a list.
#string.join will take the list and transform in a string.
print string.join(string.split(promisse))
#let's see if this is equal to promisse
if string.join(string.split(promisse))==promisse:
    print True  #I can use return just inside functions(def)
#Outputs True.
