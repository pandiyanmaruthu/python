import blackjack_object
import sys

def start_play():

    while True:
        print (""""Welcome to black jack Game....Get as close as 21 don't go over 
                Delear will hit until he reaches 17. Ace value is 1 or 11""")

        deck=blackjack_object.Deck()
        deck.shuffle()
        player_hand=blackjack_object.Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        player_hand.adjust_ace()

        delear_hand=blackjack_object.Hand()
        delear_hand.add_card(deck.deal())
        delear_hand.add_card(deck.deal())
        delear_hand.adjust_ace()
        player_chips=blackjack_object.Chips()
        blackjack_object.take_chip(player_chips)
        blackjack_object.show_some(player_hand,delear_hand)
        def hit():
            while Playing:
                blackjack_object.hit_or_stand(player_hand,deck)

                blackjack_object.show_some(player_hand,delear_hand)

                if player_hand.value>21:
                    blackjack_object.player_bust(player_hand,delear_hand,player_chips)
                    break
        def stand():
            if player_hand.value<=21:
                while delear_hand.value<17:
                    blackjack_object.hit(delear_hand,deck)
                blackjack_object.show_all(player_hand,delear_hand)

                if delear_hand.value>21:
                    blackjack_object.dealer_bust(player_hand,delear_hand,player_chips)
                elif delear_hand.value>player_hand.value:
                    blackjack_object.player_bust(player_hand,delear_hand,player_chips)
                elif player_hand.value>delear_hand.value:
                    blackjack_object.player_won(player_hand,delear_hand,player_chips)
                else:
                    blackjack_object.match_draw(player_hand,delear_hand)
        def check_total():
            print ("Player's chips remaining: {}".format(player_chips.total))

        again=input("Do you want to play again!(Y/N): ").upper()
        if again[0]=="Y":
            Playing=True
            continue
        else:
            import getpass
            login=getpass.getuser()
            print ("Thanks for Playing Black-Jack! {}".format(login))
            break
start_play()
print(sys.getsizeof(blackjack_object.Hand))
print(sys.getsizeof(blackjack_object.take_chip))
