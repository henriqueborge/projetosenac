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
             break

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