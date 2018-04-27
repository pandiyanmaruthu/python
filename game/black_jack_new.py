from random import shuffle
Suits=("Clever","Hearts","Diamonds","Spades")
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
Playing=True
class Cards():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.deck=[]
        for suit in Suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))
    def __str__(self):
        mydeck=''
        for cards in self.deck:
            mydeck+="\n"+cards.__str__()
        return "Deck Has: {} ".format(mydeck)

    def shuffle(self):
        shuffle(self.deck)

    def takecard(self):
        lastcard=self.deck.pop()
        return lastcard
deck_of_cards=Deck()
deck_of_cards.shuffle()
print (deck_of_cards)
print (deck_of_cards.takecard())

