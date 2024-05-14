from datetime import datetime
import os

USUARIOS = {
    "0001": "Luiza Lopes Almeida",
    "0002": "Carlos Ribeiro de Jesus",
    "0003": "Tobias Souza Gomes"
}

AGENCIA = "AG-1357"

CONTA = "2468-12"

# saldo inicial da conta
saldo = 0

# limite maximo, que pode ser sacado de cada vez
limite = 500

# numero de saques que o usuário realizou naquele dia
numero_saques = 0

# numero máximo de saques, que o usuario pode fazer por dia
LIMITE_SAQUES = 3

separador = "=" * 50

operacoes = []

while True:
    menu = f"""
{separador}

Usuario: {USUARIOS["0003"]}
Agencia: {AGENCIA}
Conta:   {CONTA}
Saldo:   {saldo:.2f}

{separador}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

{separador}

"""

    opcao = input(menu)    

    data_atual = datetime.today().strftime("%d-%m-%Y %H:%M")

    if opcao == "d":
        # depositar
        
        # limpa o terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" Depositar ".center(50,"="))
        print("Responsável: {usuario}".format(usuario=USUARIOS["0003"]))
        print("Operação: Depósito")
        print( f"Data: {data_atual}".format(data_atual) )
        valor = input("Valor: ")
        valor = float(valor)

        if valor > 0:      
            # acrescenta o valor ao saldo      
            saldo += valor

            # limpa o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n")
            print("  Sucesso  ".center(50,"="))
            print(f"O valor de R$ {valor:.2f} foi depositado em sua conta.".format(valor=str(valor)))
            print(separador)


            operacoes.append({
                "operacao": "deposito",
                "status": "sucesso",
                "usuario": USUARIOS["0003"],
                "data_operacao": data_atual,
                "valor": valor,
                "saldo": saldo
            })            

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("\n")
            print("  Erro  ".center(50,"="))
            print(f"O valor o ser depositado deve ser maior que 0.")
            print(separador)

    
    elif opcao == "s":
        # sacar

        # verifica se o usuario ainda tem saques disponiveis
        if numero_saques >= 3:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n")
            print("  Erro  ".center(50,"="))
            print(f"Você atingiu o número máximo de saques.")
            print(separador)
        else:
            # limpa o terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" Sacar ".center(50,"="))
            print("Responsável: {usuario}".format(usuario=USUARIOS["0003"]))
            print("Operação: Saque")
            print( f"Data: {data_atual}".format(data_atual) )
            print("Saques realizados: {saques}".format(saques=numero_saques))
            valor = input("Valor: ")
            valor = float(valor)

            if valor > 0: 
                if saldo >= valor:
                    # verifica se o valor a ser sacado supera o limite definido.
                    if valor > limite:
                        os.system('cls' if os.name == 'nt' else 'clear')            
                        print("\n")
                        print("  Erro  ".center(50,"="))
                        print(f"O valor a ser sacado é maior que o seu limite.")
                        print(f"Limite por saque: R$ {limite:.2f}")
                        print(f"O valor que você deseja sacar: R$ {valor:.2f}")
                        print(separador)
                    else:
                        # subtrai o valor ao saldo      
                        saldo -= valor

                        # incrementa o numero de saques
                        numero_saques += 1

                        # limpa o terminal
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n")
                        print("  Sucesso  ".center(50,"="))
                        print(f"O valor de R$ {valor:.2f} foi sacado de sua conta.".format(valor=str(valor)))
                        print(separador)


                        operacoes.append({
                            "operacao": "saque",
                            "status": "sucesso",
                            "usuario": USUARIOS["0003"],
                            "data_operacao": data_atual,
                            "valor": valor,
                            "saldo": saldo
                        })    
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')            
                    print("\n")
                    print("  Erro  ".center(50,"="))
                    print(f"O valor o ser sacado deve ser menor ou igual ao saldo que você tem disponivel.")
                    print(f"Seu saldo atual é: {saldo:.2f}".format(saldo))
                    print(f"E o valor que você deseja sacar é: {valor:.2f}".format(valor))
                    print(separador)    
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print("\n")
                print("  Erro  ".center(50,"="))
                print(f"O valor o ser sacado deve ser maior que 0.")
                print(separador)
    
    elif opcao == "e":
        # extrato
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" Visualizar operações ".center(50,"="))
        print("Responsável: {usuario}".format(usuario=USUARIOS["0003"]))
        print("Operação: Extrato")
        print( f"Data: {data_atual}".format(data_atual) )

        response = ""

        if not operacoes:
            response += "Ainda não há operações, a serem exibidas."
        else:
            for operacao in operacoes:
                response += separador
                response += "\n"
                response += f"Operação: {operacao["operacao"]}\n"
                response += f"Status: {operacao["status"]}\n"
                response += f"Usuário: {operacao["usuario"]}\n"
                response += f"Data operação: {operacao["data_operacao"]}\n"
                response += f"Valor da operação: R$ {operacao["valor"]:.2f}\n"
                response += f"Saldo disponível após a operação: R$ {operacao["saldo"]:.2f}\n"
                response += separador
                response += "\n"

        print(response)
    
    elif opcao == "q":
        break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("A opção selecionada não é válida, por favor selecione um opção válida.")


