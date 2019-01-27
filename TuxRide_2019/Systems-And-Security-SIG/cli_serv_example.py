import socket
from sys import argv

BUFFER_SIZE = 2048

def server(ip: str, port: int):
    
    # Acquire a socket
    serv_socket = socket.socket() 

    # Bind the socket to a particullar IP and Port
    serv_socket.bind((ip, port))

    # Start listening for new connections on the socket
    serv_socket.listen()

    print("Server Started. Listening for connections at %s:%d"%(ip, port))

    # On recieving a new connection request, accept the connection by dedicating a seperate socket for talking to the client.
    cli_sck, addr = serv_socket.accept()

    print("Connected to %s:%d"%addr)

    # Send-Recieve cycle
    recieved_message = cli_sck.recv(BUFFER_SIZE)
    print("Recieved : %s"%(recieved_message.decode()))
    send_message = input("Enter message : ")
    cli_sck.sendall(send_message.encode())
    print("Sent : %s"%send_message)

    # Close the connection
    cli_sck.close()

    serv_socket.close()

def client(ip: str, port: int):
    print("Client Started")
    # Acquire a new socket
    cli_socket = socket.socket()

    # Send a connection request to the specified  IP and Port
    cli_socket.connect((ip, port))
    
    print("Connected to %s:%d"%(ip, port))

    # Send-Recieve Cycle
    send_message = input("Enter message : ")
    cli_socket.sendall(send_message.encode())
    print("Sent : %s"%send_message)
    while True:
        recieved_message = cli_socket.recv(BUFFER_SIZE)
        if not recieved_message:
            break
        print("Recieved : %s"%(recieved_message.decode()))

    # Close the socket
    cli_socket.close()

def main():
    if len(argv) != 4:
        print("Usage : python3 cli_serv_example.py <server|client> <IP> <PORT>")
        return
    ip = argv[2]
    port = int(argv[3])
    if argv[1].lower() == "server":
        server(ip, port)
    if argv[1].lower() == "client":
        client(ip, port)

if __name__ == "__main__":
    main()
