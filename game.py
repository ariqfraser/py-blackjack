from random import shuffle
from calcHandValue import calcHandValue
from re import search
from os import system

class Game:
    deck = []
    dealerHand = []
    playerHand = []

    def __init__(self):
        self.generateDeck()

    def generateDeck(self):
        suits = 'HDCS'
        ranks = 'A23456789TJQK'
        self.deck = [suit + rank for suit in suits for rank in ranks]
        shuffle(self.deck)

    def draw(self):
        card = self.deck.pop()
        return card

    def display_hand(self, player=False, showOneCard=False):
        hand = self.playerHand if player else self.dealerHand
        hand_value = calcHandValue(hand)
        display_value = hand_value[0] if hand_value[0] == hand_value[1] else f"{hand_value[0]} or {hand_value[1]}"
        hand_value_with_hidden_value = calcHandValue([hand[0]])
        display_with_hidden_value = hand_value_with_hidden_value[0] if hand_value_with_hidden_value[0] == hand_value_with_hidden_value[1] else f"{hand_value_with_hidden_value[0]} or {hand_value_with_hidden_value[1]}"
        display_hand = hand[0] if showOneCard else ', '.join(hand)
        print(f"{'Your' if player else 'Dealer'} hand: {display_hand}")
        print(f"Total value: {display_with_hidden_value if showOneCard else display_value }\n")

    def start(self):
        system('cls')
        print("Welcome to the table.\n")
        self.dealerHand = [self.draw(), self.draw()]
        self.playerHand = [self.draw(), self.draw()]

        self.display_hand(player=True)
        self.display_hand(showOneCard=True)

        while True:
            user_choice = input("[1] Hit [2] Stand\nEnter a number: ")
            system('cls')
            if user_choice == "1":
                self.playerHand.append(self.draw())
                self.display_hand(player=True)
                self.display_hand(showOneCard=True)

                player_value = calcHandValue(self.playerHand)
                if all(value > 21 for value in player_value):
                    print("You have bust. Sorry.")
                    break
            elif user_choice == "2":
                self.display_hand(player=True)
                self.display_hand()
                player_value = calcHandValue(self.playerHand)
                dealer_value = calcHandValue(self.dealerHand)

                while max(dealer_value) < 17:
                    self.dealerHand.append(self.draw())
                    dealer_value = calcHandValue(self.dealerHand)
                    print("Dealer draws\n")
                    self.display_hand()
                    print("")
                
                if all(value > 21 for value in dealer_value):
                    print("Dealer busts. You WIN!")
                elif max(player_value) > max(dealer_value):
                    print("You WIN!")
                elif max(player_value) == max(dealer_value):
                    print("PUSH")
                else:
                    print("Dealer WINS")
                break
            else:
                self.display_hand(player=True)
                self.display_hand(showOneCard=True)
                print("Invalid choice. Please enter 1 or 2.")
        print("Thanks for playing")