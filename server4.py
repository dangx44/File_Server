import socket

HOST = '127.0.0.1'
PORT = 65432
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
        print("[STARTING] Server is starting.")
        #Start TCP Socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Bind HOST & PORT to Server
        server.bind(ADDR)
        #Server listening for client to connect
        server.listen()
        print("[Listening] Server is listening.")

        while True:
            #Server accepts connection from client
            conn, addr = server.accept()
            print(f"[NEW CONNECT] {addr} connected.")
            #Receives filename from client
            filename = conn.recv(SIZE).decode(FORMAT)
            print("[RECV] Filename received.")
            file = open(filename, "w")
            conn.send("Filename received.".encode(FORMAT))
            #Receives file data from client
            data = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] File data received.")
            file.write(data)
            conn.send("File data received.".encode(FORMAT))
            #Close file
            file.close()
            #Cllse client connection
            conn.close()
            print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()
