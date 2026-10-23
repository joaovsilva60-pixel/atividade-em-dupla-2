import os
os.system("cls")

print("=== Atacarejo Bom Preço ===")

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
preco = float(input("Digite o preço unitário: R$ "))

total = quantidade * preco

if quantidade <= 5:
    percentual = 0.02
elif quantidade <= 10:
    percentual = 0.03
else:
    percentual = 0.05

desconto = total * percentual
total_pagar = total - desconto

print("\n=== Resumo da compra ===")
print(f"Produto: {produto}")
print(f"Total da compra: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f} ({percentual * 100:.0f}%)")
print(f"Total a pagar: R$ {total_pagar:.2f}")
