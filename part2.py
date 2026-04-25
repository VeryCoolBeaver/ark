from pygame import*
from random import randint
from math import hypot
from socket import socket , AF_INET, SOCK_STREAM
from threading import Thread


my_data=list(map(int,sock.recv(64).decode().strip().split(",")))
my_id=my_data[0]
my_Player = Player(my_data[1],my_data[2],my_data[3],"Player")

all_players =[]
foods = [Food()for_in range(300)]

def recieve_data():
    globall all_players,running,lose
    while running:
        try:
            data=sock.recv(4096).decode().strip()
            if data =="LOSE":
                lose==True
            elif data:
                parts=data.strip('|').split('|')
                all_players=[list(map(int,p.split(",")))for p in parts if len(p.split(','))==4]
Thread(target=recieve_data,daemon=True).start()

for p in all_players:
    if p[0]== my_id:continue
    sx=int((p[]-my_players.x)*scale+WINDOW_SIZE[0]//2)
    sy=int((p[]-my_players.y)*scale+WINDOW_SIZE[1]//2)
    draw.circle(screen,(2,225,0),(sx,sy),int(p[3]*scale))
    