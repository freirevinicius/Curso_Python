#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date

ano_atual = date.today().year
nascimento = int(input('Ano de Nascimento '))
idade = ano_atual - nascimento

if idade <= 9:
    print('{} anos. MIRIM'.format(idade))
elif idade <= 14:
    print('{} anos. INFANTIL'.format(idade))
elif idade <= 19:
    print('{} anos. JUVENIL'.format(idade))
elif idade <= 25 :
    print('{} anos. SÊNIOR'.format(idade))
else:
    print('{} anos. MASTER'.format(idade))