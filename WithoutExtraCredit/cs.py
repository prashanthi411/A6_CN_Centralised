import socket
import threading
import pickle
from datetime import datetime
import datetime
from operator import itemgetter

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9000))
server_socket.listen(5)
print("Central Server is running!")

num_list = [0,1,2,3,4,5,6,7,8,9]
req=[]


def handle_client(client_socket):
    global req
    print("Server has connected!")
    print("Receiving request from server...")
    data = pickle.loads(client_socket.recv(1024))
    req.append(data)
    print("Received request:", req)
    print("Updating num_list...")
    print("Closing connection with server...")
    client_socket.close()
    print("Done!")


def start_sync():
    global num_list
    final_list=[]
    global req
    temp_list=[]
    p=0
    threading.Timer(30.0, start_sync).start()
    print("\n *** Syncing num_list with server ***")
    for r in req:
        tstamp=(datetime.datetime(r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
        temp_list.append(r[0])
        temp_list.append(r[1])
        temp_list.append(tstamp)
        final_list.append(temp_list)
        temp_list=[]

    final_list.sort(key=itemgetter(2))
    for f in final_list:
        i = int(f[0])
        j = int(f[1])
        temp = num_list[i]
        num_list[i] = num_list[j]
        num_list[j] = temp
        p=p+1
    
    req = final_list[p:]
    print("Current num_list:", num_list)
    cs_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs_as_client.connect(('10.1.33.124', 9001))
    cs_as_client.send("1".encode())  # flag
    print("Sending current num_list to server...")
    listtosend = pickle.dumps(num_list)
    cs_as_client.send(listtosend)
    cs_as_client.close()
    cs_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs_as_client.connect(('10.1.33.124', 9002))
    cs_as_client.send("1".encode())  # flag
    print("Sending current num_list to server...")
    listtosend = pickle.dumps(num_list)
    cs_as_client.send(listtosend)
    cs_as_client.close()
    cs_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs_as_client.connect(('10.1.33.124', 9003))
    cs_as_client.send("1".encode())  # flag
    print("Sending current num_list to server...")
    listtosend = pickle.dumps(num_list)
    cs_as_client.send(listtosend)
    cs_as_client.close()
    print("*** Sync completed! ***")


start_sync()

while True:
    client_socket, addr = server_socket.accept()
    print("\nGot connection from", addr)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
