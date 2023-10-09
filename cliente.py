
import csv

def deletar_cliente(arquivo_csv, id_cliente):
    nova_lista_clientes = []

    
    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        
        for linha in reader:
            
            if linha['ID'] == id_cliente:
                continue  
            nova_lista_clientes.append(linha)  

    
    with open(arquivo_csv, mode='w', newline='') as file:
        
        campos = ['ID', 'Nome', 'Email', 'Telefone']

        
        writer = csv.DictWriter(file, fieldnames=campos)

        
        writer.writeheader()

       
        for linha in nova_lista_clientes:
            writer.writerow(linha)

    print(f"Cliente com ID {id_cliente} foi excluído com sucesso.")


arquivo_csv = 'clientes.csv'
id_cliente_a_deletar = '123' 
deletar_cliente(arquivo_csv, id_cliente_a_deletar)

import csv
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
    
        for clientee in clientes: #para navegar no dicionário
             writer.writerow([clientee["Nome"], clientee["Email"], clientee["Telefone"]])
            

def ler_dados_csv():
    with open('arquivo.csv', mode='r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            print(f"Nome:{linha['Nome']}, Email: {linha['Email']}, Telefone:{linha['Telefone']}")
    

while True:
    print("MENU\n"
        "1. cadastrar \n"
        "2. imprimir\n")
    opcao=int(input("escolha uma opção"))

    if opcao == 1:
        nome = input("nome do cliente: \n")
        email = input("Email do cliente:\n ")
        telefone = input("telefone do cliente:\n ")
        cadastrar_cliente(clientes,nome,email,telefone)
        criar_arquivo_csv()
    elif opcao == 2:
        ler_dados_csv()
#função cadastrar
#função para ler arquivo
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
        if cliente["nome"] == nome_cliente:
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            novo_telefone = input("Novo telefone: ")
            novos_valores = {'nome': novo_nome, 'email': novo_email, 'telefone': novo_telefone}
            clientes[i] = novos_valores
            editar_linha_csv('arquivo.csv', i + 1, [novo_nome, novo_email, novo_telefone])
            print("Dados do cliente atualizados com sucesso.")
            break
    else:
        print(f"Cliente com nome '{nome_cliente}' não encontrado.")
#função deletar arquivo

