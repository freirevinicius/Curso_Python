# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo


val_hora = float(input("Qual valor da hora? "))
horas_trabalhadas = float(input("Quantas horas trabalhadas? "))

salario_bruto = val_hora * horas_trabalhadas
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print("+ Salário bruto:   R$", round(salario_bruto, 2))
print("- IR (11%):        R$", round(ir, 2))
print("- INSS (8%):       R$", round(inss, 2))
print("- Sindicato (5%):  R$", round(sindicato, 2))
print("= Salário Líquido: R$", round(salario_liquido, 2))
