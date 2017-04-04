# Name: Soon Sam R Santos
# Date: January 26, 2017
# Session: Lecture 8
# Chapter16.py

#CHAPTER 15
import random
class Card:
    suitList = ['Clubs','Diamonds','Hearts','Spades']
    rankList = ['narf','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (self.rankList[self.rank] + "of" +
                self.suitList[self.suit])
    def __cmp__(self,other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0
class Deck:
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
    def printDeck(self):
        for card in self.cards:
            print card
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " "*i + str(self.cards[i]) + "\n"
        return s
    def shuffle(self):
        nCards= len(self.cards)
        for i in range(nCards):
            j = random.randrange(0,nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    def removeCard(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
    def popCard(self):
        return self.cards.pop()
    def isEmpty(self):
        return (len(self.cards)==0)
    def deal(self, hands, nCards=999):
        nHands = len(hands) #quantity of people in the game.
        for i in range(nCards): #Loop from 0 to the quantity of cards I will deal.
            if self.isEmpty(): break #If the deck is empty break.
            card = self.popCard()    #Take off the top card.
            hand = hands [i%nHands]  #Whose turn is next? 0,1,2,3,0,1,2,3,0,1,2,3,0...
            hand.addCard(card)       #Adding the top card to this hand.
        
#**********************Chapter 16*********************
#**********************Inheritance********************

#**********************16.1***************************
#*******************Inheritance***********************
#INHERITANCE: The ability to define a new class that is a modifier version of an
#existing class.
#1 - Add new methods to a class without modifying the existing class.
#2 - New class inherits all of the methods of the existing class.
#3 - Existing class: Parent class / New Class: Child or subclass.
#4 - Facilitate code reuse.
#5 - Can make programs difficult to read.
#Just use if the natural structure of the program tells you to do so.
#GOAL: Card Game OLDMAID. Write code that could be reused to implement other card games.

#**********************16.2***************************
#*******************A hand of cards***********************
#The name of the parent class appears in the parentheses. This means that all the methods
#from Deck were taken to use in Hand.
#Hand: Child / Deck: parent
class Hand(Deck):
    #The initialization will receive the name of the player and the cards
    #the name is optional as I inputed a default value with an empty string
    def __init__(self, name=''):
        self.name= name
        self.cards= []
    #Adding a card.
    def addCard(self,card):
        self.cards.append(card)
    #I don't need to def the method remove card because it is already in
    #the Deck methods.

#**********************16.3***************************
#*******************Dealing cards***********************
#I want now to deal cards from the deck into the hands.
#I will take three arguments: the deck I will take off cards.
#The hands I'll plug in cards, and the quantity of cards I will take off for all hands.
#hands is a list.

#**********************16.4***************************
#*******************Printing a Hand***********************
#We can already use our __str__ module and printDeck in Deck to print the hand.
#Uncomment to execute
        
#deck= Deck()           #Creatinh the deck with 52 cards.
#deck.shuffle()         #Shuffling the deck.
#hand = Hand("SoonSam") #Creating a empty hand.
#deck.deal([hand],5)    #Distribuindo 5 cards to one hand.
#print hand             #hand is a class and I will take advantage off the __str__

#module in the deck to print each term of the hand. 
#If I modify something in the __str__ module of deck this would output.
#<__main__.Hand instance at 0x0000000003C9D348>
#because it would be showing the class. But with the __str__ module, this class
#is going directly to Deck class and going into the __str__ method and executing
#each hand.cards[0,1,2,3,4] for priting by using the str module from class Card:
#If i change the __str__ module from Card it will output.
#<__main__.Card instance at 0x000000000365B608>
# <__main__.Card instance at 0x0000000003659548>
#  <__main__.Card instance at 0x000000000365D4C8>
#   <__main__.Card instance at 0x000000000365BF08>
#    <__main__.Card instance at 0x0000000003659348>
#Because it would be still executing the __str__ module from deck hand[0,1,2,3,4]
#but it would just output the place of the classes because it doesn't have the str
#module to translate what the classes mean.

#By changing the __str__ module from deck. It would output the place of class 'hand'
#By changing the __str__ module from class. It would output the place
#of each card in hand.

#To show additional informtion we will create an additional method __str__ in Hand
#that will overrides the existing methods in deck.
        
    def __str__(self):   #The hand I am working with.
        s = "Hand " + self.name
        if self.isEmpty(): #If it is empty.
            return s + " is empty\n"
        else:  #If it is not empty.
            #invoking the __str__ method from Deck class on self(any hand).
            return s + " contains \n" + Deck.__str__(self)

#**********************16.5***************************
#*******************The CardGame class***********************

class CardGame:
    #As common games I take the deck and shuffle it.
    def __init__(self):
        self.deck = Deck()  #Creating a deck to the game.
        self.deck.shuffle() #Just shuffling the deck
#The Rules of the Game:
#1 - Goal: Get rid of all cards in your hand by matching card by rank and color.
#2 - Queen of Clubs is exclude in the beginning of the game so Queen of Spades has no match.
#3 - The 51 remaiders cards are dealt to the players in a round robin(once).
#4 - Players match the cards they have in their hands and discard them.
#5 - The game begins.
#6 - Each player picks a card (without looking) from the left player who has cards.
    #If it matches, he take off the pair.
        #If not, he will have one more card in his hand.
            #Eventually,ArithmeticError all possibles matches are made.
                #the loser's hand will have the Queen of Spades.

#**********************16.6***************************
#*******************OldMaidHand class***********************
#A new class that takes as his child Hand.
class OldMaidHand(Hand):
    #The method that is the rule of the game to remove cards.
    def removeMatches(self):  #From each hand.
        count = 0
        #Making a copy, so we can traversse it and remove cards from the original.
        originalCards = self.cards[:]   #originalCards'll be a list with the cards in
        #hand.
        for card in originalCards: #Going through each card in hand.
            match = Card(3 - card.suit, card.rank)
            #The match'll have the same rank and the same color. 3 - card.suit turns
            #Clubs into Spades, and Hearts into Diamonds. The opposite also works.
            if match in self.cards:
            #self.cards is changing while originalCards is not. If self.cards
            #has the match card, that is 4 of Spades turned into a 4 of Clubs.
            #Now they are comparing to equal cards.
                self.cards.remove(card)   #Removing the card that war turned into another
                self.cards.remove(match)    #Removing the original card that was turned into another.
                print "Hand %s: %s matches %s" % (self.name, card, match) #Hand's name and the matches.
                count = count + 1
        return count   #Quantity of pairs removed.
#Uncomment to see.
#game = CardGame()                      #Creating a class of CardGame. (Create the deck and shuffle it)
#hand = OldMaidHand("soon")             #Creating a hand of this game.
#game.deck.deal([hand],13)              #Dealling 13 cards to one player from deck.deal from the deck in CardGame.
#print hand
#hand.removeMatches()
#print hand

#'str' has not attribuit object for suit
#This error was because I plugged str in the pop method from deck.
#Second, self.cards.removeCard doest work, self.cards.remove works.
#Third, It was not working because return count was inside the for loop.

#**********************16.7***************************
#*******************OldMaidGame class***********************
#I already have:
#A class for the cards.
#A class to organize and create the decks.
#A class to initializate a hand and add cards. (Deck)
#A class to start any game.
#A class to create a hand to the specific game OldMaidHand. (Hand)
#A class to play the specific game OldMaidGame. (Bellow)
#Finally, it's time to play now. We will inheritate the CardGame,, by the way we'll not need to create the deck.
class OldMaidGame(CardGame):
    #RemoveAllMatches.
    def removeAllMatches(self):
        count = 0
        for eachhand in self.hands:
            count = count + eachhand.removeMatches()
        return count

    #Print all hands.
    def printHands(self):
        for eachhand in self.hands:
            print eachhand   #or just print eachhand

    #Takes one argument that indicate whose turn it is. Self is the game.
    def playOneTurn(self, i):
        #If the player has no cards. No matches.
        if self.hands[i].isEmpty():
            return 0
        neighbor = self.findNeighbor(i)  #Find the index of the neighbor
        pickedCard = self.hands[neighbor].popCard()  #Take the top card of the neighbor. 
        self.hands[i].addCard(pickedCard)           #Add it to the person.
        print "Hand", self.hands[i].name, "picked: ", pickedCard   #Showing the card that was picked.
        count = self.hands[i].removeMatches() #Receiving the quantity of matches that was found.
        self.hands[i].shuffle()   #Shuffling the card of this player. self.hands[i] = The player. So the next player's choice is random.
        return count   #Number of matches.

    #FindNeighbor start with the player in the left and goes until find one player that has cards.
    def findNeighbor(self, i):
        numHands = len(self.hands)
        for next in range(1, numHands):
            neighbor = (i + next) % numHands  #if i = 3, neighbor will be 0. If i = 0 neighbor will be 1. If i = 1 neighbor will be 2.
            #If the hand is not empty. This is the neighbor I am looking for.
            if not self.hands[neighbor].isEmpty():
                return neighbor        #This is the neighbor with no empty hand.
        
    def play(self, names):  #Self and the a list of names. (People who is going to play)

        #Remove the Queen of Clubs.
        self.deck.removeCard(Card(0,12))

        #Make a hand for each player.
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))  #It is here that the OldMindHand takes action. I could have created just a Hand, but I would not be able to use removeMatches.

        #deal the cards.   #Each hand is in self.hands.
        self.deck.deal(self.hands)   #From the game(self) from the deck(deck) that is inherited in CardGame deal the cards to the list of self.hands that are hand of OMH Game.
        #No second argument, because of the default value of 999.
        print "--------Cards have been dealt"
        self.printHands()   #Above
    
        #Remove initial matches.    
        matches = self.removeAllMatches()   #matches receive the number of matches found.
        print "------------Matches discarded, play begins"
        self.printHands()   #Above

        #Play untill all 50 cards are matched.  (when matches = 25)
        turn = 0
        numHands = len(self.hands)
        while matches < 25:   #When matches i 24 this will run one more time and match will get into 25, then it can not run anytime more. That's why it is not <=.
            matches = matches + self.playOneTurn(turn)  #Above
            turn = (turn + 1)% numHands
        print "----------Game is Over"
        self.printHands()
        print "--------THE WINNER!!!"
        for eachhand in self.hands:
            if not eachhand.isEmpty():
                print eachhand.name, " ---> WON THE GAME"
#Executing the game.
game = OldMaidGame()
game.play(["soon","sam","MIT"])
