from re import search

def calcHandValue(cards):
    handValue = [0, 0]

    for card in cards:
        value = card[1]
        suit = card[0]

        if search("[A-Z]", value):
            if value == 'A':
                handValue[0] += 1
                handValue[1] += 11
            else:
                handValue[0] += 10
                handValue[1] += 10
        
        else:
            handValue[0] += int(value)
            handValue[1] += int(value)
    return handValue