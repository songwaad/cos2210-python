def cut(card_in_deck):
    length = len(card_in_deck)
    new_deck = []
    
    for i in range(int(length/2), length):
        new_deck.append(card_in_deck[i])

    for i in range(0, int(length/2)):
        new_deck.append(card_in_deck[i])

    return new_deck

def slit(card_in_deck):
    length = len(card_in_deck)
    new_deck = []

    for i in range(0, length, 2):
        new_deck.append(card_in_deck[i])

    for i in range(1, length, 2):
        new_deck.append(card_in_deck[i])
    
    return new_deck


card_in_deck = input("Please enter the cards in the deck (separated by spaces):").split()
command = input("Please enter the commands (e.g., CSCS):").upper()

for c in command:
    if c == 'C':
        card_in_deck = cut(card_in_deck)
    elif c == 'S':
        card_in_deck = slit(card_in_deck)

print(card_in_deck)