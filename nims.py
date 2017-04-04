# Name: Soon Sam R Santos
# Section: Lecture 3 and 4. Homework 2 A Exercise 2.6
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    while pile>0:
        #Asking the quantity of stones player 1 want to take
        player1=input("1 - How many stones do you want to take?\n")

        #INVALID INPUTS
        #Check first of all if the value inputed is permitted
        #OBS: ''1>player1>max_stones'' is not working. I needed to separeted.
        while (type(player1)!=int or player1<1 or player1>max_stones
               or player1>pile): #Invalid input
            #If not, I'll ask again
            player1=input("1 - How many stones do you want to take?\n")#Re-ask
            #This loop will just finish when he input a permitted value
        #Then he counts down the stones in the pile
        pile=pile-player1
        #And print the pile so the user can see how many stones are left
        print "There are:",pile,"stones left"
        if pile==0:
            return "Player1 Won!"
        #Asking the quantity of stones player 2 want to take
        player2=input("2 - How many stones do you want to take?\n")
        #INVALID INPUTS
        #Check first of all if the value inputed is permitted
        while (type(player2)!=int or player2<1 or player2>max_stones
               or player2>pile): #Invalid input
            #If not, I'll ask again
            player2=input("2 - How many stones do you want to take?\n")#Re-ask
            #This loop just finish when he input a permitted value
        #The he counts down the stones in the pile    
        pile=pile-player2
        #And print the pile, so the user can see how many stones are left
        print "There are:",pile,"stones left"
        if pile==0:
            return "Player2 Won!"
    print "Game over"

