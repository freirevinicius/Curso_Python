# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do
# saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota
# de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota
# de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

import os

print("************************CAIXA ELETRÔNICO***************************")
print("NOTAS DISPONÍVEIS: [R$1.00] [R$5.00] [R$10.00] [R$50.00] [R$100.00]")
print("*******************************************************************")
valor = int(
    input('*QUANTOS REAIS DESEJA SACAR? (mínimo R$10.00) (máximo R$ 600.00* \n'))

while(valor < 10 or valor > 600):
    os.system('cls')
    valor = int(
        input('VALOR INVÁLIDO! DIGITE UM VALOR ENTRE R$10.00 E 600.00 \n'))

notas_de_100 = int((valor - (valor % 100))/100)
notas_de_50 = int((valor % 100)/50)
notas_de_10 = int(((valor % 50)/10))
notas_de_1 = valor % 10

if(notas_de_100 == 1):
    print(f'{notas_de_100} Nota  de R$100.00')
elif(notas_de_100 > 1):
    print(f'{notas_de_100} Notas de R$100.00')

if(notas_de_50 == 1):
    print(f'{notas_de_50} Nota  de R$50.00')
elif(notas_de_50 > 1):
    print(f'{notas_de_50} Notas de R$50.00')

if(notas_de_10 == 1):
    print(f'{notas_de_10} Nota  de R$10.00')
elif(notas_de_10 > 1):
    print(f'{notas_de_10} Notas de R$10.00')

if (notas_de_1 == 1):
    print(f'{notas_de_1} Nota  de R$1.00')
elif (notas_de_1 > 1):
    print(f'{notas_de_1} Notas de R$1.00')
