# Faça um programa que, dado um conjunto de N números, determine o
# menor valor, o maior valor e a soma dos valores.

quantidade = int(input('Quantos Números? '))

i = 1
maior = 0
menor = 0
soma = 0

while i <= quantidade:
    numero = int(input('Digite o número: '))
    
    if i == 1:
        menor = numero
    if numero>= maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    i += 1

print('O maior numero é: ', maior)
print('O menor número é: ', menor)
print('A soma é: ', soma)