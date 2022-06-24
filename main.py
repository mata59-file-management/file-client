from deposit import deposit


def main():

    print("Digite o modo de operação:")
    print("1 - Depósito")
    print("2 - Recuperação")
    program_mode = input()

    if program_mode == "1":
        deposit()


if __name__ == "__main__":
    main()
