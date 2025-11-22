# Filtra a lista de usuários buscando um CPF. Retorna o objeto usuário se encontrado.
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Cria um novo usuário (cliente) se o CPF não estiver cadastrado.
def criar_usuario(usuarios):
    
    cpf = ""
    while True:
        cpf_input = input("Informe o CPF (somente números): ")
        
        # Validação de Formato
        if len(cpf_input) != 11 or not cpf_input.isdigit():
            print("\n--> CPF inválido! Deve conter exatamente 11 dígitos numéricos. Tente novamente. <--")
            continue
        
        # Validação de Existência
        usuario_existente = filtrar_usuario(cpf_input, usuarios)
        if usuario_existente:
            print("\n--> Já existe usuário com este CPF! Tente novamente. <--")
            continue
            
        cpf = cpf_input
        break
        
    # VALIDAÇÃO E COLETA DO NOME.
    nome = ""
    while True:
        nome_input = input("Informe seu nome completo: ")
        
        # Remove espaços e verifica se o restante é composto apenas por letras
        if all(char.isalpha() or char.isspace() for char in nome_input) and len(nome_input.strip()) > 0:
            nome = nome_input.title()
            break
        else:
            print("\n--> Nome inválido! Digite apenas letras (sem números ou caracteres especiais). <--")

    # VALIDAÇÃO E COLETA DA DATA DE NASCIMENTO.
    data_nascimento = ""
    while True:
        data_nascimento_input = input("Informe a data de nascimento (ddmmyyyy ou dd/mm/aaaa): ")
        
        # Limpa barras, hífens, etc., para verificar se o restante é numérico
        data_nascimento_numerica = data_nascimento_input.replace('-', '').replace('/', '').replace('.', '')
        
        if data_nascimento_numerica.isdigit() and len(data_nascimento_numerica) == 8:
            data_nascimento = f"{data_nascimento_numerica[0:2]}/{data_nascimento_numerica[2:4]}/{data_nascimento_numerica[4:8]}"
            break
        else:
            print("\n--> Data de nascimento inválida! Digite a data no formato ddmmyyyy (8 dígitos numéricos). <--")
    
    # COLETA E FORMATAÇÃO DO ENDEREÇO.
    # Endereço é o campo mais flexível, vamos apenas garantir o Title Case.
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ").title()

    # ARMAZENAMENTO.
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\n=== Usuário criado com sucesso! ===")
    print(f"\nDados salvos:\nNome: {nome}\nCPF: {cpf}\nData Nasc: {data_nascimento}\nEndereço: {endereco}")

# Cria uma nova conta corrente e a vincula a um usuário existente pelo CPF
def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n--- Usuário não encontrado, fluxo de criação de conta encerrado! ---")
        return None

    print("=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

# Lista de Contas cadastradas
def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas.")
        return

    print("\n============== CONTAS CADASTRADAS ==============")
    for conta in contas:
        usuario = conta['usuario']
        
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            
            --- Dados do Titular ---
            Nome:\t\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
            Nascimento:\t{usuario['data_nascimento']}
            Endereço:\t{usuario['endereco']}
        """
        print("=" * 40)
        print(linha)
    print("================================================")


# Depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")

    return saldo, extrato

# Saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n--- Operação falhou! Você não tem saldo suficiente. ---")
    elif excedeu_limite:
        print("\n--- Operação falhou! O valor do saque excede o limite. ---")
    elif excedeu_saques:
        print("\n--- Operação falhou! Número máximo de saques excedido. ---")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n--> Operação falhou! O valor informado é inválido. <--")

    return saldo, extrato, numero_saques

# Extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    # Constantes do Sistema
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    # Listas de Armazenamento
    usuarios = []
    contas = []

    # Variáveis de Estado da Conta
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    def menu():
        return input(f"""
    {"=" * 20} MENU {"=" * 20}
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair
    {"=" * 46}
    => """)


    while True:
        opcao = menu()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("--> Valor inválido. Digite um número. <--")
                continue
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("--> Valor inválido. Digite um número. <--")
                continue
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            nova_conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)
            if nova_conta:
                contas.append(nova_conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema. Volte sempre!")
            break

        else:
            print("\n--> Operação inválida, por favor selecione novamente a operação desejada. <--")

if __name__ == "__main__":
    main()