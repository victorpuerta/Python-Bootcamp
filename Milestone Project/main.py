from Game import * 




if __name__ == '__main__':
	d = Card()
	g = Game()
	player = Player("Antonio")

	g.create_deck()
	g.shuffle_deck()

	g.name_player()
	g.deal_cards()
	#print(g.deck)

	#print(d)
	#print(g.deck)