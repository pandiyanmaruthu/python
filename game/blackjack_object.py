Suits=("Hearten","Diamond","Spade","Clever")
ranks=("two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace")
values={"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"jack":10,"queen":10,"king":10,"ace":11}
Playing=True

from random import shuffle
class Cards():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):
        self.deck = []
        for suit in Suits:
            for rank in ranks:
                self.deck.append(Cards(suit, rank))

    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp+='\n' + card.__str__()
        return "The Deck Has: " + deck_comp

    def shuffle(self):
        return shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card



class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.ace=0
    def add_card(self, card):
        self.cards.append(card.__str__())
        self.value+=values[card.rank]
        if card.rank=="ace":
            self.ace+=1

    def adjust_ace(self):
        # l=(len(self.cards))
        # if l<=2 and self.value>=21:
        #     self.value-=10
        while self.value>21 and self.ace:
            self.value-=10
            self.ace-=1

class Chips():
    def __init__(self):
        self.total=100
        self.bet=0
    def won_chips(self):
        self.total+=self.bet

    def loss_chips(self):
        self.total-=self.bet

def take_chip(chip):
    while True:
        try:
            chip.bet=input("Please enter your bet amount: ")
        except:
            print ("enter number...")
            continue
        else:
            if chip.bet>chip.total:
                print ("Please enter less than total {}".format(chip.total))
                continue
        break

def hit(hand,deck):
    hand.add_card(deck.deal())
    hand.adjust_ace()

def hit_or_stand(hand,deck):
    global Playing
    while True:
        get_input=raw_input("Do you want ot hit/stand? : ").upper()
        if get_input[0]=="H":
            hit(hand,deck)
        elif get_input[0]=="S":
            print ("Player is standing..Now Dealer Play!!")
            Playing=False
        else:
            print ("Please try again...")
            continue
        break
def show_some(player,delear):
    print ("Delear Card [*,{}]".format(delear.cards[1]))
    print ("Dealear Value {}".format(delear.value))
    print ("Player Card {}".format(player.cards))
    print ("Player Value {}".format(player.value))

def show_all(player,delear):
    print ("Delear Card {}".format(delear.cards))
    print ("Dealear Value {}".format(delear.value))
    print ("Player Card {}".format(player.cards))
    print ("Player Value {}".format(player.value))



mycard=Deck()
mycard.shuffle()
# print (mycard)
# print ("\n")
# print (mycard.deal())
myhand=Hand()
myhand.add_card(mycard.deal())
myhand.add_card(mycard.deal())
myhand.adjust_ace()
myhand.add_card(mycard.deal())
myhand.adjust_ace()
print (myhand.value)
print (myhand.cards)
mychips=Chips()
take_chip(mychips)
print (mychips.bet)
playerhand=Hand()
playerdeck=Deck()
hit(playerhand,playerdeck)
hit(playerhand,playerdeck)
print (playerhand.cards)
print(playerhand.value)