#Name: Soon Sam
#Date: Dec 31, 2016
#Session: lecture 2
#rps.py

#           ************Exercise 1.8***************

#*****Part1*****
#I did the for loop to take the numbers 2,3,4 until (11-1)=10
#As the results are decimals, I must use 1.0 to get float results
for num in range(2,11):
    print (1.0/num)
#*****Part2*****
#I will ask to type integer number, because non integer number will
#not reah zero

number=input("Type an integer number: ")
#this condition is to see if the number is positive
if number>=0:  #if it is positive the program will keep working here
    if number==int(number): #Another condition to see if the number
        while number>=0:    #is an integer
            print number
            number-=1
            #counting down until 0
    else:   #if the number is not integer, I choosed to not work on it
        print "non integer"
#This is if the number is negative
elif number<0:
    while number<=0:
        print number
        number+=1
        #Basically it is the same thing, however, I need to add 1
        #instead of subtract 1. (E.g. (-9)+1= -8
                                 #     (-8)+1= -7
                                 #     (-7)+1= -6.....
#*****Part3*****
                                 
#Asking for the base and for the exponential
base=input("Type the base: ")
exp=input("Type the exponential: ")

#I will do the base**exp and then I will follow with base**(exp+1),
#base**(exp+2).... until base**(exp+9)

for count in range(0,10):  #count will be the numbers I will add
                           #the exponential (1,2,3...9)
    print base, "to the",exp+count,"th =", base**(exp+count)
#Writing what the exercise will show (E.G = 2 to the 2 th = 4)

#*****Part4*****

#Ask to type the even number    
n=input("Please, type a number that is divisible by 2: ")

#Condition if the number is even. If the remainder is 0, so the number is
#even
if n%2==0:
    print "Thank you, Congratulations!!" #Finish

#if he type an odd number
else:
    while n%2!=0: #create a loop to test if the number is even or odd
                  #while it is odd, I will not finish the program
        print "This is not divisible by 2" #Warning it is not even
        #Ask for another number and replace the new number in 'n'
        n=input("Please, type a number that is divisible by 2: ")

#He got out of the loop only if he had typed an even number, so I say
#Congratulations
print "Thank you, Congratulations!!"

