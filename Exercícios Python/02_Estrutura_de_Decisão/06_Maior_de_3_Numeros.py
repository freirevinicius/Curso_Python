# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input("Digite primeiro número inteiro "))
num2 = int(input("Digite o segundo número inteiro "))
num3 = int(input("Digite o terceiro número inteiro "))

if num1 > num2 and num1 > num3:
    print("O maior número digitado foi ", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número digitado foi ", num2)
else:
    print("O maior número digitado foi ", num3)
