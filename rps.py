#Name: Soon Sam
#Date: Dec 31, 2016
#Session: lecture 2
#rps.py

#Let's show the players what they are going to play
print "\t\tLet's play rock, paper and scissors game"
print "Please!! Do not type any capitalized letter" #I'll ask for it,
#because if the first type Rock and the second rock it won't tie.

print "You can choose: "   #Show the options the have
print " -> rock;"
print " -> paper;"
print " -> scissors."

#Receive the option of each player

player1=raw_input("Player 1: ")
#Here I will eliminate the possibilitie of the player1 to type something
#different from rock, paper and scissors at the same time.
if player1!="rock" and player1!="scissors"\
   and player1!="paper":
    print "This is not a valid object selection, Please restart the game"
    
player2=raw_input("Player 2: ")
#Here I will eliminate the possibilitie of the player1 to type something
#different from rock, paper and scissors at the same time.
#I did it for player 1 and 2 to finish the program as soon as the player
#type something that is not permitted
if player2!="rock" and player2!="scissors"\
   and player2!="paper":
    print "This is not a valid object selection, Please restart the game"

#With this condition I kill all the three Ties. rock==rock, scissors=scissors
#and paper==paper
if player1==player2:
    print "Tie"

#Let's fix player 1 as scissors and plug with the two possibilities for
#player2 (rock. paper)
elif player1=="scissors":
    if player2=="paper":
        print "Player1 Wins!!! Congratulations!!"
    elif player2=="rock":
        print "Player2 Wins!!! Congratulations!!"

#Let's fix player 1 as paper and plug with the two possibilities for
#player2 (rock, scissors)
elif player1=="paper":
    if player2=="rock":
        print "Player1 Wins!!! Congratulations!!"
    elif player2=="scissors":
        print "Player2 Wins!!! Congratulations!!"

#Let's fix player 1 as scissors and plug with the two possibilities for
#player2 (scissors, paper)
elif player1=="rock":
    if player2=="scissors":
        print "Player1 Wins!!! Congratulations!!"
    if player2=="paper":
        print "Player2 Wins!!! Congratulations!!"
