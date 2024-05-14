import os

USUARIOS = {
    "0001": "Luiza Lopes Almeida",
    "0002": "Carlos Ribeiro de Jesus",
    "0003": "Tobias Souza Gomes"
}

AGENCIA = "AG-1357"

CONTA = "2468-12"

separador = "=" * 50

menu = f"""
{separador}

Usuario: {USUARIOS["0003"]}
Agencia: {AGENCIA}
Conta:   {CONTA}

{separador}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

{separador}

"""


while True:
    opcao = input(menu)    

    if opcao == "q":
        break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("A opção selecionada não é válida, por favor selecione um opção válida.")


