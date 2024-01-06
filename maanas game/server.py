import socket, sys
from _thread import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip, port = "192.168.1.100", 5555

try:
    sock.bind((ip, port))
except socket.error as e:
    print(e)

sock.listen(2)
print("Started")

pos = [(360, 360, 0), (480, 360, 0)]


def rpos(ch):
    x = ch.split(",")
    return int(x[0]), int(x[1]), int(x[2])


def mpos(t):
    return str(t[0])+','+str(t[1])+','+str(t[2])


def thr(con, playerno):
    con.send(str.encode(mpos(pos[playerno])))
    while 1:
        try:
            k = rpos(con.recv(2048).decode())
            pos[playerno] = k

            if not k:
                print("Failed to connect")
                break
            else:
                if playerno:
                    ch = pos[0]
                else:
                    ch = pos[1]
            con.sendall(str.encode(mpos(ch)))
        except Exception as e:
            print(e)
    con.close()
    print("Disconnected")


def main():
    playerno = 0
    while 1:
        con, addr = sock.accept()
        print(f"Connected to {addr}")

        start_new_thread(thr, (con, playerno))
        playerno += 1


main()
