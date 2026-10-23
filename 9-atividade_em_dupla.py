import os
os.system("cls")
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def totem_sabor_da_terra():
    total_pagar = 0.0
    quantidade_pratos = 0

    while True:
        limpar_tela()
        print("=" * 45)
        print("       RESTAURANTE SABOR DA TERRA")
        print("=" * 45)
        print("CÓD. | PRATO                  | PREÇO")
        print("-" * 45)
        print(" 1   | Feijoada Completa      | R$ 35,00")
        print(" 2   | Frango a Passarinho    | R$ 28,00")
        print(" 3   | Carne de Sol com Aipim | R$ 42,00")
        print(" 4   | Moqueca de Peixe       | R$ 50,00")
        print(" 5   | Salada Tropical        | R$ 20,00")
        print("=" * 45)

        codigo = input("Digite o código do prato desejado: ").strip()

        # Tratamento do cardápio utilizando match-case
        match codigo:
            case "1":
                nome_prato = "Feijoada Completa"
                preco = 35.00
            case "2":
                nome_prato = "Frango a Passarinho"
                preco = 28.00
            case "3":
                nome_prato = "Carne de Sol com Aipim"
                preco = 42.00
            case "4":
                nome_prato = "Moqueca de Peixe"
                preco = 50.00
            case "5":
                nome_prato = "Salada Tropical"
                preco = 20.00
            case _:
                nome_prato = None
                preco = 0.00

        if nome_prato:
            quantidade_pratos += 1
            total_pagar += preco
            print(f"\n✅ {nome_prato} adicionado(a) com sucesso! (R$ {preco:.2f})")
        else:
            print("\n❌ Código inválido! Nenhum prato selecionado.")

        # Pergunta de continuidade
        resposta = ""
        while resposta not in ["S", "N"]:
            resposta = input("\nDeseja outro prato? (S/N): ").strip().upper()

        if resposta == "N":
            break

    # Resumo final do pedido
    limpar_tela()
    print("=" * 45)
    print("          RESUMO DO SEU PEDIDO")
    print("=" * 45)
    print(f"Total de pratos pedidos: {quantidade_pratos}")
    print(f"Total a pagar:           R$ {total_pagar:.2f}")
    print("=" * 45)
    print("Obrigado pela preferência! Bom apetite! 🌿")


if __name__ == "__main__":
    totem_sabor_da_terra()