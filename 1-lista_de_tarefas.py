estado_programa = True

lista_tarefas = []

while estado_programa:
  print('\n ----------------------------->')

  print('\nLista de tarefas\n')

  print('1. Visualizar a lista.')
  print('2. Adicionar uma tarefa.')
  print('3. Remover uma tarefa.')
  print('4. Limpar a lista.')
  print('5. Encerrar o programa.')

  opcao = input('\nDigite um número(1-5): ')
  opcao = int(opcao)

  while opcao < 1 or opcao > 5:
    opcao = input('\nDigite um número(1-5): ')
    opcao = int(opcao)

  match opcao:
    case 1:
      if len(lista_tarefas) == 0:
        print('\nLista de tarefas vazia. Por favor, adicione uma tarefa!')
      else:
        print('\nTarefas do dia: \n')
        for tarefa in lista_tarefas:
          print(f'{lista_tarefas.index(tarefa) + 1}. {tarefa}')
    case 2:
      nova_tarefa = input('\nQual tarefa você deseja incluir? ')
      lista_tarefas.append(nova_tarefa)
      print('\nTarefa incluída.')
    case 3:
      remover_tarefa = input('\nQual tarefa você deseja remover? Digite o seu identificador: ')
      lista_tarefas.remove(lista_tarefas[int(remover_tarefa) - 1])
      print('\nTarefa removida.')
    case 4:
      lista_tarefas = []
      print('\nTodas as tarefas foram removidas.')
    case 5:
      estado_programa = False
      print('\nPrograma encerrado.')
    case _:
      print('Opção inexistente!')
