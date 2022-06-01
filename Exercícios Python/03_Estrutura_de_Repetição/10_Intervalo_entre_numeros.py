# Faça um programa que receba dois números inteiros e gere os números inteiros
#  que estão no intervalo compreendido por eles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o último número: '))

numero = num1
 
if num1 < num2:
    for i in range (num1,(num2 + 1)):
        print(numero, end = ' ')
        numero +=1    
else:
    for i in range (num2,(num1 + 1)):
        print(numero, end = ' ')
        numero -= 1