import random


class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        suits = ['S', "H", "D", "C"]
        return suits[self._card_number // 13]
        """if int(self._card_number) // 13 == 0:
            return "S" #Spades
        if int(self._card_number) // 13 == 1:
            return "H" #Heats
        if int(self._card_number) // 13 == 2:
            return "D" #Diamonds
        if int(self._card_number) // 13 == 3:
            return "C" #club"""

    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        """if int(self._card_number) % 13 == 0:
            return "A"
        if int(self._card_number) % 13 == 1:
            return "2" 
        if int(self._card_number) % 13 == 2:
            return "3" 
        if int(self._card_number) % 13 == 3:
            return "4" 
        if int(self._card_number) % 13 == 4:
            return "5" 
        if int(self._card_number) % 13 == 5:
            return "6" 
        if int(self._card_number) % 13 == 6:
            return "7" 
        if int(self._card_number) % 13 == 7:
            return "8" 
        if int(self._card_number) % 13 == 8:
            return "9" 
        if int(self._card_number) % 13 == 9:
            return "10" 
        if int(self._card_number) % 13 == 10:
            return "J" 
        if int(self._card_number) % 13 == 11:
            return "Q" 
        if int(self._card_number) % 13 == 12:
            return "K" 
        pass"""
        value = self._card_number % 13
        card_values = ['A', '2', '3', '4', '5', '6', '7', '8','9','10','J','Q','K']
        return card_values([value])

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        return self.get_suit() + self.get_value()

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        suit_long_names = {"C":"Clubs", "H":"Hearts", "D":"Diamonds", "S":"Spades"}
        value_long_names = {"A":"Ace","2":"Two","3":"Three", "4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight", "9":"Nine", "10":"Ten", "J":"Jack","K":"King","Q":"Queen"}
        return f"{value_long_names[self.get_value()]} Of {suit_long_names[self.get_suit()]}"
        


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        return len(self._card_list)

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        top_card = self._card_list[len(self._card_list) - 1]
        self._card_list.remove(top_card)
        return top_card


card = Card(1)
print(card.get_suit())
# deck = Deck()
# deck.shuffle_deck()
# for _ in range(deck.length()):
#     card = deck.take_top_card()
#     print(card.get_long_name())
