# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

pão = float(input("Qual o valor do Pão? "))
bolacha = float(input("Qual o valor da Bolacha? "))
salgadinho = float(input("Qual o valor do Salgadinho? "))

barato = pão

if bolacha < barato:
    barato = bolacha
    print("Você deve comprar BOLACHA")
elif salgadinho < barato:
    barato = salgadinho
    print("Você deve comprar SALGADINHO")
else:
    print("Você deve comprar PÃO")
