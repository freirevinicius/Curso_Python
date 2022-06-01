# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# A. "Telefonou para a vítima?"
# B. "Esteve no local do crime?"
# C. "Mora perto da vítima?"
# D. "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

pontos = 0

print('INTERROGATÓRIO.')
telefonou = input("Telefonou para a vítima? [S]/[N] ")
if telefonou in ('Ss'):
    pontos = + 1
else:
    pontos = + 0

esteve_local = input("Esteve no local do crime? [S]/[N] ")
if esteve_local in ('Ss'):
    pontos = pontos + 1
else:
    pontos = + 0

mora_perto = input('Mora perto da vítima? [S]/[N] ')
if mora_perto in ('Ss'):
    pontos = pontos + 1
else:
    pontos = + 0

devia = input('Devia para a vítima? [S]/[N] ')
if devia in ('Ss'):
    pontos = pontos + 1
else:
    pontos = + 0

trabalhou = input('Já trabalhou com a vítima? [S]/[N] ')
if trabalhou in ('Ss'):
    pontos = pontos + 1
else:
    pontos = + 0


if pontos <= 1:
    print('{} Ponto; INOCENTE'.format(pontos))
if pontos == 2:
    print('{} Pontos; SUSPEITO.'.format(pontos))
if pontos > 2 and pontos <= 4:
    print("{} Pontos; CÚMPLICE.". format(pontos))
if pontos == 5:
    print('{} Pontos; ASSASSINO.'.format(pontos))
