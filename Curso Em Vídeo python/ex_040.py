# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('-=' *10)
nota_1 = float(input('DIGITE A NOTA 1: '))
nota_2 = float(input('DIGITE A NOTA 2: '))
nota_3 = float(input('DIGITE A NOTA 3: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media < 5:
    print('Média {:.1f}. REPROVADO'.format(media))
elif media >= 5 and media < 7:
    print('Média {:.1f}. EM RECUPERAÇÃO.'.format(media))
else:
    print('Média {:.2f}. APROVADO'.format(media))