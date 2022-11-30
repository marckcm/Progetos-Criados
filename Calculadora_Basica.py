while True:
    print()
    sair = input('DESEJA SAIR? [S] ou [N]\n')
    if sair == 'S' or sair == 's':
        break

    num_1 = input("DIGITE UM NUMERO E DE ENTER: ")
    op = input("DIGITE ENTRE OS OPERADORES '+ - * /' E DE ENTER: ")
    num_2 = input('DIGITE O SEGUNDO NUMERO E DE ENTER: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('VOCÊ PRECISA DIGITAR UM NUMERO.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if op == "+":
        print(num_1+num_2)
    elif op == "-":
        print(num_1-num_2)
    elif op == "/":
        print(num_1/num_2)
    elif op == "*":
        print(num_1*num_2)
    else:
        print("OPERADOR INVALIDO")



