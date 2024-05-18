HEAL = 0
DAMAGE = 1

class Player:
    def __init__(self, name, life=20):
        self.__name = name
        self.__life = life

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getLife(self):
        return self.__life

    def setLife(self, life):
        self.__life = life

    def __str__(self):
        return self.__name
