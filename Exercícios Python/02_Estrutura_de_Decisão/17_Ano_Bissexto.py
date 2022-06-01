# Faça um Programa que peça um número correspondente a um determinado ano
#  e em seguida informe se este ano é ou não bissexto.

print("BISSEXTO OU NÃO")

ano = int(input("Digite o ano "))

if (ano % 4 ==0):
    print("Bissexto")
else:
    print('Não é bissexto')
