class Account():
    def __init__(self, name,balance=100):
        self.name=name
        self.balance=balance
    def deposit(self,d_value):
        self.balance+=d_value
    def withdraw(self,w_value):
        if w_value>=self.balance:
            print ("You dont have enough money, Your balance is {}".format(self.balance))
        else:
            self.balance-=w_value
# david=Account("david")
# david.deposit(10000)
# print (david.balance)
# david.withdraw(5000)
# print (david.balance)
import itertools
import random
class Decks():
    def __init__(self,set1,set2,set3,set4):
        self.set1=set1
        self.set2=set2
        self.set3=set3
        self.set4=set4
Decks1=Decks(list(range(1,14)),list(range(1,14)),list(range(1,14)),list(range(1,14)))
print (Decks1.set1)
print (Decks1.set2)
print (Decks1.set3)
print (Decks1.set4)
class calc():
    player=[]
    computer=[]
    output = list(itertools.chain.from_iterable((Decks1.set1, Decks1.set2, Decks1.set3, Decks1.set4)))
    # output=" ".join((Decks1.set1,Decks1.set2,Decks1.set3,Decks1.set4))
    # import random
    # print (random.randint(Decks1.set1,Decks1.set2,Decks1.set3,Decks1.set4))
    random.shuffle(output)
    # print (output)
    def player_won(self):
        return sum(calc.player)==21 or sum(calc.computer)<sum(calc.player)
    def computer_won(self):
        return sum(calc.computer)==21 or sum(calc.computer)>sum(calc.player)

    def play_game(self):
        i=0
        while i==0:
            calc.player.append(calc.output(i))
            calc.output.pop(i)
            calc.computer.append(calc.output(i))




# import itertools
# import random
# def cardlist():
#     output=list(itertools.chain.from_iterable((Decks1.set1,Decks1.set2,Decks1.set3,Decks1.set4)))
# # output=" ".join((Decks1.set1,Decks1.set2,Decks1.set3,Decks1.set4))
# # import random
# # print (random.randint(Decks1.set1,Decks1.set2,Decks1.set3,Decks1.set4))
#     random.shuffle(output)


while True:
    print ("Welcome to play blackjack...")
    req=input("Do you want to play: ").upper()
    if req=="Y":
        gameon=True
    else:
        gameon=False
    turn1="Player_turn"
    calcu=calc()
    while gameon:

        calcu.play_game()
        if calcu.player_won()==True:
            print ("The Player Won")
            break
        elif calcu.computer_won()==True:
            print ("The Computer Won")
            break
        else:
            continue








