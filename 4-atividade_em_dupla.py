import os
os.system("cls")

print("=== Mundo Eletro ===")

valor = float(input("Digite o valor do produto: R$ "))

print("\nFormas de pagamento:")
print("1 - À vista (10% de desconto)")
print("2 - A prazo (até 6 parcelas)")

forma = int(input("Escolha a forma de pagamento: "))

if forma == 1:
    desconto = valor * 0.10
    total = valor - desconto

    print("\n=== Resumo do pagamento ===")
    print("Forma de pagamento: À vista")
    print(f"Valor do produto: R$ {valor:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")

elif forma == 2:
    parcelas = int(input("Digite a quantidade de parcelas (1 a 6): "))

    if parcelas >= 1 and parcelas <= 6:
        desconto = 0
        total = valor
        valor_parcela = total / parcelas

        print("\n=== Resumo do pagamento ===")
        print("Forma de pagamento: A prazo")
        print(f"Valor do produto: R$ {valor:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
    else:
        print("Erro: a quantidade de parcelas deve ser de 1 a 6.")

else:
    print("Erro: forma de pagamento inválida.")
