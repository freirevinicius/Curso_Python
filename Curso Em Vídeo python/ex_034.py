#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salário do funcionário? R$'))

if salario > 1250:
    aumento = salario * 0.10
    salario_novo = salario + aumento
else:
    aumento = salario * 0.15
    salario_novo = salario + aumento

print('O salário antigo era {:.2f}, o novo salário será {:.2f}'.format(salario,salario_novo))
