import uuid as uuidGen
from . import *
class LobbyManager:
    def __init__(self):
        self.__lobby = []

    def generateUUID(self):
        return uuidGen.uuid4().__str__()[0:5]

    def alreadyExist(self, lobbyID):
        for i in self.__lobby:
            if (i.getUUID() == lobbyID):
                return True
        return False

    def createLobby(self, lobbyID):
        lobbyID = lobbyID.upper()
        while (self.alreadyExist(lobbyID) == True):
            lobbyID = self.generateUUID().upper()
        newLobby = Lobby(lobbyID)
        self.__lobby.append(newLobby)
        return newLobby

    def get_lobbies(self):
        return self.__lobby


lobby_manager = LobbyManager()
