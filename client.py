import socket
import sys
import time

from sqlalchemy import true

ClientSocket = socket.socket()
port = 1233

# if(len(sys.argv) < 2) :
#     print ('Usage : python chat_client.py hostname')
#     sys.exit()
ips = ['10.14.104.136','10.14.97.231']
cur_size = 1
temp = 0

cur_leader = 1

def bully():

    te = -1
    global cur_leader
    cur_leader=-1
    while true:
        ClientSocket = socket.socket()
        te = te+1
        # te = te%2
        if te == cur_size:
            return
        host = ips[te]

        print(f'Checking the server {ips[te]}')
        try:
            ClientSocket.connect((host, port))
            print(f"able to connect to host {host}")
            if te > cur_leader:
                cur_leader = te
                # bully()
        except socket.error as e:
            continue

        Response = ClientSocket.recv(1024)

        # Input = f"Checking {ind}"
        # ClientSocket.send(str.encode(Input))
        # Response = ClientSocket.recv(1024)
        # Resp = Response.decode('utf-8')
        # Resp = Resp[13:]
        # if Resp == Input:
        #     print(f"checking server {ind+1} Yes")
        # else:
        #     print("No")
    # print(f'{type(Resp)}    {type(Input)}')
    # print(f'{len(Resp)}    {len(Input)}')
    # print(f'{Resp}  {Input}')

        ClientSocket.close()
        time.sleep(0.5)

def check():
    try:
        global temp
        global cur_leader
        ind=-1
        while true:
            ClientSocket = socket.socket()
            ind = ind+1
            ind = ind%cur_size
            temp = ind
            host = ips[ind]

            print(f'Waiting for connection to {ips[ind]}')
            try:
                ClientSocket.connect((host, port))
            except socket.error as e:
                if cur_leader!= ind:
                    ClientSocket.close()
                    time.sleep(2)
                    continue
                else:
                    print("here ", flush=True)
                    low=0
                    bully()
                    print(f"New leader here 1found is {cur_leader+1}")
                    continue

            Response = ClientSocket.recv(1024)
            Input = f"Checking {ind}"
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
            Resp = Response.decode('utf-8')
            Resp = Resp[13:]
            if ind > cur_leader:
                cur_leader = ind
            if Resp == Input:
                print(f"leader is {cur_leader+1}    server {ind+1} Yes")
            else:
                print("No")
            # print(f'{type(Resp)}    {type(Input)}')
            # print(f'{len(Resp)}    {len(Input)}')
            # print(f'{Resp}  {Input}')

            ClientSocket.close()
            time.sleep(2)

    except:

        if temp != cur_leader:
            check()
        else:
            bully()
            print(f"New leader found is {cur_leader+1}")
            check()

if __name__=="__main__":
    # ips = ['10.14.99.6','10.14.105.70']
    # cur_size = 1
    # ind = 0

    # cur = 1
    # low = 0

    check()
