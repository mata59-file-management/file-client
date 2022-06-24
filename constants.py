import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDRESS = (IP, PORT)

SIZE = 1024
FORMAT = "utf-8"


FILE_NAME = "yt.txt"  # File must be inside the data folder
FAULT_TOLERANCE_LEVEL = "1"  # Number of copies to be made on different servers

