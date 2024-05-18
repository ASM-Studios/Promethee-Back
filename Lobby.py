import uuid as uuidGen
import sys

from Player import Player


class Lobby:
    def __init__(self, uuid, maxUser=8):
        self.__creator = None
        self.__uuid = uuid
        self.__players = []
        self.__maxUser = maxUser

    def addUser(self, player: Player):
        if self.isFull():
            raise Exception("Lobby is full")
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


class LobbyManager:
    def __init__(self):
        self.__lobby = []

    def createLobby(self, uuid):
        newLobby = Lobby(uuid)
        self.__lobby.append(newLobby)
        return newLobby

    def get_lobbies(self):
        return self.__lobby
