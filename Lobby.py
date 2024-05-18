import uuid as uuidGen

from Player import Player


class Lobby:
    def __init__(self, uuid, maxUser=8):
        self.__uuid = uuid
        self.__players = []
        self.__maxUser = maxUser

    def addUser(self, player: Player):
        if (self.isFull):
            raise Exception("Lobby is full")
        self.__players.append(player)

    def isFull(self):
        if len(self.__players) == self.__maxUser:
            return True
        else:
            return False

    def getUUID(self):
        return self.__uuid

    def getPlayers(self):
        return self.__players


class LobbyManager:
    def __init__(self):
        self.__lobby = []

    def createLobby(self, uuid):
        for i in self.__lobby:
            if (uuid == i.getUUID()):
                uuid = uuidGen.uuid4().__str__()[0:6]
        newLobby = Lobby(uuid)
        self.__lobby.append(newLobby)
        print(uuid)

    def get_lobbies(self):
        return self.__lobby
