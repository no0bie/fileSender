import socket,time

HOST = "localhost"  # The server's hostname or IP address
PORT = 5000        # The port used by the server

fileLoc = []
fileName = ""
fileNum = int(input("File count: "))

while fileNum > 0:
    fileLoc.append(input("Location: "))
    fileNum -= 1

for files in fileLoc:
    fileName += files.split("\\")[len(files.split("\\"))-1] + "\\"

with socket.socket() as s:
    s.connect((HOST, PORT))

    s.send(fileName.encode())
    time.sleep(0.5)
    for files in fileLoc:
        fileToSend = open(files,'rb')
        print('Sending ' + files)
        partOfFile = fileToSend.read(1024)
        while (partOfFile):
            s.sendall(partOfFile)
            partOfFile = fileToSend.read(1024)
        fileToSend.close()
        s.recv(1024)
    print(s.recv(1024).decode())
