import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.178.80", 5000))
s.listen(1024)
firstthree = {}
players = 0
ready = 0
dead = 0
running = False


def client(c):
    print("Connected")
    global players
    global ready
    global dead
    global running
    global firstthree
    ingame = False
    isready = False
    isdead = False
    while True:
        try:
            if running and not ingame:
                c.send("Running")
            else:
                if not isdead:
                    msg = c.recv(1024).decode('utf-8')
                    if not isready and str(msg).lower().__contains__("ready"):
                        ready += 1
                        isready = True
                    if ready == players and not ingame:
                        c.send("start".encode('utf-8'))
                        ingame = True
                        running = True
                    if str(msg).lower().__contains__("died"):
                        dead += 1
                        isdead = True
                        pos = players - dead
                        c.send(str(pos).encode('utf-8'))
                    if str(msg).__contains__("3:") or str(msg).__contains__("2:") or str(msg).__contains__("1:"):
                        name = str(msg).split(":")
                        firstthree[int(name[0])] = name[1]


        except:
            players -= 1
            if isready:
                ready -= 1
            if isdead:
                dead -= 1
            break


while True:
    c, addr = s.accept()
    c.send()
    start_new_thread(client, (c,))
