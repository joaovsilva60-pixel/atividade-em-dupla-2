import os
os.system("cls")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pesquisa_municipal():
    salarios = []
    filhos = []

    while True:
        limpar_tela()
        print("=" * 45)
        print("    PREFEITURA DE VILA NOVA - PESQUISA")
        print("=" * 45)
        print("1 – Adicionar família")
        print("2 – Sair e exibir resultados")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                limpar_tela()
                print("--- CADASTRAR FAMÍLIA ---")
                try:
                    salario = float(input("Digite o salário da família (R$): "))
                    qtd_filhos = int(input("Digite o número de filhos: "))

                    if salario < 0 or qtd_filhos < 0:
                        print("\n❌ Valores não podem ser negativos! Dados descartados.")
                    else:
                        salarios.append(salario)
                        filhos.append(qtd_filhos)
                        print("\n✅ Família cadastrada com sucesso!")
                except ValueError:
                    print("\n❌ Entrada inválida! Digite apenas números.")

                input("\nPressione ENTER para voltar ao menu...")

            case "2":
                break

            case _:
                print("\n❌ Opção inválida! Digite 1 ou 2.")
                input("\nPressione ENTER para continuar...")

    # Exibição dos Resultados
    limpar_tela()
    print("=" * 45)
    print("         RESULTADOS DA PESQUISA")
    print("=" * 45)

    total_familias = len(salarios)

    if total_familias > 0:
        media_salario = sum(salarios) / total_familias
        media_filhos = sum(filhos) / total_familias
        maior_salario = max(salarios)
        menor_salario = min(salarios)

        print(f"Total de famílias pesquisadas: {total_familias}")
        print(f"Média salarial:                R$ {media_salario:.2f}")
        print(f"Média de filhos por família:   {media_filhos:.1f}")
        print(f"Maior salário informado:       R$ {maior_salario:.2f}")
        print(f"Menor salário informado:       R$ {menor_salario:.2f}")
    else:
        print("Nenhuma família foi cadastrada na pesquisa.")

    print("=" * 45)

if __name__ == "__main__":
    pesquisa_municipal()