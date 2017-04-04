#Boolean
#While True means a loop forever
#The program will run until the end and then will come back to ask again
while True:
    number=input("Please enter a number: ")
    is_prime= True
    #[2, number - 1] - If never is divisble it is prime
    for factor in range(2,int(number**0.5)+1):
        if number%factor==0:
            is_prime=False
            break

    if is_prime==True:
        print "This is a prime number"
    else:
        print "This is not a prime number"
