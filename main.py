
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDRESS = (IP, PORT)

SIZE = 1024
FORMAT = "utf-8"


FILE_NAME = "yt.txt"  # File must be inside the data folder
FAULT_TOLERANCE_LEVEL = "1"  # Number of copies to be made on different servers


def main():
    """ Getting the filename and fault tolerance level from the user """
    print("O arquivo deve estar armazenado dentro da pasta data")
    print("Digite o nome do arquivo a ser enviado:")
    file_name = input()
    
    print("Digite o nível de tolerância a falhas desejado:")
    fault_tolerance_level = input()

    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDRESS)

    """ Opening and reading the file data. """
    try:
        file = open(f"data/{file_name}", "r")
        data = file.read()

        """ Sending the filename to the server. """
        client.send(file_name.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the file data to the server. """
        client.send(data.encode(FORMAT))
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


if __name__ == "__main__":
    main()
