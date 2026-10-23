import os
os.system("cls")





def limpar_tela():
    """Limpa o console de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')


def portal_clinica_vidaplena():
    print("=== CLINICA VIDAPLENA - CADASTRO DE ACESSO ===")

    # 1. Cadastro de credenciais
    login_cadastrado = input("Cadastre seu login: ").strip()
    senha_cadastrada = input("Cadastre sua senha: ").strip()

    # Limpa a tela após o cadastro
    limpar_tela()

    print("=== CLINICA VIDAPLENA - LOGIN DE ACESSO ===")
    print("Cadastro realizado com sucesso! Por favor, confirme suas credenciais.\n")

    tentativas_restantes = 3

    # 2. Loop de autenticação (no máximo 3 tentativas)
    while tentativas_restantes > 0:
        login_informado = input("Digite seu login: ").strip()
        senha_informada = input("Digite sua senha: ").strip()

        # Verifica se login e senha estão corretos
        if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
            limpar_tela()
            print("===========================================")
            print(f"  SEJA BEM-VINDO(A) À CLÍNICA VIDAPLENA!  ")
            print("===========================================")
            print(f"Olá, {login_cadastrado}! Acesso concedido com sucesso.")
            return

        # Em caso de erro:
        tentativas_restantes -= 1
        limpar_tela()

        print("=== CLINICA VIDAPLENA - LOGIN DE ACESSO ===")

        if tentativas_restantes > 0:
            print(f"❌ Login ou senha incorretos!")
            print(
                f"Tentativas restantes: {tentativas_restantes}. Tente novamente.\n"
            )
        else:
            # 3. Bloqueio e encerramento após 3 tentativas
            print("❌ LOGIN E SENHA INCORRETOS!")
            print("===========================================")
            print(" Acesso BLOQUEADO! Limite de 3 tentativas excedido.")
            print(" O sistema foi encerrado.")
            print("===========================================")


if __name__ == "__main__":
    portal_clinica_vidaplena()