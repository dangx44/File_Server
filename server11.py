#Server11

import os
import socket
import threading

IP = '127.0.0.1'
PORT = 4466
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the File Server.".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]
        
        if cmd == "HELP":
            send_data = "OK@"
            send_data += "LIST: List all files from server.\n"
            send_data += "UPLOAD <path>: Upload file to server.\n"
            send_data += "DELETE <filename>: Delet file from server.\n"
            send_data += "LOGOUT: Disconnect from server.\n"
            send_data += "HELP: List all commands."

            conn.send(send_data.encode(FORMAT))

        elif cmd == "LOGOUT":
            break
        
        elif cmd == "LIST":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"

            if len(files) == 0:
                send_data += "Directory empty."
            else:
                send_data += "\n".join(f for f in files)
            conn.send(send_data.encode(FORMAT))

        elif cmd == "UPLOAD":
            name = data[1]
            text = data[2]

            filepath = os.path.join(SERVER_DATA_PATH, name)
            with open(filepath, "w") as f:
                f.write(text)

            send_data = "OK@File uploaded."
            conn.send(send_data.encode(FORMAT))

        elif cmd == "DELETE":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"
            filename = data[1]

            if len(files) == 0:
                send_data += "Directory empty."
            else:
                if filename in files:
                    os.system(f"rm {SERVER_DATA_PATH}/{filename}")
                    send_data += "File deleted."
                else:
                    send_data += "File not found."
            conn.send(send_data.encode(FORMAT))

    print(f"[DISCONNECTED] {addr} Disconnected.")


def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
