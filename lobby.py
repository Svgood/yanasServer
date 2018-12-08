class Lobby:

    def __init__(self, user):
        self.users = []
        self.users.append(user)
        self.usersScoreSetted = 0
        self.onEnd = None

    def adduser(self, user):
        self.users.append(user)
        for user in self.users:
            user.score = 0
            user.sendMsg("start:;")

    def setScore(self, user, score):
        user.score = score
        self.usersScoreSetted += 1

        if self.usersScoreSetted < 2: return

        self.endGame()

    def endGame(self):
        user1 = self.users[0]
        user2 = self.users[1]

        user1.sendMsg("end:{};".format(user2.score))
        user2.sendMsg("end:{};".format(user1.score))

        if self.onEnd is None: return

        self.onEnd(self)


    def isFull(self):
        return len(self.users) > 1
