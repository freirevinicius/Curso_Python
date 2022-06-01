# Faça um Programa que peça um número e informe se o número
# é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input('INSIRA UM NÚMERO: '))

if numero % 1 == 0:
    print('O número {} é INTEIRO'.format(round(numero)))
else:
    print('O número {} é DECIMAL'.format(numero))
