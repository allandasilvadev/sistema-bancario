def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente. ")

    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excede o limite. ")

    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido. ")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n Operação falhou! O valor informado é inválido. ")

    return saldo, extrato