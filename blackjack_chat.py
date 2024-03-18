import random

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
# deck is a list of tuples, each tuple representing a card
deck = [(card, category) for category in card_categories for card in cards_list]

# return the points corresponding to the value of the card
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

# shuffle deck and deal cards to player and dealer
random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]

while True:
    player_score = sum(card_value(card) for card in player_card)
    dealer_score = sum(card_value(card) for card in dealer_card)
    print("Cards Player Has: ", player_card)
    print("Score of Player: ", player_score)
    print("\n")
    if player_score > 21:
        print("Player Busts! Dealer Wins.")
        break
    choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()
    if choice == "play":
        new_card = deck.pop()
        player_card.append(new_card)
    elif choice == "stop":
        break
    else:
        print("Invalid choice. Please try again.")
        continue

while dealer_score < 17:
    new_card = deck.pop()
    dealer_card.append(new_card)
    dealer_score += card_value(new_card)
    if dealer_score > 21:
        # Check if dealer has an Ace and adjust its value from 11 to 1 if necessary
        for i, card in enumerate(dealer_card):
            if card[0] == 'Ace':
                dealer_card[i] = ('1', card[1])  # Change Ace value from 11 to 1
                dealer_score -= 10  # Adjust the score
                break  # Adjust only one Ace, then break out of the loop

print("Cards Dealer Has:", dealer_card)
print("Score Of The Dealer:", dealer_score)
print("\n")

if dealer_score > 21:
    print("Dealer Busts! Player Wins.")
elif player_score > dealer_score:
    print("Player Wins!")
elif dealer_score > player_score:
    print("Dealer Wins!")
else:
    print("It's a tie.")
