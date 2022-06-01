# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("INSIRA A PRIMEIRA NOTA: "))
nota2 = float(input("INSIRA A SEGUNDA NOTA: "))
nota3 = float(input("INSIRA A TERCEIRA NOTA: "))
nota4 = float(input("INSIRA A QUARTA NOTA: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("A MÉDIA DO ALUNO FOI:", round(media, 1))
