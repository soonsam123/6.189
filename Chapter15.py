# Name: Soon Sam R Santos
# Date: January 26, 2017
# Session: Lecture 8
# Chapter15.py

#**********************Chapter 15*********************
#******************Sets of objects********************

#**********************15.1***************************
#*******************Composition***********************
#IF with While with IF
#Nested structures
#Method invocation
#**********************15.2***************************
#*******************Card objects**********************
#Deck: 52 cards
# 4 suits --> Spades, Hearts, Diamonds, and Clubs.
# 14 ranks --> Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King.
#ENCODE: Define a mapping between a sequence of numbers and the items I want to represent.

#SUITS:
#Spades --> 3
#Hearts --> 2
#Diamonds --> 1
#Clubs --> 0

#RANKS:
#Jack --> 11
#Queen --> 12
#King --> 13

class Card:
    #Class definition for each CARD.
    def __init__(self, suit=0, rank=2):
        self.suit= suit
        self.rank= rank
threeOFClubs=Card(3,1)
#**********************15.3***************************
#*******************Class attributes and the __str__ method**********************
#Figuring out a way to show the cards to the user
class Card:
    #Ususally we use a list of strings
    #CLASS ATTRIBUTES
    suitList= ['Clubs','Diamonds','Hearts','Spades']
    #narf is used to eliminate the necessity to worry with the beginning at 0.
    rankList=['narf','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    #Class definition for each CARD.
    def __init__(self, suit=0, rank=2):
        self.suit= suit
        self.rank= rank
    def __str__(self):
        return (self.rankList[self.rank] + "of" +
                self.suitList[self.suit])
#rankList[self.rank] would case a error : global name 'rankList' is not defined
#because as my list is inside the class, I can access it only if I use self.list.
#A class attribute is defined outside of any method, and it can be accessed from any
#of the methods in the class.
#self.suitList[self.suit] means "use the attribute suit from the object self as an
#index into the class attribute named suitList, and select the apropriate
#string."
card1=Card(1, 11)
print card1
#JackofDiamonds
card2= Card(1,3)
print card2
#3 of Diamonds
print card2.suitList[1]
#Diamons
#I must call the self to use the list suitList. As it it not defined outside class.
#self.list will bring me to the list, as I use self.__init__() and so on....

#The negative part is that if I modifie a class attribute, it will be always modified
#when I call another.
card1.suitList[1]=  "Testing"
print card1
#JackofTesting
print card2
#3ofTesting
#NO WAY!!!
card1.suitList[1]="Diamonds"
print card1
#JackofDiamonds
print card2
#3ofDiamonds

#**********************15.4***************************
#*******************Comparing cards**********************
#__cmp__ method with two parameters (self,other) that returns 1 if the first object
#is greater, -1 if the second is greater and 0 if they are equal.
#We'll decide that suits are greater than ranks. When comparing 3 of clubs with 2 of
#diamonds. Even though 2 of diamonds have a lower rank, it will be higher because it
#has a greater suit.

class Card:
    suitList= ['Clubs','Diamonds','Hearts','Spades']
    rankList=['narf','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    def __init__(self, suit=0, rank=2):
        self.suit= suit
        self.rank= rank
    def __str__(self):
        return (self.rankList[self.rank] + "of" +
                self.suitList[self.suit])

    def __cmp__(self,other):
        #check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        #suits are the same, check the rank
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        #ranks and suits are the same.
        return 0
    #As an exercise, modify __cmp__ so that Aces are ranked higher than kings.
    def __cmp__(self,other):
        #check the suits.
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        #suits are the same, check the ranks. Ace is the greater card.
        #If the card is an Ace (1). I change the value to 14 and it will properly work
        #as the highest one.
        #If self is an Ace.
        if self.rank==1:
            #and other is also an Ace --> Tie
            if other.rank==1: return 0
            #self is an Ace and other is not. Self is greater
            return 1
        #Other is an Ace and self is not --> other is greater
        if other.rank==1: return -1
        #None is an Ace. I compare normally
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0
    
#**********************15.5***************************
#*******************Decks**********************
#Now creating a deck. The initialization method creates the attribute cards and
#generates the standard set of fifty-two cards.
#SUITS:
#Spades --> 3
#Hearts --> 2
#Diamonds --> 1
#Clubs --> 0

#RANKS:
#Jack --> 11
#Queen --> 12
#King --> 13
class Deck:
    def __init__(self):
        self.cards= []
        #From 0 (clubs) to 3(Spades)
        for suit in range(4):
            #From 1(Ace) to 13(King)
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
        #I can not use return on the __init__ module.

#**********************15.6***************************
#*******************Printing the Deck**********************

class Deck:
    def __init__(self):
        self.cards= []
        for suit in range(4):
            for rank in range(1,14):
                #self.cards is adding classes to their list
                #[<__main__.Card instance at 0x000..., <__main__.Card instance 0x0....]
                self.cards.append(Card(suit,rank))
    def printDeck(self):
        #This is much easier because I am using my Card class.
        for card in self.cards:
            print card
    #We could also use the __str__ module to print the cards.
    def __str__(self):
        s=""
        for i in range(len(self.cards)):
        #This str module takes the str in the class Card.
         s= s + " "*i +str(self.cards[i]) + "\n"

#**********************15.7***************************
#*******************Shuffling the deck**********************
         
#We can do a method to shuffle the cards.
    def shuffle(self):
        import random
        #This is the quantity of times I will shuffle it
        #I will shuffle at the same quantity of cards the deck has.
        nCards= len(self.cards)
        for i in range(nCards):
            #This will be any number from i(i.e: 1) to nCards(i.e: 52) = (i.e: 25)
            j = random.randrange(0,nCards)
            #So the card in the position 1 will change to position 25 and vice versa.
            #In the next loop the card 1 will no change anymore. It is already changed
            #The the next one will be 2 and another random number.
            #Notice, the 25 position will change more than once. But actually,
            #it will change and that is what matters.
            #Tuple assignment is much easier than this bellow.
            #support = self.card[i]
            #self.card[i] = self.card[j]
            #self.card[j]= support
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
#**********************15.8***************************
#*******************Removing and dealing cards**********************
    #Method to remove cards
            def removeCard(self,card):
                #I am not comparing 2 of Hearts with the list. I am comparing
                #a card Class with the cards classes in self.cards.
                #if <__main__.Card instance at 0x00 in [<__main__.Card, <__main_.Card...]
                if card in self.cards:
                    self.cards.remove(card)
                    return True
                else:
                    return False
#Python uses the __cmp__ method to compare deep equality in my removeCard method.
            def popCard(self):
                return self.cards.pop()
            #pop removes the last card in the list. Bottom of the deck.

            def isEmpty(self):
                return (len(self.cards)==0)
