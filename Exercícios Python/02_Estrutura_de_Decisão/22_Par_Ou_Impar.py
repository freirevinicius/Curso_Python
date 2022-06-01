# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
#  Dica: utilize o operador módulo (resto da divisão).

numero = int(input('INSIRA UM NÚMERO: '))

if numero % 2 == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
