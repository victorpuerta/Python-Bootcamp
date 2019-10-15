from random import shuffle
from Card import *
from Player import *

class Game():
    
    game = False
    cards = Card()
    deck = []
    player2 = Player("Computer")
    player1 = ''

    def name_player(self):
        while True:
            name = input("Tell us your name\n")
            if len(name) > 3:
                self.player1 = Player(name)
                print("Hi {}, hope you enjoy the game!".format(name))
                break
            else:
                continue

    
    def create_deck(self):
        
        for suits_0 in self.cards.suits:
            for ranks_0 in self.cards.ranks:
                self.deck += [suits_0 + " " + ranks_0]
        return self.deck

        
    def shuffle_deck(self):        
        shuffle(self.deck)
        return self.deck    


    def deal_cards(self):        

        if len(self.player2.hand)==0:        
            for x in range(2):
                self.player1.append(self.deck[x])
                del self.deck[x]

            for x in range(2):
                if x == 0:
                	self.player2.append(self.deck[2])
                	del self.deck[2]
                else:
                	self.player2.append(self.deck[3])
                	del self.deck[3]              
        else:
            for x in range(1):
                self.player2.hand.append(self.deck[x])
                self.player2.hand.append(self.deck[x+1])
                print(self.deck.pop(x))
       # print(self.deck)
        print(self.player1.get_hand())
        print(self.player2.get_hand())
        return self.deck       

    def __str__(self):

         return ("Player 1 is: {} and player 2 is {}".format(self.player1, self.player2))
    
