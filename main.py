from deposit import deposit
from retrieve import retrieve


def main():

    while True:
        print("Digite o modo de operação:")
        print("1 - Depósito")
        print("2 - Recuperação")
        print("e - Finalizar execução")
        program_mode = input()
        if program_mode == "1":
            deposit()
        elif program_mode == "2":
            retrieve()
        else:
            break
        print("Operação concluída.")
        

if __name__ == "__main__":
    main()
