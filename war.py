import random


value = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13, 
    "Ace": 14,
}

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    def __init__(self):
        self.everycard = []

        for suit in suits:
            for rank in ranks:
                newcard = Card(suit, rank)
                
                self.everycard.append(newcard)

    def shuffle(self):
        random.shuffle(self.everycard)

    def deal(self):
        return self.everycard.pop()

class Player():

    def __init__(self, name):
        self.name = name
        self.everycard = []

    def remove(self):
        return self.everycard.pop(0)
    
    def add(self, additional):
        if type(additional) == type([]):
            self.everycard.extend(additional)
        else:
            self.everycard.append(additional)
        
    def __str__(self):
        return f'Player {self.name} has {len(self.everycard)} cards. '


p1 = Player("Wan")
p2 = Player("Tooh")
mydeck = Deck()
mydeck.shuffle()

for x in range(26):
    p1.add(mydeck.deal())
    p2.add(mydeck.deal())

playing = True
roundnum = 0

while playing == True:
    roundnum += 1
    print(f'round {roundnum}')

    if p1.everycard == []:
        print(f'Player {p1} is out of cards {p2} wins!!')
        playing = False
        break
        
    if p2.everycard == []:
        print(f'Player {p2} is out of cards {p1} wins!!')
        playing = False
        break

    p1card = []
    p1card.append(p1.remove())

    p2card = []
    p2card.append(p2.remove())

    atwar = True

    while atwar:
        if p1card[-1].value > p2card[-1].value:
            p1.add(p1card)
            p1.add(p2card)
            
            atwar = False

        elif p2card[-1].value > p1card[-1].value:
            p2.add(p1card)
            p2.add(p2card)

            atwar = False

        else:
            print("WAR, three cards drawn and fourth is flipped ")
            
            if len(p1.everycard) < 5:
                print("Player one has not enough cards")
                print("Player 2 wins")

                playing = False
                break

            elif len(p2.everycard) < 5:
                print("Player two has not enough cards")
                print("Player 1 wins")

                playing = False
                break

            else:
                for num in range(5):
                    p1card.append(p1.remove())
                    p2card.append(p2.remove())


