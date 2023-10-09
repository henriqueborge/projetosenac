
#cadastrar cliente
#funçao para ler arquivo
#funçao para editar
#funçao para deletar
def deletar_cliente(clientes, email): #foi criado a funçao de deletar
    cliente_encontrado = None  #none significa que se nao exister o cadastro, ele identifica e avisa que nao existe
    for cliente in clientes:
        if cliente['email'] == email:#a busca foi feita pelo email , porque por nome pode ter repetido
            cliente_encontrado = cliente 
            break

    if cliente_encontrado:
        clientes.remove(cliente_encontrado) #se encontrado o cliente, ativa a funçao remover
        print(f"Cliente com o email {email} foi deletado com sucesso.")

        # Atualize o arquivo CSV após a remoção
        gravar(clientes) 
    else:
        print(f"Cliente com o email {email} não encontrado.")
