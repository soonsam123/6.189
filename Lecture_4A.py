#Name: Soon Sam R. Santos
#Date: January 10, 2017
#Session: 6.189 Lecture 4 (Part A)
#Lecture_4A.py

#Defining a string
new_string='Hi Class!'
#We can go throug the letter in the string
for letter in new_string:
    print letter

#We can concatenate two strings together
a='Hi'
b='Class!'
#No space
print a+b
#Extra space
print a,b
#With comma I can plug different types.
print a,2,b,4.76

#We can index the string
print "news_string[0] is", new_string[0]
#Slice it
print "From the first to the third character:", new_string[0:3]
#Out puts the first letter of the string 'H'

#We can get the length of the string using the len function
print "The length of the string is:", len(new_string)
#And use various string methods on it
print "The string in upper characteres is:", new_string.upper()
print "The string in lower characteres is:", new_string.lower()

#It doesn't matter whether you type your email in gmail with upper or lower
#case letters. Probably they do it.
string=raw_input("Write your Email: ")
Lstring=string.lower()
Ustring=string.upper()
print Lstring, Ustring
