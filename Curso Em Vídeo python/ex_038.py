#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input('DIGITE O PRIMEIRO NÚMERO INTEIRO: '))
num2 = int(input('DIGITE O SEGUNDO NÚMERO INTEIRO: '))

if num1 > num2:
    print('O primeiro número digitado {}; é maior que o segundo {}.'.format(num1, num2))
elif num2 > num1:
    print('O segundo número digitado {}; é maior que o primeiro {}.'.format(num2, num1))
else:
    print('Os números {} e {} são iguais.'.format(num1, num2))