from dataclasses import dataclass

estado_programa = True

lista_de_produtos = []

total_de_produtos = 0

id_produto = 1

@dataclass
class Product:
    id: int
    title: str
    description: str
    price: float
    quantity: int

while estado_programa:
    print('\n ----------------------------->')

    print('\nLista de produtos\n')

    print('1. Criar produto.') # Create
    print('2. Ler um produto.') # Read
    print('3. Atualizar um produto.') # Update
    print('4. Deletar um produto.') # Delete
    print('5. Visualizar a lista de produtos.') # Read all
    print('6. Limpar a lista de produtos.')  # Delete all
    print('7. Visualizar o total de produtos em estoque.')
    print('8. Encerrar o programa.')

    opcao = input('\nDigite um número (1-8): ')

    opcao = int(opcao)

    while opcao < 1 or opcao > 8:
        opcao = input('\nPor favor, digite um número de 1 a 8: ')
        opcao = int(opcao)

    match opcao:
        # CREATE
        case 1:
            produto_nome = input('\nDigite o nome do produto: ')
            produto_descricao = input('Digite a descrição do produto: ')
            produto_preco = float(input('Digite o valor do produto: '))
            produto_quantidade = int(input('Qual a quantidade do produto em estoque? '))

            new_product = Product(id_produto, produto_nome, produto_descricao, produto_preco, produto_quantidade)

            lista_de_produtos.append(new_product)

            print('\nProduto adicionado com sucesso!')

            id_produto += 1
        # READ
        case 2:
            if len(lista_de_produtos) == 0:
                print('\nA lista de produtos está vazia!')
            else:
                produto_id = int(input('\nDigite o id do produto a ser visualizado: \n'))
                for produto in lista_de_produtos:
                    if produto_id == produto.id:
                        print(produto)
        # UPDATE
        case 3:
            if len(lista_de_produtos) == 0:
                print('\nA lista de produtos está vazia!')
            else:
                produto_id = int(input('\nDigite o id do produto a ser atualizado: '))
                for produto in lista_de_produtos:
                    if produto_id == produto.id:
                        print(produto)

                        print('\n1. Título')
                        print('2. Descrição')
                        print('3. Preço')
                        print('4. Estoque')
                        print('5. Atualizar outro produto')
                        print('6. Finalizar\n')

                        opcao = int(input('Qual informação será atualizada?\n'))
                        # IMPLEMENTAR
                        match opcao:
                            case 1:
                                print('Atualizar o título.')
                            case 2:
                                print('Atualizar a descrição.')
                            case 3:
                                print('Atualizar o preço.')
                            case 4:
                                print('Atualizar o estoque.')
        # DELETE
        case 4:
            if len(lista_de_produtos) == 0:
                print('\nA lista de produtos está vazia!')
            else:
                produto_id = int(input('\nDigite o id do produto a ser removido: '))
                for produto in lista_de_produtos:
                    if produto_id == produto.id:
                        lista_de_produtos.remove(produto)
                        print('\nProduto removido com sucesso!')
        # MOSTRAR LISTA
        case 5:
            if len(lista_de_produtos) == 0:
                print('\nA lista de produtos está vazia!')
            else:
                print('\nAqui está a lista de produtos: \n')
                for produto in lista_de_produtos:
                    print(f'{lista_de_produtos.index(produto) + 1}. {produto}')
        # ESVAZIAR LISTA
        case 6:
            print('\nLista esvaziada com sucesso!')
            lista_de_produtos.clear()
        # TOTAL DE PRODUTOS EM ESTOQUE
        case 7:
            print('\nTotal de produtos em estoque:')

            if len(lista_de_produtos) == 0:
                print('\nA lista de produtos está vazia!')
            else:
                for produto in lista_de_produtos:
                    total_de_produtos += produto.quantity
                print(f'\n{total_de_produtos} unidade(s).')
        # ENCERRAR O PROGRAMA
        case 8:
            print('Programa finalizado.')
            estado_programa = False
        # DEFAULT
        case _:
            print('Opção inexistente!')
