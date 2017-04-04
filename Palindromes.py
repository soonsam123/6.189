# Name: Soon Sam R Santos
# Date: January 25, 2017
# Session: Homework 3
# Palindromes.py

def is_palindrome(string):
    #From the first to the last term of the string must be equal to from the last to the
    #first.
    #Three variables to help me.
    i=1 #To count backwards
    j=0 #To count frontwards
    c= 0 #Help to check if all the letters were equal
    #In case the user inputed AnnAbeELLA. Turn into lower case letters
    new_string=string.lower()
    while i<=len(string): #Loop with the length of the string
        if new_string[j]== new_string[-i]: #If the string last element is equal to
            #the first, the before the last element is equal to the second and so forward.
            #I will count a letter.
            c = c + 1
        #i will begin as 1 and finish as 7 (to count from -1 to -7 [backwards])
        i = i + 1
        #j will begin as 0 and finish as 6. (to count from 0 to 6 [frontwards]) 
        j = j + 1
    #If c is equal to the length of the string, it means all the letters
    #backwards and frotwards are equal.
    if c == len(string):
        return "Palindrome"
    else:
        #If not, It is not a palindrome.
        return "NOTT!!!"
print is_palindrome('soonsam') #NOTT
print is_palindrome('YUMmy') #NOTT
print is_palindrome('AnNa') #Palindrome
