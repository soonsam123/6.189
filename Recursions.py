#Name: Soon Sam R Santos
#Date: January 21, 2017
#Session: Lecture 5
#Recursions.py

#My function will receive a list.
def itsum(list):
    result=0
    #Going through all the elements in itsum.
    for i in list:
        #Storing the values in the result.
        result= result + i
    #This'll be the sum of all the elements in the list.
    return result

#Now I will use RECURSIVE DEFINITION to make the same thing as above
def rec_sum(a_list):
    if a_list==[]:
        return 0
    else:
        #Return the first element of the list plus the sum of all the others
        #For the second element it will come back in the function and will
        #Add the first with the second, then for the thrid it will add
        #the sum of the first and the second to the third, until it get
        #to the last element
        return a_list[0] + rec_sum(a_list[1:])
#It is RECURSIVE because it calls it self
#Note, this is permitted and is very useful
#It is the same thing for the fibonacci numbers
#First, let's call a dictionary to store the first 2 elements of fibonacci
storing_results={0:1,1:1}
def fibonacci(n):
    #I'll check if my result is already in the storing_results
    if storing_results.has_key(n):
        #If there is, I'll return my dictionary value in the key [n]
        #The key[n] is the number the user inputed, what'll output is the
        #fibonacci result
        return storing_results[n]
    #else, I'll need to do the calculus
    else:
        #I'll use recursion to do this calculus
        #Look, I'll already store this value in my dictionary
        #For example, storing_results[10]=the value of the fibonacci number
        #                   The last number plus the last last number
        #storing results[2]=fibonacci(1) + fibonacci(0)
        #In order to calculate fibonacci 1 and 2, it'll go again to the function
        #And will exercute in the first if statement, because the values are in the
        #dictionary.
        storing_results[n]= fibonacci(n-1) + fibonacci(n-2)
        return storing_results[n]
        #e.g = Now I have the value of fibonacci(2) in my dictionary
        #I dont need anymore to calculate it.
#But, if the user type a big number like 20. The function will go back and forward
#Many times, taking and storing the results, until it get to 20.
#It is very useful, because all the fibonacci numbers less than 20
#Will be already in my dictionary.
#Look how it is efficienty
    
print fibonacci(30)
#1346269
print storing_results
#{0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13, 7: 21, 8: 34, 9: 55, 10: 89, 11: 144,
#12: 233, 13: 377, 14: 610, 15: 987, 16: 1597, 17: 2584, 18: 4181, 19: 6765, 20:
#10946, 21: 17711, 22: 28657, 23: 46368, 24: 75025, 25: 121393, 26: 196418,
#27: 317811, 28: 514229, 29: 832040, 30: 1346269}
#As I called 30, the values of 29,28,27,26 all were not in my dictionary
#Therefore the function needed to go back all througout this numbers until it get
#to the values of 1 and 0 and start to calculate.
#To calculate fibonacci 30 I must calculate all the previous fibonacci.
#Very useful because my dictionary'll be already with all these values.
#I don't need to calculate it anymore.
#Recursion and Dictionary to make my function pretty much stronger 
