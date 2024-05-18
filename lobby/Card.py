import random

class Card:
    @staticmethod
    def isInBound(minValue, maxValue, value):
        if (value >= minValue and value < maxValue):
            return True
        else:
            return False

    @staticmethod
    def generateRandom():
        value = random.randint(0, 100)
        if (Card.isInBound(0, 25, value)):
            return 1
        if (Card.isInBound(25, 50, value)):
            return 2
        if (Card.isInBound(50, 70, value)):
            return 3
        if (Card.isInBound(70, 85, value)):
            return 4
        if (Card.isInBound(85, 95, value)):
            return 5
        if (Card.isInBound(95, 101, value)):
            return 6
        return 6
