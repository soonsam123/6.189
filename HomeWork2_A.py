# Name: Soon Sam R Santos
# Section: Lecture 3 and 4
# hw2.py
import math
import random
##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1
#input: f1(3)
#Output: 4
#input: print f1(3)
#Output: 4
    #    None
#input: print f1(3) + 1
#Output: 4
    #    ERROR...
def f2(x):
    return x + 1
#input: f2(3)
#Output: 4
#input: print f2(3)
#Output: 4
#input: print f1(3) + 1
#Output: 5

#In java they use a lot of print. In python we will use a lot of returns
#and the prints will be used only to give information to the user or for
#debugging

# **********  Exercise 2.1 ********** 

# Define your function here
#I will create a list with the valid inputs for the user
VALID_INPUTS=['rock','paper','scissors']
#Creating a list for the winning comobos of the user.
#In this list [0][0], [1][0], [2][0] wins. The first wins.
WINNING_COMBOS=[['paper','rock'],['rock','scissors'],['scissors','paper']]
#Defining the function
def rps(player1,player2):
    #Testing if the choices are permitted. If the choice is not in the VALID_
    #INPUTS list, it is not permitted. I use .lower() in case the player
    #type upper case characteres I will use it all throughout the exercise
    if player1.lower() not in VALID_INPUTS:
        return 'Invalid input, "rock", "paper", and "scissors are permitted, You got:'+str(player1)
    if player2.lower() not in VALID_INPUTS:
        return 'Invalid input, "rock", "paper", and "scissors are permitted, You got:'+str(player2)
    #Using the list of winning combos to see if player 1 won.
    if [player1.lower(),player2.lower()] in WINNING_COMBOS:
        return "Player 1 Wins!" #Return that player 1 won
    #Testing if the choices are the same
    elif player1.lower()==player2.lower():
        return "Tie Game" #If they are I return Tie 
    #Making the same thing with the Winning combos, but for player 2
    elif [player2.lower(),player1.lower()] in WINNING_COMBOS:
        return "Player 2 Wins!" #Returning Player 2 Won
    #I included all the other possibilities. The exercises shouldn't get here.
    else:
        return "Shouldn't get here"
    
# Test Cases for Exercise 2.1
print rps('rock','rock') #Tie Game
print rps('rock','scissors') #Player 1 Wins!
print rps('ROck','papeR') #Player 2 Wins!
print rps('rockete','paper') #Invalid Inputs
# ********** Exercise 2.2 ********** 
print "-------------------------------------------------"
#Separating the exercises in the shell
# Define is_divisible function here
def is_divisible(m,n):
    #If the remainder of m by n is zero. m is divisible by n so i return True
    if m%n==0:
        return True
    #Otherwise it is false
    else:
        return False

# Test cases for is_divisible
print is_divisible(3,1) #Must be True
print is_divisible(4,5) #Must be False
print is_divisible(15,5) #Must be True
print is_divisible(5,15) #Must be False

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # ERROR. Integer division or modulo by zero

print "-------------------------------------------------"
# Define not_equal function here
def not_equal(m,n):
    #If m==n both variables are equal
    if m==n:
        return m,"is equal to",n
    #Otherwise they are not equal. This is the same to say they are different
    else:
        return m,"!=",n

# Test cases for not_equal
print not_equal(3,3) # This should return "3 is equal to 3"
print not_equal(4,7) # This should return "4 != 7"
print not_equal(10,100) # This should return "10 != 100"
print "-------------------------------------------------"
# ********** Exercise 2.3 ********** 

## 1 - multadd function
def multadd(a,b,c):
    ## 2 - Equations
    angle_test=math.sin(math.pi/4)+(math.cos(math.pi/4)/2)
    ceiling_test=math.ceil(276/19)+ (2*math.log(12,7))
    print "sin(pi/4)+cos(pi/4)/2 is:",angle_test
    print "ceiling(276/19)+2log_7(12) is:",ceiling_test

## 3 - yikes function
#def yikes(x):
    

# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********
## 1 - rand_divis_3 function

def rand_divis_3():
    #Randon function to selec a random number
    x=random.randint(0,100) #Range from 0 to 100. Both Inclusive.
    print x #Priting the random number
    if x%3==0: #Checking if it is divisible by 3
        return True #If yes return True
    else:
        return False #If not return False

# Test Cases
print rand_divis_3()
print rand_divis_3()
print rand_divis_3()
print rand_divis_3()
print "-----------------------------------------"

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(numsides, numdie):
    #Starting a while statemenet to do numdie-eth times
    i=0
    while i<numdie:
        print random.randint(1,numsides) #The random go from 1(minimum value of the die
        #to numsides(maximum value of the die.
        i+=1 #Making the loop turn again.
# Test Cases
print roll_dice(6,3)
print roll_dice(5,2)
print roll_dice(10,17)
print "-----------------------------------------"
# ********** Exercise 2.5 **********
#COMPLEX NUMBERS: Are represented by a + bi. In python they are represented
#by a + bj. Therefore if I calculate (3+5j)+(7+5j) python will give me the result
#(10+10j). It will also calculate if i multiply, divide or subtract.
#If I store the value in a variable as 'a=4.5 + 7j
#I can take the use this 'a.real= 4.5' 'a.imag=7j'
#To creat a complex number --> complex(R,I)
#Complex(4,3) = 4+3j
#Complex(3) = 3j
# code for roots function
def roots(a,b,c): #a, b, and c in the quadratic equation
    if ((b**2)-(4*a*c))<0: #if delta<0 it will compute the complex roots
        #The first complex root will take as the real part -b and as the complex
        #part the square root of - delta. (Because the math module don't compute
        #square root of negative numbers.
        #Then after all of this, it will divide by 2*a the complex numbers
        x1=complex(-b,math.sqrt(-((b**2)-(4*a*c))))/(2*a)
        #I plug a minuts sinal between the real and the complex number
        #To show the second root.
        x2=complex(-b,-math.sqrt(-((b**2)-(4*a*c))))/(2*a)
        return x1,x2 #Returning the values
    else:
        #IF it is not complex, it is easy!
        #I just plug bhaskara equation with the appropriate parentheses
        #to calculate the roots
        x1= ((-b) + math.sqrt((b**2)-(4*a*c)))/(2*a)
        x2= ((-b) - math.sqrt((b**2)-(4*a*c)))/(2*a)
        return x1,x2 #Returning the roots
# Test Cases
print roots(1,2,-1)
print roots(1,-5,6)
print roots(4,-3,1)
