#Trying to calcula the prime numbers from 1 to 50
#I will calculate all the nonprime numbers from 1 to 50
#Thus I will tell you the numbers that are not in my nonprime numbers list
#How to discover the nonprime numbers between 1 to 50?
#I just need to see all the number between 1 to 50 that are divisible
#by 2,3,5,7 (excepted by 2,3,5,7)
#If they are divisible by this numbers, they are not prime numbers.
#I can write all the numbers that are divisible by 2 in a way
#2 + 2k
#Divisibles by 3
#3 + 3k
#Divisibles by 5
#5 + 5k
#Divisibles by 7
#7 + 7k
#As i don't want to take 2,3,5,7. I will just take the next numbers so
#Instead I will take 4,6,10,14. (2*2,3*2,5*2,7*2)
#Now I already have all the nonprime numbers between 1 to 50
#I just need to plug it into lines of code in Python.
nonprime=[j for i in range(2,8) for j in range(i*2,50,i)]
#Fist, let's discuss about i*2
#My program would count from 2 to 50 by a space of 2, it would be perfect
#but 2 is a prime numbers and I don't want to include it, thus to exclud the 2
#I will take the next number that is 4. By multiplying 2 by 2.
#That is why I am using i*2, In the next one I will have 3 to 50 by a space of 3
#but as it is i*2, I will do the same thing beginning from 3 and so excluding 6

#Second, Now my j range in taking all the numbers between 1 to 50 that are
#divisible by 2,3,4,5,6,7.

#Third, My i range is going from 2 to 7, but I would like to do it just for
#2,3,5,7. As it is not possible, I include also 4 and 6 in my range,
#They will not disturb anything, they'll just includ some more numbers.

#Now I have a complete list of all the numbers between 1 to 50 that are
#divisible by 2,3,4,5,6,7. This means that they are not prime numbers.

#All the numbers that are not in the list, are prime numbers from 1 to 50.
#Therefore

prime=[num for num in range(2,50) if num not in nonprime]

#(2,50) I don't want to include 0 nor 1.

#When I print the prime numbers list it will show all the prime numbers from
#1 to 50.

print prime

print "-------------------------------------------------"

#Look, there is a thing in the program above that I did without necessity
#It was to calculate the numbers that are divisible by 4, (8,12,16,20..)
#It was a waste of time, since they are already inside the divisibles by 2
#I also calculate the numbers that are divisible by 6, (12,18,24,30..)
#It was another waste of time, since they are also already inside the
#divisibles by 2.

#I can esclude this wast of time and make my program run quickly
#Do less work than before.

#By going not from 2 to 8, but just through the list which contain 2,3,5,7

nonprime=[j for i in [2,3,5,7] for j in range(i*2,50,i)]
prime=[num for num in range(2,50) if num not in nonprime]
#The nonprime are not the same as above, because here I do not repeat
#the numbers as much as in the example above.
print nonprime
print prime

#In the end, I calculate all the numbers divisible by 2,3,5,7 between
#1 and 50 and I calculate all the prime numbers between 1 and 50 in just 4 lines
