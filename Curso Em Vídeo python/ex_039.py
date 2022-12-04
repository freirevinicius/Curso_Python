#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Qual o ano de nascimento? '))
idade = ano_atual - nascimento

print('Nascidos em {} tem {} anos em {}'.format(nascimento, idade, ano_atual))

if idade == 18:
    print('HORA DE SE ALISTAR')
elif idade < 18:
    verificar_anos = 18 - idade
    print('AINDA FALTAM {} ANOS PARA SE ALISTAR'.format(verificar_anos))
    ano = ano_atual + verificar_anos
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    verificar_anos = idade - 18
    print('JÁ PASSOU {} ANOS DA HORA DE SE ALISTAR'.format(verificar_anos))
    ano = ano_atual - verificar_anos
    print('Você se alistou em {}'.format(ano))