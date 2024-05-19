from . import *
from lobby.Player import Player


class Lobby:
    class LobbyFull(Exception):
        def __init__(self):
            super().__init__("Lobby is full")

    class AlreadyConnected(Exception):
        def __init__(self):
            super().__init__("User is already connected")

    def __init__(self, uuid, maxUser=8):
        self.__creator = None
        self.__uuid = uuid
        self.__players = {}
        self.__maxUser = maxUser
        self.__current = None

    def isConnected(self, player):
        for i in self.__players:
            if i.getName() == player.getName():
                return True
        return False

    def addUser(self, username: str):
        if self.isFull():
            raise self.LobbyFull()
        else:
            player = Player(username)
            self.__players[player.getName()] = player

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
        return [{"username": player.getName(), "life": player.getLife(), "asGamble": player.getAsGamble()} for player in self.__players]

    def getPlayer(self, username):
        for player in self.__players:
            if player.getName() == username:
                return player
        return None

    def getUsers(self):
        return list(self.__players.values())

    def setCurrent(self, username):
        self.__current = username

    def getCurrent(self):
        return self.__current

    def getNext(self):
        users = self.getUsers()
        if not users:
            return None

        current_index = next((index for index, player in enumerate(users) if player.getName() == self.__current), None)
        if current_index is None:
            self.__current = users[0].getName()
        else:
            next_index = (current_index + 1) % len(users)
            self.__current = users[next_index].getName()
        return self.__current
