from Player import Player
import sys

class Lobby:
    class LobbyFull(Exception):
        def __init__(self):
            super().__init__("Lobby is full")

    class AlreadyConnected(Exception):
        def __init__(self):
            super().__init__("User is already connected")

    def __init__(self, uuid, maxUser = 8):
        self.__creator = None
        self.__uuid = uuid
        self.__players = []
        self.__maxUser = maxUser

    def isConnected(self, player):
        for i in self.__players:
            if (i.getName() == player.getName()):
                return True
        return False

    def addUser(self, player):
        if (self.isFull()):
            raise self.LobbyFull()
        else:
            if (self.isConnected(player)):
                raise self.AlreadyConnected()
            self.__players.append(player)

    def isFull(self):
        if len(self.__players) >= self.__maxUser:
            return True
        else:
            return False

    def getUUID(self):
        return self.__uuid

    def getCreator(self):
        return self.__creator

    def addCreator(self, creator):
        self.__creator = creator

    def getPlayers(self):
        return self.__players
