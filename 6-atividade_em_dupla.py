import os
os.system("cls")

print("=== Instituto Dados Já ===")

pares = 0
impares = 0
soma = 0

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número inteiro: "))

    soma += numero

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n=== Resumo dos números ===")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Soma de todos os números: {soma}")
