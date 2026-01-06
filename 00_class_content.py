# Testes

# print("Hello, world!\n");

# a = 100;
# b = 25;

# c = a + b;

# print("The sum of " + str(a) + " + " + str(b) + " is: " + str(c) + "\n");


### Aula 8 - Variáveis, tipos e entradas do usuário

# nome = "Leonardo Coutinho dos Santos"
# idade = 28
# altura = 1.80
# estudante = True

# print(type(nome))
# print(type(idade))
# print(type(altura))
# print(type(estudante))

# nome = input("Digite o seu nome completo: ")
# idade = int(input("Digite a sua idade: "))
# altura = float(input("Digite a sua altura: "))
#  fruta_favorita = input("Qual é a sua fruta favorita? ")

### Aula 9 - Melhorando o print com f-string

# print(f'Ola, {nome}. Você tem {idade} anos. Sua altura é de {altura} metros. Sua fruta favorita é {fruta_favorita}.')

#  print(f'Daqui a 5 anos, você terá {idade + 5} anos de idade!')

### Aula 10 - Operadores aritméticos e desafios do dia a dia

#  print(type(nome))
# print(type(idade))
#  print(type(altura))
# print(type(fruta_favorita))

# num_1 = 10
# num_2 = 2

# print(f'Números: {num_1} & {num_2}\n')

# print(f'Soma: {num_1 + num_2}')
# print(f'Subtração: {num_1 - num_2}')
# print(f'Multiplicação: {num_1 * num_2}')
# print(f'Divisão: {num_1 / num_2}')
# print(f'Divisão (inteiro): {num_1 // num_2}')
# print(f'Resto da divisão: {num_1 % num_2}')
# print(f'Potenciação: {num_1 ** num_2}')

# preco_produto = 100.0
# desconto = 20/100

# valor_final = preco_produto - (preco_produto * desconto)

# print(f'\nO valor do produto é R${preco_produto}. Com o desconto aplicado de {desconto * 100}%, o valor é: R${valor_final}')

## Exercício - pedir o preço do produto e o desconto para o usuário:

# valor_produto = float(input('Por favor, digite o valor do produto em R$: '))
# valor_desconto = float(input('\nPor favor, digite o valor do desconto em % (0 a 100): '))

# valor_final = valor_produto - (valor_produto * (valor_desconto / 100))

# print(f'\nO valor do produto com o desconto aplicado é: R$ {valor_final:.2f}')

## Mini-desafio: calcular quantos dias um produto duraria se a pessoa usar X porções por dia.

# quantidade_produto = int(input('Por favor, especifique a quantidade do produto: '))
# porcao_diaria = int(input('\nPor favor, especifique a quantidade do produto a ser utilizada diariamente: '))

# duracao_dias = quantidade_produto / porcao_diaria

# print(f'\nO produto irá durar: {duracao_dias:.0f} dias.')

### 11. Criando programas com operadores lógicos e relacionais

## I. Operadores relacionais:

# num_1 = 10
# num_2 = 20

# print(num_1 == num_2)
# print(num_1 != num_2)

# print('\n')

# print(num_1 > num_2)
# print(num_1 < num_2)

# print('\n')

# print(num_1 >= num_2)
# print(num_1 <= num_2)

# idade_usuario = int(input('Por favor, digite a sua idade: '))

# if (idade_usuario >= 18):
#   print('Você é um adulto!')
# else:
#   print('Você não é um adulto!')

## II. Operadores lógicos: (AND, OR & NOT)

## Para dirigir, a pessoa tem que ter 18 anos de idade ou mais e possuir a Carteira Nacional de Habilitação (CNH)!

# idade_usuario = int(input('Por favor, digite a sua idade: '))
# carteira_motorista = input('Você tem permissão para conduzir? ')

# if(carteira_motorista == 'sim'):
#   carteira_motorista = True
# else:
#   carteira_motorista = False

# if(idade_usuario >= 18 and carteira_motorista == True):
#   print('Você pode dirigir, parabéns!')
# else:
#   print('Você não pode dirigir!')

# nome_usuario = input('Qual o nome de usuário? ')
# senha_usuario = input('Qual a senha do usuário? ')

# verificador = nome_usuario == 'user_admin' and senha_usuario == 'admin123'

# if(nome_usuario != 'user_admin'):
#   if(senha_usuario != 'admin123'):
#     print('Nome de usuário e senha estão incorretos!')
#   else:
#     print('Nome de usuário incorreto!')
# elif (senha_usuario != 'admin123'):
#   print('Senha incorreta!')
# else:
#   print('Acesso permitido!')

### 12. Condições (if, elif, else) com exemplos da vida real

# nota_aluno = float(input('Qual é a sua nota final? '))

# if(nota_aluno >= 7):
#   print('Você foi aprovado!')
# elif(nota_aluno >= 5 and nota_aluno < 7):
#   print('Você está de recuperacão!')
# else:
#   print('Você foi reprovado!')

# idade_cliente = int(input('Qual é a sua idade? '))

# if(idade_cliente >= 18):
#   print('Acesso liberado!')
# elif(idade_cliente >= 16 and idade_cliente < 18):
#   autorizacao_pais = input('Você tem autorização dos pais? (s/n): ')
#   if(autorizacao_pais == 's'):
#     print('Acesso liberado!')
#   else:
#     print('Acesso negado, você não tem autorização dos pais!')
# else:
#   print('Acesso negado, você não tem idade suficiente!')

### 13. Repetições com for e while

# for i in range(10):
#   print(i)

# for i in range(1, 11):
#   print(i * 0.5)

# for i in range(10, 0, -2):
#   print(i)

# for i in range(9, 0, -2):
#   print(i)

# k = 1

# while k <= 5:
#   print(k)
#   k += 1

# nome_usuario = input('Qual é o nome do usuário? ')
# senha_usuario = input('Qual é a senha? ')

# verificador = nome_usuario == 'user_admin' and senha_usuario == 'admin123'

# while(verificador == False):
#   print('\nPor favor, tente novamente!\n')
#   nome_usuario = input('Qual é o nome do usuário? ')
#   senha_usuario = input('Qual é a senha? ')
#   verificador = nome_usuario == 'user_admin' and senha_usuario == 'admin123'

# print('\nAcesso garantido! Fim do programa.')

### 14. Listas, dicionários e tuplas no mundo real

## I. Listas - Mutáveis

# frutas = ['Banana', 'Abacate', 'Morango']

# print(frutas)
# print(len(frutas))

# frutas.append('Uva')

# print(frutas)
# print(len(frutas))

# frutas.remove('Banana')

# print(frutas)
# print(len(frutas))

# print(frutas[0])

# tarefas = ['Estudar python com IA', 'Ler um artigo sobre IA', 'Responder e-mails']

# tarefas.append('Fazer musculação na academia')

# for i in range(len(tarefas)):
#   print(f'{i + 1}. {tarefas[i]}')

# for tarefa in tarefas:
#   print(f'{tarefas.index(tarefa) + 1}. {tarefa}')

## II. Tuplas - Imutáveis

# meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# for mes in meses:
#   print(f'{meses.index(mes) + 1}. {mes}')

## III. Dicionários

# produto = {
#     'id': '1',
#     'titulo': 'Hydraulic Cylinder',
#     'description': 'This is a hydraulic cylinder',
#     'weight': '20kg',
#     'size': '10x10x10',
#     'value': 120.00
# }

# print(produto['id'])

# aluno = {
#     'nome': input('Qual é o nome do aluno? '),
#     'idade': input('Qual é a idade do aluno? '),
#     'nota': input('Qual é a nota final do aluno? ')
# }

# print(f"\n{aluno['nome']} tem {aluno['idade']} anos. A sua nota final é {aluno['nota']}.")

# frutas_em_estoque = ['Banana', 'Uva', 'Limão']
# frutas_em_falta = ['Kiwi', 'Abacate', 'Abacaxi']

# frutas_totais = []

# print(f'As frutas em estoque são: {frutas_em_estoque}\n')

# print(f'As frutas em falta são: {frutas_em_falta}\n')

# frutas_em_estoque.insert(0, 'Mamão')

# frutas_em_estoque.remove('Banana')

# fruta_removida = frutas_em_estoque.pop()

# frutas_totais.extend(frutas_em_estoque)
# frutas_totais.extend(frutas_em_falta)

# frutas_totais.sort()

# print(f'Estas são todas as frutas comercializadas (em ordem alfabética): {frutas_totais}\n')

# frutas_totais.reverse()

# print(f'Estas são todas as frutas comercializadas (em ordem inversa): {frutas_totais}\n')

# print(f'Essa é a fruta que foi removida (pop): {fruta_removida}')

### 15. Criando funções reutilizáveis no Replit

# def soma(a, b):
#   return a + b

# soma_1 = soma(8, 12)
# soma_2 = soma(10, 12)
# soma_3 = soma(12, 12)

# print(soma_1)
# print(soma_2)
# print(soma_3)

# def calcular_desconto():
#   preco = float(input('Qual o preço do produto (em R$)? '))
#   desconto = float(input('Qual o desconto a ser aplicado (1% a 100%)? '))

#   return preco - preco * desconto / 100

# valor_final = calcular_desconto()

# print(f'O valor do produto com o desconto aplicado é R$ {valor_final:.2f}')

### 18. O que é Programação Orientada a Objetos?

# class Casa:
#   def __init__(self, cor, quartos, banheiros):
#     self.cor = cor
#     self.quartos = quartos
#     self.banheiros = banheiros

#   def mostrar_cor(self):
#     print(f'A cor da casa é {self.cor}')

#   def mostrar_quartos(self):
#     print(f'A casa tem {self.quartos} quartos')

#   def mostrar_banheiros(self):
#     print(f'A casa tem {self.banheiros} banheiros')

#   def adicionar_quarto(self):
#     self.quartos += 1

#   def pintar_casa(self, nova_cor):
#     self.cor = nova_cor

# casa_1 = Casa('verde', 4, 2)

# print('Casa 1: ')

# casa_1.mostrar_cor()
# casa_1.mostrar_quartos()
# casa_1.mostrar_banheiros()

# casa_2 = Casa('azul', 8, 4)

# print('\nCasa 2: ')

# casa_2.mostrar_cor()
# casa_2.mostrar_quartos()
# casa_2.mostrar_banheiros()

# casa_2.adicionar_quarto()
# casa_2.pintar_casa('roxo')

# print('\nCasa 2: ')

# casa_2.mostrar_cor()
# casa_2.mostrar_quartos()
# casa_2.mostrar_banheiros()

# Criar um programa de cadastro de casas de uma imobiliária: pedir as informações via input e criar uma nova casa.

### 19. Criando uma classe de Carros no Colab

# class Carro:
#   def __init__(self, modelo, marca, cor, ano):
#     self.modelo = modelo
#     self.marca = marca
#     self.cor = cor
#     self.ano = ano
#     self.ligado = False
#     self.seta = None

#   def mostrar_modelo(self):
#     print(f'O modelo do carro é {self.modelo}')

#   def mostrar_marca(self):
#     print(f'A marca do carro é {self.marca}')

#   def mostrar_cor(self):
#     print(f'A cor é {self.cor}')

#   def mostrar_ano(self):
#     print(f'O ano é {self.ano}')

#   def ligar_carro(self):
#     if not self.ligado:
#       self.ligado = True
#       print('O carro foi ligado!')
#     else:
#       print('O carro já está ligado!')

#   def desligar_carro(self):
#     if self.ligado:
#       self.ligado = False
#       print('O carro foi desligado!')
#     else:
#       print('O carro já está desligado!')

#   def ligar_seta(self, direcao):
#     self.seta = direcao
#     print(f'A seta foi ligada para a {self.seta}')

# carro_1 = Carro('golf', 'volkswagen', 'preto', 2004)

# carro_1.mostrar_modelo()
# carro_1.mostrar_marca()
# carro_1.mostrar_cor()
# carro_1.mostrar_ano()

# carro_1.ligar_carro()

# carro_1.ligar_seta('esquerda')

### 20. Criando uma classe de Pessoas no Colab

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Gênero: {self.genero}')

    def atualizar_idade(self):
        self.idade += 1


class Funcionario(Pessoa):
    def __init__(self, nome, idade, genero, cargo, setor, ciclo):
        super().__init__(nome, idade, genero)
        self.cargo = cargo
        self.setor = setor
        self.ciclo = ciclo

    def info(self):
        print('--- \n')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Genero: {self.genero}')
        print('\n--- \n')
        print(f'Cargo: {self.cargo}')
        print(f'Setor: {self.setor}')
        if self.ciclo < 1:
            print(f'Tem menos de 1 ano de empresa!')
        else:
            print(f'Tem {self.ciclo} anos de empresa!')


pessoa_1 = Pessoa('Leonardo', 28, 'Masculino')
pessoa_2 = Pessoa('Maria', 55, 'Feminino')

colaborador_2 = Funcionario('Gandalf', 37, 'Masculino', 'Programador', 'Informática', 0)

print('* Pessoa 1: \n')
pessoa_1.informacoes()

print('\n* Pessoa 2: \n')
pessoa_2.informacoes()

print('\n* Colaborador 1 (extends Pessoa): \n')

colaborador_2.info()


## ANIMALS CLASS

class Animal:
    pass

class Dog:
    sound = 'ROUF'

    def __init__(self, name):
        self.name = name


class Cat:
    sound = 'MIAU'

    def __init__(self, name):
        self.name = name



