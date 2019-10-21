from random import shuffle
from Card import *
from Player import *

class Game():
    
    game = False
    cards = Card()
    deck = []
    player2 = Player("Dealer")
    player1 = ''
    value_player1 = 0
    value_player2 = 0
    player_win = ''

    

    '''
    ///////////////////////////////////////////////
    DECK SET UP
    /////////////////////////////////////////
    '''

    def create_deck(self):
        
        for suits_0 in self.cards.suits:
            for ranks_0 in self.cards.ranks:
                self.deck += [suits_0 + " " + ranks_0]
        return self.deck

        
    def shuffle_deck(self):        

        shuffle(self.deck)
        return self.deck    

    '''
    ///////////////////////////////////////////////
    ///////////////////////////////////////////////
    /////////////////////////////////////////
    '''

    '''
    ///////////////////////////////////////////////
    PLAYER LOGIC
    /////////////////////////////////////////
    '''

    def name_player(self):
        while True:
            name = input("Tell us your name\n")
            if len(name) > 3:
                self.player1 = Player(name)
                print("Hi {}, hope you enjoy the game!".format(name))
                break
            else:
                continue

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
                
        return self.deck   


    def hit(self):

        self.player1.append(self.deck[1])
        del self.deck[1]
        return self.deck


    def stands(self):

        if  Game.hand_computer(self) < 17:
            self.player1.append(self.deck[1])
            del self.deck[1]
            return self.deck
            #Game.stands(self)
 
        else:
            if Game.hand_computer(self) > Game.hand_player(self) and Game.hand_computer(self) <= 21:
                self.player_win = self.player2.get_name()
                return self.player_win
            else:
                self.player_win = self.player1.get_name()
                return self.player_win






    def hand_player(self):

        self.value_player1 = 0

        for value in self.cards.values:
            for card in self.player1.get_hand():
                if value in card:
                    self.value_player1 += self.cards.values[value]
        return self.value_player1


    def hand_computer(self):

        self.value_player2 = 0

        for value in self.cards.values:
            for card in self.player2.get_hand():
                if value in card:
                    self.value_player2 += self.cards.values[value]
        return self.value_player2


    def check_hand_player(self):

        if Game.hand_player(self)>21:
            return True
        else:
            return False
           

    

    '''
    ///////////////////////////////////////////////
    ///////////////////////////////////////////////
    /////////////////////////////////////////
    '''


  
    '''
    ///////////////////////////////////////////////
    GAME LO/GIC
    ////////////////////////////////////////
    '''


    def start(self):
        bet = 0
        decision = ''
        self.game = True
        Game.create_deck(self)
        Game.shuffle_deck(self)
        Game.name_player(self)
        Game.deal_cards(self)

        print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n")
        print("Dealer hits until she reaches 17. Aces count as 1 or 11.\n")
        bet = input("How many chips would you like to bet?\n")
        self.player1.set_bet(bet) 

        while self.game:       

            print("\nDealer's Hand:")
            print("<card hidden>")
            print("{} \n".format(self.player2.get_hand_last()))

            print("Player's Hand:")
            for cards in self.player1.get_hand():
               print(cards)
            print("\n",Game.hand_player(self))


            if Game.check_hand_player(self):
                break

            decision = input("\nWould you like to Hit or Stand? Enter 'h' or 's'\n")

            if decision == 'h':
                print("Player's hitted")
                Game.hit(self)
                

            else:
                print("Player's sants")
                Game.stands(self)
                break

        if Game.check_hand_player(self):
            print("Player bust!")
            print("Player's winnings stand at {}".format((int(self.player1.get_bet())/2)))

        else:
            print("\nDealer's Hand:")
            for cards in self.player1.get_hand():
                print(cards)
                
            print("\n",Game.hand_computer(self))
            print("\n")          

            print("Player's Hand:")
            for cards in self.player1.get_hand():
               print(cards)
            print("\n",Game.hand_player(self))
            print("{}'s winnings stand at {}".format(self.player_win,(int(self.player1.get_bet())/2)))

       

    '''
    ///////////////////////////////////////////////
    ///////////////////////////////////////////////
    /////////////////////////////////////////
    '''



    '''
    ///////////////////////////////////////////////
    CHECK HANDS AND TESTING
    /////////////////////////////////////////
    '''
  

    def __str__(self):

         return ("Player 1 is: {} and player 2 is {}".format(self.player1, self.player2))
    
    '''
    ///////////////////////////////////////////////
    ///////////////////////////////////////////////
    /////////////////////////////////////////
    '''    