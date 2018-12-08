from lobbyManager import LobbyManager


class GameHandler:

    def __init__(self, server):
        self.server = server
        self.lobbyManage = LobbyManager()

    def handle(self, command, user):
        cmd = command[0]

        if cmd == "rdy":
            self.lobbyManage.addUser(user)

        if cmd == "set":
            self.lobbyManage.findLobbyByUser(user).setScore(user, int(command[1]))