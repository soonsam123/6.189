#Lecture 1 - B
#raw_input_example(me).py
#Soon Sam R Santos
#Dec 29, 2016
# Use raw_input to receive letters.
name= raw_input("What is your name? ")
city= raw_input("What city do you live in? ")
state= raw_input("What State is that in? ")
print "Hello there! It is so great to meet you,"
#First way, separated lines.
print name
print city
print state
#Second way, in the same line by using commas.
print name,"from", city, state
# Use input to receive numbers, int or float.
age= input("Pardon my rudeness, but how old are you? ")
#int(argument) forces the argument to be an integer by rounding.
print "Wow! You look like could be", int(age - (0.15*age)),"!!"
            
