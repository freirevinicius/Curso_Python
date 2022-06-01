# Faça um programa que lê as duas notas parciais obtidas por um aluno numa
#  disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

n1 = float(input("Insira a Nota 1 "))
n2 = float(input("Insira a Nota 2 "))

media = (n1 + n2) / 2

if media > 4.0:
    apr = "APROVADO"
elif media <= 4.0:
    apr = "REPROVADO"

if media >= 9.0 and media <= 10:
    print("Nota {} Conceito [A] {}".format(round(media, 2), apr))
elif media >= 7.5 and media < 9.0:
    print("Nota {} Conceito [B] {}".format(round(media, 2), apr))
elif media >= 6.0 and media < 7.5:
    print("Nota {} Conceito [C] {}".format(round(media, 2), apr))
elif media >= 4.0 and media < 6.0:
    print("Nota {} Conceito [D] {}".format(round(media, 2), apr))
elif media >= 0.0 and media < 4.0:
    print("Nota {} Conceito [E] {}".format(round(media, 2), apr))
