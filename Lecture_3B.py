#Name: Soon Sam R. Santos
#Date: January 8, 2017
#Session: 6.189 Lecture 3 (Part B)
#Lecture_3B.py

#def to begin the function definition
def is_a_party(apples, pizzas):
    #See if you have the quantity of food to do a party
    if apples>10 and pizzas>10:
        return True  #Breaks immediately and shows True
    else:
        return False #Breaks immediately and shows False
#A function withou parameters
def party():
    num_apples=input("How many apples do you have? \n")
    num_pizzas=input("How many pizzas do you have? \n")
    #OBS:This is not recursion, I am calling a function, but it is another
    #function. To be recursion I would need to call party itself
    if is_a_party(num_apples,num_pizzas): #If it is true, it will work
        return "Yeah! Let's do a party"   #And return this message
    else:  #This else executes if the condition is false.
        A=11-num_apples
        B=11-num_pizzas
        print "You still need to buy:",A,"Apples and",B,"Pizzas"
        return "Oww noo, Go to the store!"
    
#Testing the functions
print is_a_party(20,20)
print is_a_party(5,12)
print is_a_party(17,7)
print is_a_party(15,13)

print party()
