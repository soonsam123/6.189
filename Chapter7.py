#Name: Soon Sam R. Santos
#Date: January 7, 2017
#Lecture 4

#*******How to think like a Computer Scientist************
#**********************Chapter 7**************************

#*************************7.1*****************************

name="SoonSam"
letter = name[1]
#It will outputs 'o' because the first letter is o
#S is the zero-eth letter
print letter
#It will outputs 'S'
letter= name[0]
print letter

print "--------------------------------------------------"
#*************************7.2*****************************

#The len function returns the number of characteres in a string
name="SoonSam"
length= len(name)
print length
#Outputs exactly the number of letters, not beginning with zero

#last=name[length]
#It will cause an ERROR, SoonSam has no 7th letter, the last is 6th
#since we start with zero.

#Outputs the last letter of the string
last=name[length-1]
print last

#Counting backward
print name[-1]  #Last Letter 'm'
print name[-2]
print name[-3]
print name[-4]
print name[-5]
print name[-6]
print name[-7]  #First Letter 'S'

#Notice that counting backwards I didn't start from zero

print "--------------------------------------------------"

#*************************7.3*****************************

#Loop to output all the letter, I need index to support because it starts
#as zero
index= 0
while index<len(name):  #Begin zero and finish [len(name) - 1]
    letter=name[index]
    print letter, '\t',
    index += 1

print "--------------------------------------------------"
    
#To print backwards is almost the same thing, but I start with 1.
i=1
while i<=len(name):
    letter2=name[-i]
    print '\n',letter2
    i+=1

print "--------------------------------------------------"

#I already had learned this, is the samething as the while loop, but it is
#much faster because it is a propertie of python
for char in name:
    print char

print "--------------------------------------------------"

#Using a python characteristic to print many similar names
prefixes= "JKLMNOPQ"
suffix= "ack"
suffix2= "uack"
for each_char in prefixes:
    if each_char=="O" or each_char=="Q":
        print each_char+suffix2
    print each_char+suffix
    
print "--------------------------------------------------"

#*************************7.4*****************************

#This variable[n:m] count from the nth letter to the (mth letter - 1)
#It still begin with zero-th
string="Soonsam, MIT, App"
print string[0:7]
print string[9:12]
print string[14:17]
#Omiting one of the numbers
print string[:3] #0th, 1th, 2th.
print string[3:] #3th, 4th, 5th ..., last one

print "--------------------------------------------------"

#*************************7.5*****************************

#The comparison operators work on strings.
word='apple'
if word!='banana':
    print "Yes, we have no bananas!"

#Putting in alphabetical order
if word<'banana':
    print word, "comes before banana"
elif word>'banana':
    print word, "comes after banana"
else:
    "Yes, we have no bananas!"

#Python organize first all the uppercase letters and then the lowercase
#Eventough Zebra is alphabetical latter than banana, it will outputs
#Zebra come before banana because of the uppercase letter.
a='Zebra'
if a<'banana':
    print a, "comes before banana"
elif a>'banana':
    print a, "comes after banana"
else:
    "Yes, we have no bananas!"

print "--------------------------------------------------"

#*************************7.6*****************************
#String are immutable

#greeting= "Hello, World!"
#greeting[0]= 'J'         #ERROR, I can't change strings
#print greeting

#Simple way to solve it: I can add letters but not change. Strings are immutable
greeting="Hello, World!"
newGreeting= 'J' + greeting[1:]
print newGreeting

print "--------------------------------------------------"

#*************************7.6*****************************

#Looking for a specific letter in a string. If find show the position
#else return -1
def find(string, ch):
    index=0
    while index<len(string):
        if string[index]== ch:
            return index + 1 #When return the function show and finish 
        index=index+1        #imediatelly
    return -1  #If theres is no such letter, show -1 and finish imediatelly
print "--------------------------------------------------"

#*************************7.7*****************************

#How many times the letter a appears in banana
fruit='banana'
count=0
for letter in fruit:
    if letter=='a':
        count=count+1
print count

print "--------------------------------------------------"

#*************************7.8*****************************
#Doing the same thing inside a function with while statement
def find(str, char):
    i=0
    count=0
    while i<len(str):
        if str[i]==char:
            count=count+1
        i=i+1
#Doing the same thing inside the function with a for loop(Smaller)        
def find(str, char):
    count=0
    for letter in str:
        if letter==char:
            count+=1
    print count
  
print "--------------------------------------------------"

#*************************7.9*****************************
#*****************The string module***********************

#Finding a letter in a string in a even much easer way
#Usind the import string
import string
fruit='banana'
place=string.find(fruit,'a') #Don't forget "string".find
print index  #Outputs 1, that is the second place in the string

#I can also do it
string.find("banana","na")
#Outputs 2, that is the third place in the string

string.find("banana","a",4) #the last number is where it should start looking
#Outputs 5

#Another way is a range
string.find("bob","b",1,2) #It doesn't include 2, therefore it will
#FAIL (-1)
print "--------------------------------------------------"

#*************************7.10*****************************
#*****************Character Classification*****************

print string.lowercase
#abcde....
print string.uppercase
#ABCDE....
print string.digits
#0123456789

#1 - Finding a lowercase letter in the string.lowercase
def isLower(ch):
    return string.find(string.lowercase, ch)!= -1
#Outputs True or False

#2 - Alternatively use a propetie of python.  The fastest one.
def isLower(ch):
    return ch in string.lowercase

#3 - A yet another alternatively. If between a and z, it is a lowercase
def isLower(ch):
    return 'a'<=ch<='z'

#test/ NOT WORKING
def isLower2(string, char):
    return string.find(string, char)!= -1
#Another constant defined in the string module
print string.whitespace

