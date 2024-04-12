import socket
import os


# Get and set address and port for connection
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 5050
COUNT = 0

total_seats = 30 # all seats
booked_seats = 0 # number of seats booked
temp = " "

try:
    # create a new socket with data stream options
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind host address and port to the socket
    sock.bind((ADDR, PORT))  

    # listen for client connections (max queue 5)
    sock.listen(5)
    print(f"Server is running on {ADDR}, listening on port {PORT}")
except:
    print("Failed to establish connection!!")    

# function to handle bookings
def booking(query, COUNT):
    global booked_seats
    # reserve seat
    if query.lower() == "reserve":        
        # check if seats available
        if booked_seats == 30:            
            return("Failed Reservation.")            
        # book a seat and update available seats            
        else:    
            booked_seats = booked_seats + COUNT  
            available = total_seats - booked_seats
            return(f"Seat Reserved. Shuttle Bus now has {available} seats available.")
    # check available seats    
    elif query.lower() == "ask":
        if booked_seats == 30:            
            available = total_seats - booked_seats                
            return(f"Shuttle Bus has {available} seats available.")          
        else:
            booked_seats = booked_seats + COUNT
            available = total_seats - booked_seats
            return(f"Shuttle Bus has {available} seats available.")          
    else:
        return("Invalid arguments!!")    

        
while True:
    # accept new connections
    client_conn, address = sock.accept()  
    print("Connection from: " + str(address)+" established.")

    # receive data stream.
    data = client_conn.recv(1024).decode()        
    if not data:
        # break if no data received
        break
    # parse query to reservations function    
    temp = str(data)
    if(temp.lower() == "reserve"):
        COUNT = 1   
    else:
        COUNT = 0
        
    data = booking(temp,COUNT)
    # send function output to client
    client_conn.send(data.encode()) 
                          
    # close the connection
client_conn.close()  
