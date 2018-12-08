import util

class User:

    def __init__(self, id, name, conn):
        self.authorised = False
        self.id = id
        self.name = name
        self.conn = conn

        #for game
        self.score = 0
        self.lobby = None

    def sendMsg(self, msg):
        self.conn.send(util.sb(msg))

    def closeLobby(self):
        if self.lobby is None: return

        self.lobby.endGame()

