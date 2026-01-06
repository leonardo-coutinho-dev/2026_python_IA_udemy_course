estado_programa = True

produto = {}
lista_de_produtos = []

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
            print('You have chosen 1')
        case 2:
            print('You have chosen 2')
        case 3:
            print('You have chosen 3')
        case 4:
            print('You have chosen 4')
        case 5:
            estado_programa = False