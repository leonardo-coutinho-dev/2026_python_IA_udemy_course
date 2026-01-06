from functions import *

preco = float(input('Qual o preço do produto (em R$)? '))
desconto = float(input('Qual o desconto a ser aplicado (1% a 100%)? '))

preco_final = calcular_desconto(float(preco), float(desconto))

print(f'O valor do produto com o desconto aplicado é R$ {preco_final:.2f}')

print(f'A soma de 199 + 298 é: {soma(199, 298)}')