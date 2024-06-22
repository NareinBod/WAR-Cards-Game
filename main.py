from classes import Player, Deck

# Create players
player1 = Player('Player 1')
player2 = Player('Player 2')

# Create a deck and shuffle all the cards in the deck
new_deck = Deck()
new_deck.shuffle()

# Assign cards in the deck equally to both players
for i in range(len(new_deck.all_cards)):
    if i % 2 == 0:
        player1.add_cards(new_deck.deal_one())
    else:
        player2.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Currently on round {round_num}")
    
    # Condition for player out of cards
    if len(player1.all_cards) == 0:
        print('Player One is out of cards, Player Two wins')
        game_on = False
        break
    if len(player2.all_cards) == 0:
        print('Player Two is out of cards, Player One wins')
        game_on = False
        break

    # Start a new round
    player_one_cards = [player1.remove_one()]
    player_two_cards = [player2.remove_one()]

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player2.add_cards(player_one_cards)
            player2.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR")

            if len(player1.all_cards) < 5:
                print('Player One unable to declare war')
                print('Player Two wins')
                game_on = False
                break
            elif len(player2.all_cards) < 5:
                print('Player Two unable to declare war')
                print('Player One wins')
                game_on = False
                break
            else:
                for num in range(5):
                    if len(player1.all_cards) > 0:
                        player_one_cards.append(player1.remove_one())
                    if len(player2.all_cards) > 0:
                        player_two_cards.append(player2.remove_one())



    














