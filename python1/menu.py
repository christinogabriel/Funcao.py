from soma import soma
from dividir import dividir
from multiplicar import multiplicar
from subtrair import subtrair
def menu():
    """
    Menu das operações matemáticas
    :return: float
    """
    op = None
    while op != "5":
        print("Digite uma das opções")
        print("1 - SOMAR")
        print("2 - SUBTRAIR")
        print("3 - MULTIPLICAR")
        print("4 - DIVIDIR")
        print(" 5 - SAIR")
        op = input("Opção: ")
        if op == "1":
            a = float(input("Digite Valor 1: "))
            b = float(input("Digite Valor 2: "))
            print("A soma é: ", soma(a,b))
        elif op == "2":
            a = float(input("Digite Valor 1: "))
            b = float(input("Digite Valor 2: "))
            print("Subtração é: ", subtrair(a,b))
        elif op == "3":
            a = float(input("Digite Valor 1: "))
            b = float(input("Digite Valor 2: "))
            print("A multiplicação é: ", multiplicar(a, b))
        elif op == "4":
            a = float(input("Digite Valor 1: "))
            b = float(input("Digite Valor 2: "))
            print("A divisão é: ", dividir(a, b))
        else:
            print(" Você digitou 5... Byeeeeeeeeee")


menu()