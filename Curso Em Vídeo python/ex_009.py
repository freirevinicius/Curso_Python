# faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
numero = int(input('Qual tabuada deseja fazer? '))

print('-' * 12)

for i in range (0, 11):
    tabuada = i * numero
    print('{} x {:2} = {}'.format(i, numero, tabuada))

print('-' * 12)