from . import *

HEAL = 0
DAMAGE = 1

class Player:
    def __init__(self, name, life=20):
        self.__name = name
        self.__life = life
        self.__cards = []
        self.asGamble= False

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getLife(self):
        return self.__life

    def setLife(self, life):
        self.__life = 20 if life > 20 else life

    def setAsGamble(self, value):
        self.asGamble = value

    def getAsGamble(self):
        return self.asGamble

    def addCard(self, card):
        self.__cards.append(card)

    def generateCard(self):
        card = Card.generateRandom()
        self.__cards.append(card)
