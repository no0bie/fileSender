
import socket
import threading, time
import dbManager


def on_new_client(clientsocket,addr):
    clientsocket.settimeout(6)
    NameOf = clientsocket.recv(1024).decode()
    for name in NameOf[:-1].split("\\"):

        fileToWrite = open(name, "wb")
        fileContent = clientsocket.recv(1024)
        print("Receiving: " + name)
        while (fileContent):
            try:
                fileToWrite.write(fileContent)
                fileContent = clientsocket.recv(1024)
            except:
                break
        fileToWrite.close()
        time.sleep(1)
        clientsocket.send("done".encode())
        time.sleep(1)
    msg = "Saved files, code: "+str(dbManager.writeDB(NameOf[:-1]))
    clientsocket.send(msg.encode())
    clientsocket.close()

s = socket.socket()
host = "localhost"
port = 5000

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))
s.listen(5)
while True:
   c, addr = s.accept()
   print('Got connection from', addr)
   x = threading.Thread(target=on_new_client, args=(c,addr))
   x.start()
s.close()
