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
class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.ace=0
    def add_card(self,card):
        self.cards.append(card.__str__())
        self.value+=values[card.rank]
        if card.rank=="Ace":
            self.ace+=1
    def adjust_ace(self):
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

def hit(hand,card):
    hand.add_card(card.takecard())
    hand.adjust_ace()

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter Your Bet Amount: "))
        except:
            print ("Please enter in Numbers: ")
        else:
            if chips.bet>chips.total:
                print ("Total: {} Your Bet: {}, Enter Less than Total..".format(chips.total,chips.bet))
            else:
                break

def hit_or_stand(player,delear,card):
    global Playing
    user_input=input("Do You want to hit/Stand?: ").upper()
    if user_input[0]=="H":
        hit(player,card)
    elif user_input[0]=="S":
        Playing=False


def show_some(player,delear):
    print ("Delear Card: [*,{}]".format(delear.cards[1]))
    print ("Player Card: {}".format(player.cards))

def show_all(player,delear):
    print ("Delear Card: {}".format(delear.cards))
    print ("Player Card: {}".format(player.cards))
    print ("Delear Value: {}".format(delear.value))
    print ("Player Value: {}".format(player.value))

def player_bust(player):
    print ("Player Lost")
    player.loss_chips()
def player_won(player):
    print ("Player Won")
    player.won_chips()
def delear_lost(player):
    print ("Delear Lost")
    player.won_chips()
def delear_won(player):
    print ("Delear Won")
    player.loss_chips()

def draw():
    print ("Match tie..")

while True:
    print ("""Welcome To black-jack..""")

    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    player_hand.add_card(deck.takecard())
    player_hand.add_card(deck.takecard())
    player_hand.adjust_ace()
    delear_hand=Hand()
    delear_hand.add_card(deck.takecard())
    delear_hand.add_card(deck.takecard())
    delear_hand.adjust_ace()
    player_chips=Chips()
    take_bet(player_chips)
    show_some(player_hand,delear_hand)

    while Playing:
        hit_or_stand(player_hand,delear_hand,deck)
        show_some(player_hand,delear_hand)
        if player_hand.value>21:
            player_bust(player_chips)
            break

    if player_hand.value<=21:

        while delear_hand.value<17:
            delear_hand.add_card(deck.takecard())

        if delear_hand.value>21:
            delear_lost(player_chips)
        elif delear_hand.value<=21 and delear_hand.value>player_hand.value:
            delear_won(player_chips)
        elif delear_hand.value<21 and delear_hand.value<player_hand.value:
            player_won(player_chips)
        else:
            draw()
    show_all(player_hand,delear_hand)
    print ("Player Chips Total: {}".format(player_chips.total))
    play_again=input("Do you want to play again!..").upper()
    if play_again=="Y":
        Playing=True
        continue
    else:
        print ("Thanks,You can come and play anytime...!")
        break






# mychips=Chips()
# take_bet(mychips)
# print (mychips.bet)


# deck_of_cards=Deck()
# deck_of_cards.shuffle()
# print (deck_of_cards)
# print (deck_of_cards.takecard())

