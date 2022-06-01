# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range(1, 6):
    numero = float(input(f'Digite o {i}o número: '))
    soma += numero

media = soma / 5

print(media)
