import os
os.system("cls")

print("=== Financeira Confia ===")

renda = float(input("Digite a renda mensal do cliente: R$ "))
emprestimo = float(input("Digite o valor do empréstimo solicitado: R$ "))
prestacoes = int(input("Digite o número de prestações: "))

valor_prestacao = emprestimo / prestacoes

print(f"\nValor da prestação: R$ {valor_prestacao:.2f}")

if emprestimo <= renda * 10 and valor_prestacao <= renda * 0.30:
    print("Crédito aprovado!")
else:
    print("Crédito negado!")
