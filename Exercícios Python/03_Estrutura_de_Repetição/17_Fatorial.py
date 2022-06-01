# Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

#from math import factorial

#print('CALCULAR FATORIAL')
#numero = int(input("Fatorial de: ") )

#f = factorial(numero)
#print(f'O Fatorial de {numero} é {f}')

print('CALCULAR FATORIAL')
numero = int(input("Fatorial de: ") )
fatorial = 1
contador = numero
print(f'Calculando {numero}! = ', end = " ")
while contador > 0:
    print(contador, end = " ")
    print(' x ' if contador > 1 else ' = ', end = ' ')
    fatorial *= contador
    contador  -= 1

print(fatorial)