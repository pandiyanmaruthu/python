from random import shuffle
Deck=list(range(2,11)*4)
Deck1=[10,10,10,10]*4
Playing=True
Deck.extend(Deck1)
shuffle(Deck)
print (len(Deck))
print (Deck)
player=[]
dealer=[]
def pick_card(cardlist):
    mycard=cardlist.pop()
    return mycard

while len(player)<2 and len(dealer)<2:
    player.append(pick_card(Deck))
    dealer.append(pick_card(Deck))
# print ("Dealer Cards:[*, {}] ".format(dealer[1]))
# print ("Player Cards:{} ".format(player))

if sum(player)>21:
    print ("Dealer Won!!")
elif sum(player)==21 and (sum(dealer)>21 or sum(dealer)<21):
    print ("Player Won!!")
while Playing:
    print ("Dealer Cards:[*, {}] ".format(dealer[1]))
    print ("Player Cards:{} ".format(player))
    hit_or_stand=raw_input("Do you want to Hit or Stand:  ").upper()
    if hit_or_stand[0]=="H":
        while sum(player)<21:
            player.append(pick_card(Deck))

            break
    else:
        while (sum(dealer)<17):
            dealer.append(pick_card(Deck))
        if sum(dealer)>21 and sum(dealer)>sum(player):
            print ("Player Won!!")
            print ("Dealer: {} ".format(dealer))
            print ("Player: {}".format(player))
            print ("Dealer Sum: {}".format(sum(dealer)))
            print ("Player Sum: {}".format(sum(player)))
        elif sum(dealer)<=21 and sum(dealer)>sum(player):
            print ("Delear Won!!")
            print ("Dealer: {} ".format(dealer))
            print ("Player: {}".format(player))
            print ("Dealer Sum: {}".format(sum(dealer)))
            print ("Player Sum: {}".format(sum(player)))
        elif sum(player)<=21 and sum(player)>sum(dealer):
            print ("Player Won!!")
            print ("Dealer: {} ".format(dealer))
            print ("Player: {}".format(player))
            print ("Dealer Sum: {}".format(sum(dealer)))
            print ("Player Sum: {}".format(sum(player)))
        elif sum(player) > 21 and sum(player) > sum(dealer):
            print ("Delear Won!!")
            print ("Dealer: {} ".format(dealer))
            print ("Player: {}".format(player))
            print ("Dealer Sum: {}".format(sum(dealer)))
            print ("Player Sum: {}".format(sum(player)))
        Playing=False


