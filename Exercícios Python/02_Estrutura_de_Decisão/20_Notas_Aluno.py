# Faça um Programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Digite a NOTA 1: "))
nota2 = float(input("Digite a NOTA 2: "))
nota3 = float(input("Digite a NOTA 3: "))

media = (nota1 + nota2 + nota3) / 3


if media == 10:
    print("Média: {} Aprovado com Distinção".format(round(media, 2)))
elif media >= 7 and media < 10:
    print("Média: {} Aprovado".format(round(media, 2)))
elif media < 0 or media > 10:
    print("Lançamento de nota incorreto. Encerrando!")
    exit()
else:
    print("Média: {} Reprovado".format(round(media, 2)))
