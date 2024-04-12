import socket
import sys #for command-line args

# Get and set address and port for connection
ADDR = sys.argv[1] # first command line argument is server address
PORT = int(sys.argv[2])

# create and instantiate a new socket with data stream options
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_sock.connect((ADDR, PORT))  

# commandline input
query = sys.argv[3] # second command line argument is client query

while True:
    
    # send query to server
    client_sock.send(query.encode())  
    
    # receive server response
    data = client_sock.recv(1024).decode()  

    # show server response
    print(data)  
    break
# close the connection
client_sock.close()  
