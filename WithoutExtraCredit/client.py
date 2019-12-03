import socket
import pickle
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.1.33.124', 9003))
client_socket.send("0".encode())  # flag

indices=[]

print("Server's list:", pickle.loads(client_socket.recv(1024)))
i = input("Enter index i:")
j = input("Enter index j:")
timestamp = datetime.now() # timestamp
indices.append(i)
indices.append(j)
indices.append(timestamp.year)
indices.append(timestamp.month)
indices.append(timestamp.day)
indices.append(timestamp.hour)
indices.append(timestamp.minute)
indices.append(timestamp.second)
indices.append(timestamp.microsecond)
indices_string= pickle.dumps(indices)	# sending indices and timestamp
client_socket.send(indices_string)
client_socket.close()
