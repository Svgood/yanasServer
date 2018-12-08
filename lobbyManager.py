import lobby
import util

class LobbyManager:

    def __init__(self):
        self.lobbies = []

    def addUser(self, user):
        createdLobby = self.getNotFilledLobby()
        if createdLobby is None:
            createdLobby = lobby.Lobby(user)
            createdLobby.onEnd = self.onLobbyEnd
            self.lobbies.append(createdLobby)
            return
        createdLobby.adduser(user)

    def getNotFilledLobby(self):
        for lobby in self.lobbies:
            if not lobby.isFull():
                return lobby
        return None

    def onLobbyEnd(self, lobby):
        util.printLog("Removed lobby")
        self.lobbies.remove(lobby)

    def findLobbyByUser(self, user):
        for lobby in self.lobbies:
            if user in lobby.users:
                return lobby
        return None