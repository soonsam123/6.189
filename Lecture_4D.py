#Name: Soon Sam R. Santos
#Date: January 10, 2017
#Session: 6.189 Lecture 4 (Part D)
#Lecture_4D.py

#The subfunction will return a Boolean type, then the rps function
#will call the subfunction.
def valid_input(inp):
    if inp=='paper' or inp=='rock' or inp=='scissors':
        return True
    else:
        return False
#Now the function to play
def game(player1, player2):
    #If this condition is True it will keep playing
    if valid_input(player1) and valid_input(player2):
        if player1==player2:
            return "Tie"
        if (player1=='paper' and player2=='rock') or\
           (player1=='scissors' and player2=='papaer') or\
           (player1=='rock' and player2=='scissors'):
            return "Player 1 Wins!"
        else:
            return "Player 2 Wins!"
    else:
        print "OhoOw, Someone typed an Invalid Input!"

#Testing
print game('rock','paper') #Player 2 Wins!
print game('rock','scissors') #Player 1 Wins!
print game('scissors','scissors') #Tie
print game('scissor','rocke') #Invalid Input!
