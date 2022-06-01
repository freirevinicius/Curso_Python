# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é POSITIVO")
elif numero == 0:
    print("O número é NULO")
else:
    print("O número é NEGATIVO")
