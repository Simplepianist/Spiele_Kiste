import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.56.1", 5000))
s.listen(1024)
players = 0
ready = 0
dead = 0


def client(csocket):
    global ready
    global dead
    global players
    send = False
    started = False
    died = False
    players += 1
    while True:
        try:
            reply = "Waiting"
            ans = csocket.recv(1024).decode("utf-8")
            if ans == "Close":
                csocket.close()
                players-=1
                dead-=1
                ready-=1
            if ans == "Ready":
                if not send:
                    ready += 1
                    send = True

                if ready == players and players != 0 and players != 1 and not started:
                    reply = "Start"
                    for i in range(players):

                        csocket.sendall(reply.encode("utf-8"))
                    started = True
            elif ans == "Died" and not died:
                place = players - dead
                dead += 1
                reply = str(place) + ". Place"
                died = True
                csocket.sendall(reply.encode("utf-8"))
                csocket.sendall(reply.encode("utf-8"))
            if reply == "Died" and not died:
                died = True
                if players == 1:
                    csocket.sendall("1. Place".encode("utf-8"))
                    csocket.sendall("1. Place".encode("utf-8"))
                    players = 0
                    ready = 0
                    dead = 0

                break
            if died and reply == "Waiting":
                place = players - dead
                reply = str(place) + ". Place"
            csocket.sendall(reply.encode("utf-8"))

        except:
            break



while True:
    csocket, addr = s.accept()
    start_new_thread(client, (csocket,))
