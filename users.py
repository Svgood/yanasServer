import util

class User:

    def __init__(self, id, name, conn):
        self.authorised = False
        self.id = id
        self.name = name
        self.conn = conn

        #for game
        self.score = 0

    def sendMsg(self, msg):
        self.conn.send(util.sb(msg))

