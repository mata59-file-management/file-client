import socket

from constants import ADDRESS, FORMAT, RETRIEVE_ID, SIZE


def retrieve():
    # Getting the filename and fault tolerance level from the user
    print("Digite o nome do arquivo a ser resgatado (incluir extensão):")
    file_name = input()

    # Starting a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to the main server
    client.connect(ADDRESS)

    # Sending a identifier so that the server knows that it should perform a retrieval operation
    client.send(RETRIEVE_ID.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # A CONTINUAR

    # # Sending the file name to the server
    # client.send(file_name.encode(FORMAT))
    # msg = client.recv(SIZE).decode(FORMAT)
    # print(f"[SERVER]: {msg}")
