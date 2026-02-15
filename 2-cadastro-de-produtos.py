from dataclasses import dataclass

estado_programa = True

estado_programa_atualizar = False

lista_de_produtos = []

total_de_produtos = 0

valor_total_pr = 0

lucro_total_pr = 0

id_produto = 1

@dataclass
class Product:
    id: int
    _title: str
    _description: str
    _price: float
    _profit: float
    _quantity: int

    def __init__(self, id_prod: int, title: str, description: str, price: float, profit: float, quantity: int):
        self.id = id_prod
        self._title = title
        self._description = description
        self._price = price
        self._profit = profit
        self._quantity = quantity


    # CUSTOM METHODS
    @property
    def valor_total(self) -> float:
        return self._quantity * self._price

    # GETTERS ----->
    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def price(self) -> float:
        return self._price

    @property
    def profit(self) -> float:
        return self._profit

    @property
    def quantity(self) -> int:
        return self._quantity

    # SETTERS ----->
    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @profit.setter
    def profit(self, value: float) -> None:
        if value < 0:
            raise ValueError("Profit cannot be negative")
        self._profit = value

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

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
    print('8. Valor total (R$) em estoque.')
    print('9. Lucro (R$) total esperado.')
    print('10. Encerrar o programa.')

    opcao = input('\nDigite um número (1-10): ')

    opcao = int(opcao)

    while opcao < 1 or opcao > 10:
        opcao = input('\nPor favor, digite um número de 1 a 10: ')
        opcao = int(opcao)

    match opcao:
        # CREATE
        case 1:
            produto_nome = input('\nDigite o nome do produto: ')
            produto_descricao = input('Digite a descrição do produto: ')
            produto_preco = float(input('Digite o valor (R$) do produto: '))
            produto_lucro = float(input('Digite o lucro (R$) do produto: '))
            produto_quantidade = int(input('Qual a quantidade do produto em estoque? '))

            new_product = Product(id_produto, produto_nome, produto_descricao, produto_preco, produto_lucro, produto_quantidade)

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

                        estado_programa_atualizar = True

                        while estado_programa_atualizar:

                            print('\n1. Título')
                            print('2. Descrição')
                            print('3. Preço')
                            print('4. Lucro')
                            print('5. Estoque')
                            print('6. Atualizar outro produto')
                            print('7. Finalizar\n')

                            opcao = int(input('Qual informação será atualizada?\n'))
                            # IMPLEMENTAR
                            match opcao:
                                case 1:
                                    produto_nome = input('\nDigite o nome do produto: ')
                                    produto.name = produto_nome
                                    print('Nome atualizado com sucesso!')
                                case 2:
                                    produto_descricao = input('Digite a descrição do produto: ')
                                    produto.description = produto_descricao
                                    print('Descrição atualizada com sucesso!')
                                case 3:
                                    produto_preco = float(input('Digite o valor (R$) do produto: '))
                                    produto.price = produto_preco
                                    print('Preço atualizado com sucesso!')
                                case 4:
                                    produto_lucro = float(input('Digite o lucro (R$) do produto: '))
                                    produto.profit = produto_lucro
                                    print('Lucro atualizado com sucesso!')
                                case 5:
                                    produto_quantidade = int(input('Qual a quantidade do produto em estoque? '))
                                    produto.quantity = produto_quantidade
                                    print('Quantidade atualizada com sucesso!')
                                case 6:
                                    print('Atualizar outro produto!')
                                case 7:
                                    estado_programa_atualizar = False
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
                total_de_produtos = 0
        # ENCERRAR O PROGRAMA
        case 8:
            for produto in lista_de_produtos:
                valor_total_pr += produto.valor_total
            print(f'O valor total (em R$) dos produtos em estoque é: R$ {valor_total_pr}')
            valor_total_pr = 0
        case 9:
            for produto in lista_de_produtos:
                lucro_total_pr += produto.profit * produto.quantity
            print(f'O lucro total (em R$) dos produtos em estoque é: R$ {lucro_total_pr}')
            lucro_total_pr = 0
        case 10:
            print('Programa finalizado.')
            estado_programa = False
            estado_programa_atualizar = False
        # DEFAULT
        case _:
            print('Opção inexistente!')
