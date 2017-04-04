#Name: Soon Sam R Santos
#Date: January 20, 2017
#Session: Lecture 5 - Chapter 10
#Chapter10.py

#*********************10*****************************
#***************Dictionaries*****************

#We learned strings, list, tuples. All of them use just integers as index.
#Dictionaries are similar them, except they can use any immutable type as an index.
#Let's create a dictionary to translate English-->Spanish

#To create an empty dictionary:
eng2sp={}
#Now My index is not an integer anymore. It is a string
#Don't forget the ''.
eng2sp['one']='uno'
eng2sp['two']='dos'
#In dictionaries the index are called key
#So the pair are key-values pairs
print eng2sp
#These are the key-value pairs
#{'two':'dos','one':'uno'}

#2 - There is a second way to create a dictionary
eng2sp={'one':'uno','two':'dos','three':'tres'}
print eng2sp
#Outputs {'three': 'tres', 'two': 'dos', 'one': 'uno'}
#They are not outputted in order, but we don't need to carry about it
#Since we call them by names
print eng2sp['two']

print "-------------------------------------------"#Organazing

#*********************10.1*****************************
#***************Dictionary Operations*****************

#The quantity of each fruit in a stock
inventory={'apples':412,'melon':317,'bananas':254,'pineapple':143}
#If the stock of melon finishs
#Use the function del
del inventory['melon']
print inventory
#Outputs {'pineapple': 143, 'apples': 412, 'bananas': 254}

#Or just add a new value
#Dictionaries are MUTABLES
inventory['melon']=0
print inventory
#Outputs {'melon': 0, 'pineapple': 143, 'apples': 412, 'bananas': 254}

#The function len also works here
print len(inventory) #4 --> Number of key-pairs values.

print "-------------------------------------------"#Organazing

#*********************10.2*****************************
#*****************Dictionary Methods*******************

#Instead of the function def keys(eng2sp), we use the method syntax eng2sp.keys()
print eng2sp.keys() #This outputs the keys of the dictionary
#['three','one','two']

#As we might except, the values also works
print eng2sp.values() #Thus outputs the values of the dictionary
#['tres', 'dos', 'uno']

#The third one return both, but not as a dictionary, it returns as a list tuples
print eng2sp.items()
#[('three', 'tres'), ('two', 'dos'), ('one', 'uno')]
#[] instead of {}, () in each key-value pair and , instead of :
#The () represents a list, the commas inside the parentheses represent tuples
#That's why it is a list of tuples

print eng2sp.has_key('one')  #Object(dictionary).has_key(what you want to find)
#True
print eng2sp.has_key('soon')
#False

print "-------------------------------------------"#Organazing

#*********************10.3*****************************
#*****************Aliasing and copying*******************

#Copying a dictionary
opposite={'up':'down','right':'wrong','true':'false'}
allias=opposite
#Now I have two dictionary that refer to the same object
copy=opposite.copy()
#Copy refer to the same object(but it is not the object, it is just a copy of the object)
#If I change allias, opposite also will change
allias['right']='left'
print opposite['right']
#'left'

#But if I change copy
copy['up']=15
print opposite['up']
#'down'
#I change copy, but opposite didn't change. As copy is equal to opposite, but it is
#not related to opposite

print "-------------------------------------------"#Organazing

#*********************10.4*****************************
#*******************Sparse matrices********************

#To represent marices with many zeros, it is not so useful to use lists
#Therefore we can represent it with dictionaries
matrix={(0,3):1,(2,1):2,(4,3):3}
#Key: Tuple (Where the element is)
#Value: integer
#The others spaces of the matrices are zero.
print matrix[2,1] #[] To call the element
#2

#To call a zero
print matrix.get((1,3),0) #First, row and column(Position of the element)
                          #Second, if there is nothing, return 0
#0
print matrix.get((0,3),0)
#1
print matrix.get((2,3),'Not in')
#As the second term, I can write something
print "-------------------------------------------"#Organazing

#*********************10.5*****************************
#*************************Hints************************

#I can store values into a dictionary, that have already been computed
#This is called hint
#Fibonacci numbers: 1,1,2,3,5,8,13,21... (2+3=5/ 3+5=8)
#This dictionary already contain the result of fibonacci(0) = 1 and fibonacci(1)=1
previous = {0:1, 1:1}
def fibonacci(n):
    #If i input fibonacci(0). previous.haskey(0) will output the value of the key 0
    #Because this is a value I already have in the dictionary, without doing any calculus
    #it would output the fibonacci(0) value of 1
    if previous.has_key(n):
        return previous[n]
    #If there is not, I would need to calculate it
    else:
        #The newValue is the previous value plus the ante previous value.
        #RECURSION!!!
        newValue = fibonacci(n-1) + fibonacci(n-2)
        #My previous dictionary will store one more value, to don't need to calculate
        #it again. previous[10]=valuee...
        previous[n] = newValue
        #I show the value
        return newValue
print fibonacci(50)
#20365011074L / L is meaning that it is a long integer member
#My shell didn't outputed the L, maybe because it is a new version and now they can
#output long integers

print "-------------------------------------------"#Organazing

#*********************10.6*****************************
#********************Long integers*********************

print type(1L)
#<type 'long'>

#To create a long.
#1 - Write with L (1L, 3L, 57L)
#2 - Use the long function (long(1), long(3.9), long('57'))
print long(1)
#1L
print long(3.9)
#3L
print long('57')
#57L
#It is not outputing like this in my shell. Probably they uploaded it in the last version

print "-------------------------------------------"#Organazing

#*********************10.7*****************************
#*******************Couting letters********************

#There is a very gentle way to do a histogram with dictionaries.
#First, I create an empty dictionary that will receive:
#Key: the letter
#Value: The quantity of times it appears
letterCount={}
#I will pass through all the letters in Mississippi
for letter in 'Mississippi':
    #My dictionary will store the letter as key.
    #Then it will look it how many letters is already in the dictionary
    #If there is none, it returns 0
    #In the end, it adds 1
    letterCount[letter]= letterCount.get(letter, 0) + 1
print letterCount
#{'i': 4, 'p': 2, 's': 4, 'M': 1}

#There is a way to put it in alphabetic order
#First I will take all the items.
letterItems=letterCount.items()
#[('i', 4), ('p', 2), ('s', 4), ('M', 1)]
#It creates a list of tuples
letterItems.sort()
#In the list of tuples I can use sort to order the letter in alphabetic.
print letterItems

