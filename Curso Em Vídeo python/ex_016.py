#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc

numero = float(input('Digite um número real'))
print('O número {} tem a parte inteira {}'.format(numero, trunc(numero)))