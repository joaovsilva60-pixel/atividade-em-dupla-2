import os
os.system("cls")


#SOLICITANDO DADOS
primeira_nota= float(input("Digite a primeira nota :"))
segunda_nota = float(input("Digite a segunda  nota :"))
terceira_nota = float(input("Digite a terceira nota :"))

#CALCULE  A MEDIA
media= (primeira_nota+segunda_nota+terceira_nota)/2

#EXIBE A MEDIA
print=input(f"\nMédia final :")

#verifica  a situação do aluno
if media>=7:
    print("Situação Aprovado:")
if media>=6:
    print("situação recuperação:")
elif media <5:
    print("aluno reprovado:")