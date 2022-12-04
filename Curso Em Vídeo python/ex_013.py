#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário

salario = float(input('Qual o salário?'))
salario_novo = salario + (salario * 15 / 100)

print('O funcionário que recebia R${:2f}, com o aumento de 15% passará a receber R${:2f}'.format(salario, salario_novo))