# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

num1 = int(input("Insira o Primeiro número (Inteiro)"))
num2 = int(input("Insira o Segundo número (Inteiro)"))
num3 = float(input("Insira o Terceiro número (Real)"))

a = float(num1 * 2) * (num2 / 2)
b = float(num1 * 3) + num3
c = num3 ** 3

print("O produto do dobro de {} com metade de {} é {}" .format(
    num1, num2, round(a, 2)))
print("A soma do triplo de {} com {} é {}" .format(num1, num3, round(b, 2)))
print("{} elevado ao cubo é {}" .format(num3, round(c, 2)))
