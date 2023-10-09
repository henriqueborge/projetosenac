<<<<<<< HEAD

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





=======
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
>>>>>>> a7615cd5cefb0eb78d24152765100d7adbd30334
