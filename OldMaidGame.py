# Name: Soon Sam R Santos 
# Date: January 30, 2017
# OldMaidGame.py
#*****************OldMaid CardGame*********************
import random
class Card:
    suitList=["Clubs","Diamonds","Hearts","Spades",]
    rankList=["narf","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King",]
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (self.rankList[self.rank] + " of " + self.suitList[self.suit])
    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(0,4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))
    def printDeck(self):
        for card in self.cards:
            print card
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " "*i + str(self.cards[i]) + "\n"
        return s
    def shuffle(self):
        nCards = len(self.cards)
        for i in range(0,nCards):
            j = random.randrange(0, nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    def removeCard(self, card):
        if card not in self.cards:
            return False
        else:
            self.cards.remove(card)
            return True
    def popCard(self):
        return self.cards.pop()
    def isEmpty(self):
        return (len(self.cards) == 0)
    def deal(self, hands, nCards=999):
        nHands = len(hands)
        for i in range(nCards):
            if self.isEmpty(): break
            card = self.popCard()
            hand = hands [i%nHands]
            hand.addCard(card)            
class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name
    def addCard(self, card):
        self.cards.append(card)
    def __str__(self):
        s = "Hand " + self.name
        if self.isEmpty():
            return s + " is Empty"
        else:
                return s + " contains\n" + Deck.__str__(self)
class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
class OldMaidHand(Hand):
    def removeMatches(self):
        count = 0
        originalCards = self.cards[:]
        for card in originalCards:
            match = Card (3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print "Hand %s: %s matches %s" %(self.name, card, match)
                count = count + 1
        return count
class OldMaidGame(CardGame):
    def removeAllMatches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.removeMatches()
        return count
    def printHands(self):
        for hand in self.hands:
            print hand
    def findNeighbor(self, i):
        numHands = len(self.hands)
        for next in range(1, numHands):
            neighbor = (i + next) % numHands
            if not self.hands[neighbor].isEmpty():
                return neighbor
    def playOneTurn(self, i):
        if self.hands[i].isEmpty():
            return 0
        neighbor = self.findNeighbor(i)
        pickedCard = self.hands[neighbor].popCard()
        self.hands[i].addCard(pickedCard)
        print "Hand ", self.hands[i].name, "picked: ", pickedCard
        count = self.hands[i].removeMatches()
        self.hands[i].shuffle()
        return count
    def play(self, names):
        self.deck.removeCard(Card(0,12))
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
        self.deck.deal(self.hands)
        print "-----------Cards have been dealt"
        self.printHands()
        matches = self.removeAllMatches()
        print "----------Matches discarded, play begins"
        self.printHands()
        turn = 0
        numHands = len(self.hands)
        while matches < 25:
            matches = matches + self.playOneTurn(turn)
            turn = (turn + 1)%numHands
        print "--------Game is Over"
        self.printHands()
        print "**$$$$****THE LOOSER****$$$$***"
        for hand in self.hands:
            if (len(hand.cards)!=0):
                return hand.name, " ---> LOST THE GAME"
            
GAME = OldMaidGame()
GAME.play(["soon","sam","MIT"])
