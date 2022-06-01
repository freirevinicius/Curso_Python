# Faça um programa que peça uma nota, entre zero e dez.
#  Mostre uma mensagem caso o valor seja inválido e continue pedindo até
# que o usuário informe um valor válido.

numero = int(input('DIGITE UM NÚMERO ENTRE 0 E 10 '))

while numero <= 0 or numero > 10:
    numero = int(input('DIGITE UM NÚMERO ENTRE 0 E 10 '))

print(f'O número {numero}, está correto.')
