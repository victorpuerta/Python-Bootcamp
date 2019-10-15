
class Player():

    def __init__(self,name,hand=[],bet=0):
        self.name = name
        self.hand = hand
        self.bet = bet

    def get_hand(self):
        return self.hand

    def set_hand(self, hand):
        self.__hand = hand

    def append(self, val):
        self.hand = self.hand + [val]
        return self.hand  


    def __str__(self):
        return ("{}".format(self.hand))
