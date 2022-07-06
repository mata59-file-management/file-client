import socket

from constants import ADDRESS, DEPOSIT_ID, FORMAT, SIZE, UPLOAD_FOLDER_NAME


def deposit():
    # Getting the filename and fault tolerance level from the user
    file_name = ''
    while not file_name:
        print("O arquivo deve estar armazenado dentro da pasta uploads")
        print("Digite o nome do arquivo a ser enviado:")
        file_name = input()

    fault_tolerance_level = ''
    while not fault_tolerance_level:
        print("Digite o nível de tolerância a falhas desejado:")
        fault_tolerance_level = input()

    # Starting a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to the main server
    client.connect(ADDRESS)

    try:
        """ Opening and reading the file data. """
        file = open(f"{UPLOAD_FOLDER_NAME}/{file_name}", "rb")
        data = file.read()

        # Sending a identifier so that the server knows that it should perform a deposit
        client.send(DEPOSIT_ID.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        # Sending the file name to the server
        client.send(file_name.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the file data to the server. """
        client.send(data) # Sending binary files, do not encode
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the fault tolerance level to the server. """
        client.send(fault_tolerance_level.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Closing the file. """
        file.close()

    except FileNotFoundError:
        print("Arquivo não existe na pasta data")

    """ Closing the connection from the server. """
    client.close()
