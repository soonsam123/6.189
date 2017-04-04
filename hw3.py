
# Name: Soon Sam R Santos
# Section: Lecture 5 - Homework 3
# hw3.py
import math
##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 
#From now on, we will use functions take take parameters instead of asking the user
#for input. Unless the exercise tell you to do so.
# Define your function here
def list_intersection(list1,list2):
    #List comprehensions are amazing, I was dong it in 20 lines and it was not
    #working. When I need to create a new_list, but I don't know how long it will
    #be, the best way is to work with list comprehensions.
    
    #The new_list will receive all the numbers in list, but only if they belong also
    #to the list2.
    new_list=[num for num in list1 if num in list2]
    return new_list

# Test Cases for Exercise 3.1
print list_intersection([1,2,3,4,5],[4,5,6,7,8,9,10])
print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 3], [3, 3, 3, 2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])
print "--------------------------------------" #Organazing
# **********  Exercise 3.2 **********

# Define your function here
#import math (in the beginning) I need this for calculus
def ball_collide(ball1, ball2): #These are two tuples ball1=(x,y,r) and ball2=(x,y,r)
    #The distance between two points according to algebra.
    d= math.sqrt(((ball1[0] - ball2[0])**2)+((ball1[1] - ball2[1])**2))
    #Calculate the sum of the radius.
    sum_R= ball1[2] + ball2[2]
    #If the distance is less than the sum of the radius
    #They are colliding.
    #Otherwise, they are not.
    if d<=sum_R:
        return True
    else:
        return False

# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True
print "--------------------------------------" #Organazing
# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {'18.01':'Single Variable Calculus','18.02':'Multivariable Calculus'\
              , '6.189': 'Introduction to Python', '6.01':\
              'Introduction to EE and CS'}

def add_class(class_num, desc):
    #My_classes in the key of class_num is receiving the value of desc
    my_classes[class_num]=desc

# Here, use add_class to add the classes you're taking next term
add_class('6.02', 'Introduction to EE and CS II')
add_class('6.042','Mathematics for Computer Science')
add_class('18.06','Linear Algebra')
def print_classes(course):
    new_dic={}
    #I will check if my one of my keys begins with the number 'course'
    #Storing just the keys into an object
    keys= my_classes.keys()
    #Now keys is a list of the keys.
    #I will pass throughout the terms in keys
    for terms in keys:
        #And see if the first letter of this keys begin with the number
        #the user typed.
        if terms[0]==course:
            #If so, I store it in my new dictionary.
            new_dic[terms]= my_classes[terms]
    #And I show it.
    show_keys = new_dic.keys()
    show_values = new_dic.values()
    i=0
    while i<len(show_keys):
        print show_keys[i], "-->", show_values[i]
        i=i+1
      

# Test Cases for Exercise 3.3
print "Classes of course 6: "
print print_classes('6')
print "Classes of course 6: "
print print_classes('1')
print "Classes of course 9: "
print print_classes('9')

print 
# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

print "--------------------------------------" #Organazing

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    #I will go throughout the list of names and store each name as a key
    #and each age as a value.
    #OBS: I will not plug the ages as keys, because the dictionary would recognize
    #both 18 as the same key, and it would have a dictionarie with less key-values
    #pairs than I would expect.
    i=0
    for names in l1:
        #comb_dict[each age] = l1 from position 0 to 11.
        comb_dict[names]= l2[i]
        i+=1
    return comb_dict

combined_dict = combine_lists(NAMES, AGES) #New dictionary with all the names and
                                           #ages.

def people(age): #Function will receive an age.
    #Storing the items of the dictionary into a list of tuples
    #the first term will be the key and the second will be the value.
    list_Tuples= combined_dict.items()
    #new_list <-- The first term of the tuple for i from 0 to 11 in list of tuples
    #only if the second term is equal to the age.
    new_list=[list_Tuples[i][0] for i in range(12) if list_Tuples[i][1]==age]
    return new_list
#When I need to create a new_list but I don't know what its length will be
#the best way until now is to use list comprehension!! DONT FORGET!!!            
# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []
print "--------------------------------------" #Organazing
# **********  Exercise 3.5 **********
#1. Use a dictionary to map between the month and its numerical value
#2. You can use either a list or dictionary to convert the final output of the algortihm
#to the day of the week.
#3. Make sure you handle the following three points correctly.
#Task 1
month_dic={'march':1,'april':2,'may':3,'june':4,'july':5,'august':6,
       'september':7,'october':8,'november':9,'december':10,'january':11,
       'february':12}
#Defining my function
def zellers(month, day, year):
    #Reducing to lower case letter. In case the usar input something like --> MARch
    #A is the month as a number. So A will be the value of my dictionary in the key
    #month_lower
    month_lower= month.lower()
    A = month_dic[month_lower]
    #B is day as a number
    B = day
    #C is the last two digits of the year
    #Converting year to a string to take just the last two digits
    #and then trasnforming it into an integer again
    C= int(str(year)[2:])
    #If the user typed January or February I'll need to use the preceding year
    if A==11 or A==12:
        C = C - 1
    #D will be the first two digits of year

    D= int(str(year)[:2])

    #Operations
    W = (13*A - 1) / 5
    X = C / 4
    Y = D / 4
    Z = W + X + Y + B + C - (2*D)
    R = Z%7 
    if R<0:
        R = R + 7
    day_Week={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',
              6:'Saturday'}
    return day_Week[R]

# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday" # This should be True
print zellers("January",25,2017) #Today, should output Wednesday
