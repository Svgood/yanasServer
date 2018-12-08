import socket
import threading
import time

import util
import config
import GameHandlers
import users


class Serv:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((config.host, config.port))

        self.conns = []
        self.users = []
        self.threads = []
        self.curThread = 0
        self.lobbiesId = 0
        self.usersId = 0

        self.gameHandler = GameHandlers.GameHandler(self)
        #self.preGameHandler = PreGameHandler(self)

        self.loggedUsers = {}

        util.printLog("started on {}".format(config.host))

    def listen(self):

        #alive checker
        t = threading.Thread(target=self.aliveChecker)
        t.start()

        while True:
            util.printLog("listening")
            self.sock.listen(128)
            conn, addr = self.sock.accept()
            self.conns.append(conn)

            usr = users.User(self.curThread, "NoName{}".format(self.curThread), conn)
            self.users.append(usr)

            util.printLog("Got connection from " + str(addr))

            t = threading.Thread(target=self.listenConn, args=(usr, conn))
            self.threads.append(t)
            t.start()

            self.curThread += 1

    def listenConn(self, user, con):
        while True:
            try:
                data = con.recv(1024)
            except:
                self.closeConnection(user, 1)
                return
            if not data:
                self.closeConnection(user, 1)
                return
            else:
                util.printLog("Got message from conn id: " + str(user.id))
                util.printLog(util.bs(data))
                if not self.msgHandler(user, util.bs(data)):
                    self.closeConnection(user)
                    return

    #Checking for dead connections
    def aliveChecker(self):
        while True:
            time.sleep(5)
            for user in self.users:
                #util.printLog("checking if alive")
                try:
                    user.sendMsg("?:;")
                except:
                    self.closeConnection(user, 1)

    #Handling messages from user
    def msgHandler(self, user, msg):
        if ";" in msg:
            msg = msg[:msg.find(";")]
        command = msg.split(":")
        cmd = command[0]

        if cmd == "closeConnection":
            return False

        #Game commands
        self.gameHandler.handle(command, user)

        return True


    def closeConnection(self, user, code=0):
        if code == 0:
            util.printLog("Closing connection - ok")
        else:
            util.printLog("Closing connection error")

        if user == None:
            return

        self.users.remove(user)
        try:
            user.conn.close()
        except:
            util.printLog("Closed already")





