# Faça um Programa que leia um número e exiba o dia correspondente da semana.
#  (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a 
# mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

dia = int(input("Qual dia? [1] [2] [3] [4] [5] [6] [7] "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-Feira")
elif dia == 3:
    print("Terça-Feira")
elif dia == 4:
    print("Quarta-Feira")
elif dia == 5:
    print("Quinta-Feira")
elif dia == 6:
    print("Sexta-Feira")
elif dia == 7:
    print("Sábado")
else:
    print("Valor Inválido.")
