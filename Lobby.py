import uuid as uuidGen

from Player import Player

class Lobby:
    def __init__(self, uuid, maxUser = 8):
        self.__uuid = uuid
        self.__players = []
        self.__maxUser = maxUser

    def addUser(self, player: Player):
        if (self.isFull):
            raise Exception("Lobby is full")
        else:
            self.__players.append(player)

    def isFull(self):
        if (len(self.__players) == self.__maxUser):
            return True
        else:
            return False

    def getUUID(self):
        return self.__uuid

class LobbyManager:
    def __init__(self):
        self.__lobby = []

    def generateUUID(self):
        return uuidGen.uuid4().__str__()[0:5]

    def alreadyExist(self, uuid):
        for i in self.__lobby:
            if (i.getUUID() == uuid):
                return True
        return False

    def createLobby(self, uuid):
        uuid = uuid.upper()
        while (self.alreadyExist(uuid) == True):
            uuid = self.generateUUID().upper()
        newLobby = Lobby(uuid)
        self.__lobby.append(newLobby)
