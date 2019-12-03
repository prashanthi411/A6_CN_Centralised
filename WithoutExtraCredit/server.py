import socket
import threading
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9001))
server_socket.listen(5)
print("Server is running!")

num_list=[0,1,2,3,4,5,6,7,8,9]


def handle_client(client_socket):
    global num_list
    choice = client_socket.recv(1).decode()  # flag to know whether client or cs is connecting
    if choice == "0":
        print("Client has connected!")
        print("Sending current list to client...")
        serverlist = pickle.dumps(num_list)
        clientsocket.send(serverlist)
        swaptuple = clientsocket.recv(1024) # receive i,j tuple
        req=pickle.loads(swaptuple)
        print("Receiving request from client...")
        print("Received request:", req[0],req[1])
        print("Closing connection with client...")
        client_socket.close()
        print("Sending request to central server...")
        server_as_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_as_client.connect(('localhost', 9000))
        server_as_client.send(swaptuple)
        print("Closing connection with central server...")
        server_as_client.close()
        print("Done!")
    else:
        print("Central server has connected to send request!")
        print("Receiving updated list...")
        num_list = pickle.loads(client_socket.recv(1024))
        print("New list:", num_list)
        print("Done!")


while True:
    client_socket, addr = server_socket.accept()
    print("\nGot connection from", addr)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
