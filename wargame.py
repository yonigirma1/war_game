#Card game using OOP Python

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play.
    """
    def __init__(self):
        print("creating a card")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("shuffling deck")
        shuffle(self.allcards)

    def slpit_in_half(self):
        print("splitting the cards")
        return(self.allcards[:26],self.allcards[26:])



class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return("contain {} cards").format(len(self.cards))

    def add_card(self,new_card):
        self.cards.extend(new_card)

    def remove_card(self):
        self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}").format(self.name,self.drawn_card)
        print(/n)
        return drawn_card

    def remove_war_cards(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hands.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0


#### GAME PLAY #######

print("Welcome to War, let's begin...")

#creating a new deck, shuffling and splitting into two parts
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#create two players
comp = player("computer",Hand(half1))
user = player(name,Hand(half2))

#set round counts
total_rounds = 0
war_counts = 0

#game play
while user.still_has_cards() and comp.still_has_cards:
    total_rounds += 1
    print("It is time for a new round and currently:")
    print(user.name+" has :"+ str(len(user.hand.cards)))
    print(comp.name+" has :"+ str(len(comp.hand.cards)))
    print("both players play a card")
    print('\n')

    #cards on the table
    table_cards = []

    #playing cards
    c_card = comp.play_card()
    u_card = user.play_card()

    #Add to table cards
    total_cards.append(c_card)
    total_cards.append(u_card)

    #checking if there is a war
    if c_card[1] == u_card[1]:
        war_counts += 1

        print("we have a match! time for war!!")
        print("Each player removes 3 cards face down and 1 caed face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        #playing cards
        c_card = comp.play_card()
        u_card = user.play_card()

        #Add to table cards
        total_cards.append(c_card)
        total_cards.append(u_card)

        #Checking who has a higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("The game lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
