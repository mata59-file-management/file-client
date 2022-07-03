import socket

from constants import ADDRESS, DOWNLOAD_FOLDER_NAME, FORMAT, RETRIEVE_ID, SIZE


def retrieve():
    # Getting the filename from the user
    file_name = ''
    while not file_name:
        print("Digite o nome do arquivo a ser resgatado (incluir extensão):")
        file_name = input()

    # Starting a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to the main server
    client.connect(ADDRESS)

    # Sending a identifier so that the server knows that it should perform a retrieval operation
    client.send(RETRIEVE_ID.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"# Server: {msg}")

    # Sending the file name to the server
    client.send(file_name.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"# Server: {msg}")

    # Receiving the response from the server
    # OK - File found
    # NOT_FOUND - File not found
    ack = client.recv(SIZE).decode(FORMAT)
    client.send("Acknowledgment received".encode(FORMAT))

    if ack == "OK":
        # Receiving the file data from the server
        file_data = client.recv(SIZE)
        # print(f"# File data: {file_data}#")
        client.send("File data received".encode(FORMAT))

        file = open(f"{DOWNLOAD_FOLDER_NAME}/{file_name}", "wb")
        print(f"# Recebendo os dados do arquivo #")
        file.write(file_data)
        file.close()  
    else:
        print("-- Arquivo não encontrado nos servidores --")



