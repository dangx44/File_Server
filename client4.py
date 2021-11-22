import socket
import sys

HOST = '127.0.0.1'
PORT = 65432
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024

def upld():
    file_name = input("Enter filename: " )
    #Open & read file
    f = open("data/" + file_name, "r")
    data = f.read()
    #Send filename to Server
    client.send(file_name.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    #Send file data to Server
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    #Close file
    f.close()
    #Close connection to Server
    client.close()

def dwld():
    #request to download file
    file_name = input("Enter file name: ")
    file_name_data = file_name.encode("utf-8")
    #send file downlaod reaquest
    client.send(file_name_data)
    #receive file info to download
    file_info = client.recv(1024)
    #file info decode
    info_decode = file_info.decode("utf-8")
    print(info_decode)
    #get file size
    #filesize = float(info_decode.split(': ')[2].split('MB')[0])
    #filesize2 = filesize*1024
    #write data to file
    with open(file_name, "wb") as f:
        while True:
            #loop to receive data
            file_data = client.recv(1024)
            if not file_data:
                break
            #received data
            elif file_data:
                #write data
                f.write(file_data)
               # cnum = cnum+1
                #new = cnum/filesize2*100
               # printi("Currently downloaded: %.2f%%"%new,end = "\r")
                #receiv complete

    client.close()

def lst():
    pass

if __name__ == "__main__":
    #Start TCP Socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Connect to Server
    client.connect(ADDR)

    while True:
        prompt = input("\nEnter command: ")
        if prompt[:4].upper() == "UPLD":
            upld()
        elif prompt[:4].upper() == "DWLD":
             dwld()
        elif prompt[:4].upper() == "LIST":
            lst()
