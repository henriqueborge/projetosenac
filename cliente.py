
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





