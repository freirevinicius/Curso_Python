#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
total = 0
for contador in range (1, numero + 1):
    if numero % contador == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')

print('\n\033[mO número {} foi dividido {} vezes'.format(numero, total))

if total == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')
