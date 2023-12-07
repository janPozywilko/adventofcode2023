import typer

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().splitlines()
    return d

def hand_type(game):
    hand = game.split(" ")[0]
    card_count = {card: hand.count(card) for card in hand}
    counts = list(card_count.values())
    if 5 in counts:
        return 6  # Five of a kind
    elif 4 in counts:
        return 5  # Four of a kind
    elif 3 in counts and 2 in counts:
        return 4  # Full house
    elif 3 in counts:
        return 3  # Three of a kind
    elif counts.count(2) == 2:
        return 2  # Two pair
    elif 2 in counts:
        return 1  # One pair
    else:
        return 0  # High card
    
def hand_type_2(game):
    hand = game.split(" ")[0]
    if hand == 'JJJJJ':
        hand = 'AAAAA'
    card_count = {card: hand.count(card) for card in hand}
    if 'J' in card_count.keys():
        jokers = card_count.get('J')
        card_count.pop('J')
        max_key = max(card_count, key=card_count.get) 
        card_count[max_key] += jokers
    counts = list(card_count.values())
    if 5 in counts:
        return 6  # Five of a kind
    elif 4 in counts:
        return 5  # Four of a kind
    elif 3 in counts and 2 in counts:
        return 4  # Full house
    elif 3 in counts:
        return 3  # Three of a kind
    elif counts.count(2) == 2:
        return 2  # Two pair
    elif 2 in counts:
        return 1  # One pair
    else:
        return 0  # High card
    

def card_value(card):
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return card_values[card]

def card_value_2(card):
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return card_values[card]
    
def sortDeck(converted_deck, original_deck):
    n = len(converted_deck)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):

            if converted_deck[j][1] > converted_deck[j + 1][1]:
                converted_deck[j], converted_deck[j + 1] = converted_deck[j + 1], converted_deck[j]
                already_sorted = False
            elif converted_deck[j][1] == converted_deck[j+1][1]:
                for k in range(5):
                    if card_value(original_deck[converted_deck[j][0]].split(" ")[0][k]) > card_value(original_deck[converted_deck[j+1][0]].split(" ")[0][k]):
                        converted_deck[j], converted_deck[j + 1] = converted_deck[j + 1], converted_deck[j]
                        already_sorted = False
                        break
                    elif card_value(original_deck[converted_deck[j][0]].split(" ")[0][k]) < card_value(original_deck[converted_deck[j+1][0]].split(" ")[0][k]):
                        break
                    else:
                        continue

        if already_sorted:

            break

    return converted_deck

def sortDeck_2(converted_deck, original_deck):
    n = len(converted_deck)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):

            if converted_deck[j][1] > converted_deck[j + 1][1]:
                converted_deck[j], converted_deck[j + 1] = converted_deck[j + 1], converted_deck[j]
                already_sorted = False
            elif converted_deck[j][1] == converted_deck[j+1][1]:
                for k in range(5):
                    if card_value_2(original_deck[converted_deck[j][0]].split(" ")[0][k]) > card_value_2(original_deck[converted_deck[j+1][0]].split(" ")[0][k]):
                        converted_deck[j], converted_deck[j + 1] = converted_deck[j + 1], converted_deck[j]
                        already_sorted = False
                        break
                    elif card_value_2(original_deck[converted_deck[j][0]].split(" ")[0][k]) < card_value_2(original_deck[converted_deck[j+1][0]].split(" ")[0][k]):
                        break
                    else:
                        continue

        if already_sorted:

            break

    return converted_deck

def main():
    deck = loadData("data.txt")
    sum = 0
    converted_deck = []

    # Part 1
    # for i,hand in enumerate(deck):
    #     converted_deck.append([i,hand_type(hand)])
    # sorted_deck = sortDeck(converted_deck, deck)
    
    # for i in range(1, len(sorted_deck)+1):
    #     sum += i * int(deck[sorted_deck[i-1][0]].split(" ")[1])

    # print(sum)

    # Part 2
    for i,hand in enumerate(deck):
        converted_deck.append([i,hand_type_2(hand)])
    sorted_deck = sortDeck_2(converted_deck, deck)
    
    for i in range(1, len(sorted_deck)+1):
        sum += i * int(deck[sorted_deck[i-1][0]].split(" ")[1])

    print(sum)

    
    

    


if __name__ == "__main__":
    typer.run(main)