import pygame
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.178.80", 5000))


ready = False
while not ready:
    ans = input("Type Ready to get Ready")
    if str(ans).lower() == "ready":
        ready = True
        s.send("Ready".encode('utf-8'))

while True:
    msg = s.recv(1024).decode('utf-8')
    if msg.lower().__contains__('start'):
        break

done = False
dead = False
pygame.init()

while True:
    inp = input('Died test')
    if inp.lower() == 'dead':
        s.send('Died'.encode('utf-8'))
    else:
        print('no')