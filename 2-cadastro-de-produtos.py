from dataclasses import dataclass

estado_programa = True

lista_de_produtos = []

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

    print('1. Visualizar a lista.')
    print('2. Adicionar um produto.')
    print('3. Remover um produto.')
    print('4. Limpar a lista.')
    print('5. Encerrar o programa.')

    opcao = input('\nDigite um número(1-5): ')
    opcao = int(opcao)

    while opcao < 1 or opcao > 5:
        opcao = input('\nPor favor, digite um número de 1 a 5: ')
        opcao = int(opcao)

    match opcao:
        case 1:
            if len(lista_de_produtos) == 0:
                print('\nA lista de produtos está vazia!')
            else:
                print('\nAqui está a lista de produtos: \n')
                for produto in lista_de_produtos:
                    print(f'{lista_de_produtos.index(produto) + 1}. {produto}')
        case 2:
            produto_nome = input('Digite o nome do produto: ')
            produto_descricao = input('Digite a descrição do produto: ')
            produto_preco = float(input('Digite o valor do produto: '))
            produto_quantidade = int(input('Qual a quantidade do produto em estoque? '))

            new_product = Product(id_produto, produto_nome, produto_descricao, produto_preco, produto_quantidade)

            lista_de_produtos.append(new_product)

            print('Produto adicionado com sucesso!')

            id_produto += 1
        case 3:
            print('You have chosen 3')
        case 4:
            print('You have chosen 4')
        case 5:
            estado_programa = False
