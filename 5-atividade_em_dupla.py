import os
os.system("cls")



import time

print("=== Gerador de Tabuada ===")

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    time.sleep(1)
