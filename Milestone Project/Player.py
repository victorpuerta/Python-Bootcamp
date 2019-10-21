
class Player():

    def __init__(self,name,hand=[],bet=0):
        self.name = name
        self.hand = hand
        self.bet = bet

    def get_hand(self):
        return self.hand

    def get_hand_last(self):
        return self.hand[-1]

    def set_hand(self, hand):
        self.__hand = hand

    def set_bet(self, bet):
        self.bet = bet

    def get_bet(self):
        return self.bet

    def get_name(self):
        return self.name

    def append(self, val):
        self.hand = self.hand + [val]
        return self.hand  


    def __str__(self):
        return ("{} has: {}".format(self.name,self.hand))
