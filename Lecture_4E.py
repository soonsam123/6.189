#Name: Soon Sam R. Santos
#Date: January 10, 2017
#Session: 6.189 Lecture 4 (Part E)
#Lecture_4E.py

#This is the list to valid the inputs
VALID_OPTIONS=['rock','paper','scissors']
#This is the list of wining combos, the first is the winner
WINNING_COMBOS=[['rock','scissors'],['paper','rock'],['scissors','paper']]

#Defining the function to play rps
def rps(player1,player2):
    #player1.lower() turn all the upper case letter into lower
    #in is used to see if the word is in the list
    #not in is used for the opposite
    if player1.lower() not in VALID_OPTIONS:
        return "Invalid Input! It must be 'rock','paper' or 'scissors' You got:"+str(player1)
    if player2.lower() not in VALID_OPTIONS:
        return "Invalid input!  It must be 'rock','paper' or 'scissors' You got:"+str(player2)
    
    if player1.lower()==player2.lower():
        return "Tie game"
    elif [player1.lower(),player2.lower()] in WINNING_COMBOS:
        return "Player 1 Wins!"
    elif [player2.lower(),player1.lower()] in WINNING_COMBOS:
        return "Player 2 Wins!"
    else:
        return "I already covered everything"
    #It shouldn't get here.
    
#Testing
print rps('rock','rock') #Tie game
print rps('rock','scissors') #Player 1 Wins!
print rps('ROCK','paper') #Player 2 Wins!
print rps('rocket','scissorse') #Invalid Input

#I must use .lower() in every case, because if he inputs some uppercase charactere
#I need to transform it into lower case to evaluate in in the VALID_OPTIONS and
#in the WINNING_COMBOS
