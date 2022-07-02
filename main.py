from deposit import deposit
from retrieve import retrieve


def main():

    print("Digite o modo de operação:")
    print("1 - Depósito")
    print("2 - Recuperação")
    program_mode = input()

    if program_mode == "1":
        deposit()
    elif program_mode == "2":
        retrieve()
        

if __name__ == "__main__":
    main()
