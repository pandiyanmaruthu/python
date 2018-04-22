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
    # def __init__(self):
    #     self.deck = []  # start with an empty list
    #     for suit in Suits:
    #         for rank in ranks:
    #             self.deck.append(Cards(suit, rank))  # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp+='\n' + card.__str__()
        return "The Deck Has: " + deck_comp
    #
    # def __str__(self):
    #     deck_comp = ''  # start with an empty string
    #     for card in self.deck:
    #         deck_comp += '\n ' + card.__str__()  # add each Card object's print string
    #     return 'The deck has:' + deck_comp
    def shuffle(self):
        return shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
# class Deck:
#
#     def __init__(self):
#         self.deck = []  # start with an empty list
#         for suit in Suits:
#             for rank in ranks:
#                 self.deck.append(Cards(suit, rank))  # build Card objects and add them to the list
#
#     def __str__(self):
#         deck_comp = ''  # start with an empty string
#         for card in self.deck:
#             deck_comp += '\n ' + card.__str__()  # add each Card object's print string
#         return 'The deck has:' + deck_comp
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#
#     def deal(self):
#         single_card = self.deck.pop()
#         return single_card
mydeck=Deck()
print (mydeck)

