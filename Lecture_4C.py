#Name: Soon Sam R. Santos
#Date: January 10, 2017
#Session: 6.189 Lecture 4 (Part C)
#Lecture_4C.py
             ## Examples of List Comprehensions in Python

###
print "Example 1: Make a list of letter derivate by a string"
print [letter for letter in "Hello, World!"]

###
print "\nExample 2: Add an exclametion point to every letter"
print [letter+'!' for letter in "Hello,World!"]

###
print "\nExample 3: A multiplication table for the 9's"
print [9*num for num in range(11)]
print "\nExample 4: A multiplication table for 17"
print [17*num for num in range(11)]

###
print "\nExample 5: Make a list of letter in a string if they're not 'o'"
print [letter for letter in "Hello, World!" if letter!='o']

###
print "----------------------------------------------------"
#Practicing January 21, 2017
#Prime numbers
#Numbers divisibles by 2, 3, 5, 7. Except themselves
nonprimes=[j for i in [2,3,5,7] for j in range(2*i,100,i)]
primes=[x for x in range(2,100) if x not in nonprimes]
print primes
#Until now, the most useful factor for list comprehension for me.
