import os
os.system("cls")
print("===Calculadora CrediFácil===")

num1=float(input("Digite o primeiro numero: "))
num2=float(input("Digiteo segundo numeoro: "))

operador=input("Digite o operador(+,-,* ou/):")
match operador:
    case "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")

    case "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")

    case "*":
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")

    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Aviso: não é possível dividir por zero!")

    case _:
        print("Aviso: operador inválido!")
        