import random, os, sys

cardName = {1: 'As', 2: 'Dos', 3: 'Tres', 4: 'Quatre', 5: 'Cinc', 6: 'Sis', 7: 'Set', 8: 'Vuit', 9: 'Nou',
            10: 'Deu', 11: 'Jota', 12: 'Reina', 13: 'Rei'}
cardSuit = {'c': 'Piques', 'h': 'Cors', 's': 'Espases', 'd': 'Diamants'}

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return (cardName[self.rank] + " de " + cardSuit[self.suit])

    def getRank(self):
        return (self.rank)

    def getSuit(self):
        return (self.suit)

    def BJValue(self):
        if self.rank > 9:
            return (10)
        else:
            return (self.rank)


def showHand(hand):
    for card in hand:
        print("    " + str(card))


def showCount(hand):
    print("Puntuació: " + str(handCount(hand)))


def handCount(hand):
    handCount = 0
    for card in hand:
        handCount += card.BJValue()
    return (handCount)

def gameEnd(score):
    print(color.BOLD +"Blackjack!! "+ color.END + "-*Puntuació*- maquina: " + str(score['maquina']) + " Puntuació jugador: " + str(score['jugador']))
    sys.exit(0)


deck = []
suits = ['c', 'h', 'd', 's']
score = {'maquina': 0, 'jugador': 0}
hand = {'maquina': [], 'jugador': []}

for suit in suits:
    for rank in range(1, 14):
        deck.append(Card(rank, suit))

keepPlaying = True

while keepPlaying:

    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)

    # Deal Cards

    hand['jugador'].append(deck.pop(0))
    hand['maquina'].append(deck.pop(0))

    hand['jugador'].append(deck.pop(0))
    hand['maquina'].append(deck.pop(0))

    playHuman = True
    bustedHuman = False

    while playHuman:
        print(color.RED + "---------------------------------------------------------" + color.END)
        print(color.BOLD + "_-*Blackjack*-_ "+ color.BLUE + "Maquina: " + str(score['maquina']) + color.PURPLE + " - Jugador: " + str(score['jugador']) + color.END)

        print()

        print(color.BOLD + "La maquina ha robat: " + color.END + str(hand['maquina'][-1]) )
        print()

        print(color.BOLD + "La teva ma:" + color.END)

        showHand(hand['jugador'])
        print()
        showCount(hand['jugador'])

        print()

        inputCycle = True
        userInput = ''

        while inputCycle:
            userInput = input("(U)na carta mes, (R)es mes, or (S)ortir: ").upper()
            if userInput == 'U' or 'S' or 'Q':
                inputCycle = False

        if userInput == 'U':
            hand['jugador'].append(deck.pop(0))
            if handCount(hand['jugador']) > 21:
                playHuman = False
                bustedHuman = True
        elif userInput == 'R':
            playHuman = False
        else:
            gameEnd(score)

    playComputer = True
    bustedComputer = False

    while not bustedHuman and playComputer:
        print(handCount(hand['maquina']))
        if handCount(hand['maquina']) < 17:
            hand['maquina'].append(deck.pop(0))
        else:
            playComputer = False

        if handCount(hand['maquina']) > 21:
            playComputer = False
            bustedComputer = True

    if bustedHuman:
        print(color.PURPLE + 'El jugador ha perdut' + color.END)
        score['maquina'] += 1
    elif bustedComputer:
        print(color.BLUE + 'La maquina ha perdut' + color.END)
        score['jugador'] += 1
    elif handCount(hand['jugador']) > handCount(hand['maquina']):
        print(color.PURPLE +'El jugador guanya' + color.END)
        score['jugador'] += 1
    else:
        print(color.BLUE + 'La maquina guanya' + color.END)
        score['maquina'] += 1

    print()
    print('Ma de la maquina:')
    showHand(hand['maquina'])
    showCount(hand['maquina'])

    print()
    print('Ma de l\'usuari')
    showHand(hand['jugador'])
    showCount(hand['jugador'])
    print()
    if input("(S)ortir o intro per jugar una nova ronda").upper() == 'S':
        gameEnd(score)

    deck.extend(hand['maquina'])
    deck.extend(hand['jugador'])

    del hand['maquina'][:]
    del hand['jugador'][:]