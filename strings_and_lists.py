# Name: Soon Sam R Santos
# Section: Lecture 3 and 4. HomeWork 2
#Date: January 12, 2017
# strings_and_lists.py
import string
# **********  Exercise 2.7 **********
def sum_all(number_list):
    total=0
    #Passing through each number
    for num in number_list:
        #Storing each number into a variable that is the sum.
        total=total+num
    return total


# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])
print "---------------------------------------"
#WAYS TO CREATE A LIST
#1 --> list = [None]*10
#2 --> list = range(10)
#3 --> number_list=[1,2,3,4,5,6]
#test=[[] for i in number_list]
#print test -->Outputs [[], [], [], [], [], []] 
def cumulative_sum(number_list):
    # number_list is a list of numbers
    #One way to create an empty list with the quantity of terms of number_list - eth
    #zeros
    cumulative=[0]*len(number_list) #3 cumulative[3]
    i=0
    while i<len(number_list): #Loop with the size of the list
        #Storing to cumulative[2] the value of the previous (cumulative[1])
        #plus the value of the actual number_list[2]
        #In the first loop, when i=0. The cumulative[0-1]= cumulative[-1] will be
        #the last term of cumulative plus the first term of number_list
        #as the last term of cumulative is zero, this will not affect in the result
        #But, if it would affect in the result I could separated with an if statement
        cumulative[i]=cumulative[i-1]+number_list[i]
        i+=1
        #Returning the value of the new list.
    return cumulative
    
# Test Cases
print cumulative_sum([3,4,10]) #Should outputs [3,7,17]
print cumulative_sum([5,7,12]) #Should outputs [5,12,24]
print cumulative_sum([1,0,8])  #Should outputs [1,1,9]

# **********  Exercise 2.8 **********
#Defining the function
def report_card():
    #Asking how many classes he took and storing in quant
    quant=input("How many classes did you take?\n")
    i=0
    total=0
    #Creating one list for the names and other for the grades with the length of quant
    name=[None]*quant
    grade=[0]*quant
    #Loop to store the name and the frades in the list that I created
    while i<quant:
        name[i]=raw_input("What was the name of this class?\n")
        grade[i]=input("What was your grade in this class?\n")
        #Making the sum of all the grade
        total=total+grade[i]
        i+=1
    #Calculating the GPA
    GPA=float(total)/quant
    print 'REORT CARD:'
    i=0
    #Other loop to show the name and the grandes
    while i<quant:
        print name[i],"-->",grade[i]
        i+=1
    #Printing the overall GPA
    print "Overall GPA:", GPA
print "---------------------------------------"        
    
#There is a way to do this program without asking the user how many classes he took.    

# Test Cases
#print report_card()
#How many classes did you take?
#2
#What was the name of this class?
#Calculus
#What was your grade in this class?
#87
#what was the name of this class?
#Physics
#What was your grade in this class?
#98
#REPORT CARD:
#Calculus --> 87
#Physics --> 98
#Overall GPA: 92.5

# **********  Exercise 2.9 **********


VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    if word[0] in VOWELS:
        return word[:]+"hay"
    else:
        return word[1:]+word[0]+"ay"
    

# Test Cases
print pig_latin('boot') #Shoult outputs ootbay
print pig_latin('image') #Should outputs imagehay
print "---------------------------------------"

# **********  Exercise 2.10 **********
#******List Comprehensions*******
#>>>S=[x**2 for x in range(10)]
#>>>V=[2**i for i in range(13)]
#>>>M=[x for x in S if x%2==0]
#>>>
#>>>print S, V, M
#[0,1,4,9,16,25...]
#[1,2,4,8,16...]
#[0,4,16,36,64] The even numbers in S

#Calculating Prime numbers by using list comprehension
#First I calculate the nonprimes numbers between 1 to 50
nonprimes=[j for i in range(2,8) for j in range(i*2,50,i)]

#Second I take all the number from 1 to 50, but that are not in nonprimes
#Therefore they are prime numbers
primes=[x for x in range(50) if x not in nonprimes]
#In the end, I show them.
print primes

print "----------------------------------"

#Another example using strings
words='The quick brown fox jumps over the lazy guy'.split()
#Outputs the string transformed in a list.
print words
#I am storring in a list several lists that are the upper,lower and length
stuff=[[w.upper(),w.lower(),len(w)] for w in words]
#Outputting each term of my stuff list
for i in stuff:
    print i

#Doing the same thing with map and lambda

#Fist, I write map.
#Second, I use () instead of [].
#Third, I write inside the () lambda and the variable that will go through all the
    #terms in my listn, followed by collon. lambda w:
#Fourth, Inside the [] the output of each term in the list.
#Fifth, the list that I am going through.

print "Should output the same thing as above **************"

stuff=map(lambda w: [w.upper(),w.lower(),len(w)], words)
for i in stuff:
    print i

print "---------------------------------"

#Exercise 2.10 - (1)
#Defining the function
def cubes():
    #list comprehension from 1 to 10 that calculate the cube of each number
    list=[x**3 for x in range(1,11)]
    #Returning the list
    return list

#Exercise 2.10 - (2)
#Defining the function
      #def coin_flips():
           #list=[[h,t]]
       #INCOMPLETE
#Exercise 2.10 - (3)
#Defining the function
def vowels_phrase(phrase):
    #This time I included in the Vowels the upper and lower case characteres
    #instead of taking the phrase and passing to lower case characteres.
    VOWELS=['a','e','i','o','u','A','E','I','O','U']
    #Taking each letter of the phrase and analisyng if it is a vowel.
    list=[w for w in phrase if w in VOWELS]
    #Returning the vowels
    return list

# Test Cases
print cubes() #Parte 1
#Should outputs [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print "---------------------------------" #Separating exercises in the shell
print vowels_phrase('I am going to MIT') #Part 3
#Should outputs ['I', 'a', 'o', 'i', 'o', 'I']

print "---------------------------------"
# **********  Exercise OPT.1 **********
#Transforming a string into a list --> string.split()
#Trasnorming a list into a string --> list.join()
def phrase_latin():
    #Saying what the program will do
    '''
    This program will translate a phrase into Pig Latin
    Don't plug points, commas, dashs...
    Provide just letters and spaces please!
    '''
    phrase=raw_input("What phrase do you wish to translate?\n")
    #Thansforming the phrase into lower case characteres
    lower=phrase.lower()
    #Transforming the lower case phrase into a list
    word_list=lower.split()
    i=0
    #Creating a new list with [None] length of the word_list -eth times
    final_sentence=[None]*len(word_list)
    #Loop length of the list -eth times
    while i<len(word_list):
        #The new list will receive each term of word_list translated to PL
        final_sentence[i]=pig_latin(word_list[i])
        i+=1
    #Returning the new list with the join function to trasnform the list into
    #a string
    return string.join(final_sentence)

#Test Cases
print phrase_latin()
