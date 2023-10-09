import csv
#função cadastrar
def cadastrar_cliente(clientes, nome , email, telefone):
    cliente ={
        'Nome': nome,
        'Email':email,
        'Telefone': telefone
    }
    clientes.append(cliente)
    print("suscesso!\n")
clientes=[] 
def criar_arquivo_csv():
    with open('arquivo.csv', mode="w", newline="") as arquivo_csv:
        writer=csv.writer(arquivo_csv) #criar um novo arquivo
        writer.writerow(["Nome","Email","Telefone"])
    
        for cliente in clientes: #para navegar no dicionário
             writer.writerow([cliente["Nome"], cliente["Email"], cliente["Telefone"]])
#função para ler arquivo
def ler_dados_csv():
    with open('arquivo.csv', mode='r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            print(f"Nome:{linha['Nome']}, Email: {linha['Email']}, Telefone:{linha['Telefone']}")
#função para editar arquivo
def editar_linha_csv(arquivo, linha, novos_dados):
    with open(arquivo, mode='r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        linhas = list(leitor_csv)

    linhas[linha] = novos_dados

    with open(arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in linhas:
            escritor_csv.writerow(linha)

def atualizar_cliente(clientes, nome_cliente):
    for i, cliente in enumerate(clientes):
        if cliente["Nome"] == nome_cliente:
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            novo_telefone = input("Novo telefone: ")
            novos_valores = {'Nome': novo_nome, 'Email': novo_email, 'Telefone': novo_telefone}
            clientes[i] = novos_valores
            editar_linha_csv('arquivo.csv', i + 1, [novo_nome, novo_email, novo_telefone])
            print("Dados do cliente atualizados com sucesso.")
            break
        else:
            print(f"Cliente com nome '{nome_cliente}' não encontrado.")
#função deletar arquivo

def deletar_cliente(clientes, email): #foi criado a funçao de deletar
    cliente_encontrado = None  #none significa que se nao exister o cadastro, ele identifica e avisa que nao existe
    for cliente in clientes:
        if cliente['Email'] == email:#a busca foi feita pelo email , porque por nome pode ter repetido
            cliente_encontrado = cliente 
            break

    if cliente_encontrado:
        clientes.remove(cliente_encontrado) #se encontrado o cliente, ativa a funçao remover
        print(f"Cliente com o email {email} foi deletado com sucesso.")

        # Atualize o arquivo CSV após a remoção
        criar_arquivo_csv(clientes) 
    else:
        print(f"Cliente com o email {email} não encontrado.")
        
while True:
    print(" Menu\n")
    print("1. cadastrar cliente")
    print("2. ler dados do cliente")
    print("3. atualizar dados")
    print("4. deletar cliente")
    print("5. sair")
    
    opcao = int(input("escolha uma opção: "))
    
    if opcao == 1:
        nome=input("digite nome: ")
        email=input("digite email: ")
        telefone=input("digite telefone: ")
        cadastrar_cliente(clientes, nome, email, telefone)
        criar_arquivo_csv()
        
    elif opcao == 2:
        ler_dados_csv()
        
    elif opcao == 3:
        print(" Menu de Atualização\n")
        print("1. Editar dados de um cliente")
        print("2. Voltar ao menu principal")

        opcao_atualizacao = int(input("Escolha uma opção de atualização: "))

        if opcao_atualizacao == 1:
            if opcao_atualizacao == 1:
                nome_cliente = input("Digite o nome do cliente que deseja editar: ")
            for i, cliente in enumerate(clientes):
                if cliente["Nome"] == nome_cliente:
                    novo_nome = input("Novo nome: ")
                    novo_email = input("Novo email: ")
                    novo_telefone = input("Novo telefone: ")
                    novos_valores = {'Nome': novo_nome, 'Email': novo_email, 'Telefone': novo_telefone}
                    editar_linha_csv('arquivo.csv', i + 1, [novo_nome, novo_email, novo_telefone])
                    clientes[i] = novos_valores
                    print("Dados do cliente atualizados com sucesso.")
                    break
                else:
                    print(f"Cliente com nome '{nome_cliente}' não encontrado.")
        elif opcao_atualizacao == 2:
            continue
        else:
       
                print("Opção inválida")
                
    elif opcao == 4:
        email = input("Digite o email do cliente que deseja deletar: ")
        deletar_cliente(clientes, email)
        criar_arquivo_csv(clientes)
        
        
    elif opcao == 5:
        print("saindo")
        break
    else:
        print("opção invalida")
