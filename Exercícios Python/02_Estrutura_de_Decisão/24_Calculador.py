# Faça um Programa que leia 2 números e em seguida pergunte ao usuário
# qual operação ele deseja realizar. O resultado da operação deve ser
# acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

import os


num1 = float(input('INSIRA O PRIMEIRO NÚMERO: '))
num2 = float(input('INSIRA O SEGUNDO NÚMERO: '))

operacao = int(input('Qual operação deseja fazer? [1] Soma [2] Subração [3] Multiplicação [4] Divisão. \n'))

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
elif operacao == 4:
    resultado = num1 / num2
else:
    while(operacao < 1 or operacao > 4):
        os.system('cls')
        operacao = int(input('Qual operação deseja fazer? [1] Soma [2] Subração [3] Multiplicação [4] Divisão. \n'))

print("Resultado: ",resultado)
if resultado % 2 == 0:
    print('PAR')
else:
    print('ÍMPAR')

if resultado > 0:
    print('POSITIVO')
else:
    print('NEGATIVO')

if resultado % 1 == 0:
    print('INTEIRO')
else:
    print('DECIMAL')