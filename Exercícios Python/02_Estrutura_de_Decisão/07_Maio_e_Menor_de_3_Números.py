# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite primeiro número inteiro "))
num2 = int(input("Digite o segundo número inteiro "))
num3 = int(input("Digite o terceiro número inteiro "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("O MAIOR número é ", maior)
print("O MENOR número é ", menor)
