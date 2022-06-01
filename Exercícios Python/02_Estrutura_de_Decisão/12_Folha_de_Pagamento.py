# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são
# do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
#  Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o
# exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

val_hora = float(input("Qual valor da hora? "))
horas_trabalhadas = float(input("Quantas horas trabalhadas? "))

salario_bruto = val_hora * horas_trabalhadas
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

if salario_bruto <= 900:
    ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto > 1500 and salario_bruto >= 2500:
    ir = salario_bruto * 0.10
elif salario_bruto > 2500:
    ir = salario_bruto * 0.20

descontos = ir + inss
salario_liquido = salario_bruto - descontos


print(f"+ Salário bruto:    R$", round(salario_bruto, 2))
print("(-) IR:              R$", round(ir, 2))
print("(-) INSS:            R$", round(inss, 2))
print("FGTS (11%):          R$", round(fgts, 2))
print("Total de Descontos:  R$", round(descontos, 2))
print("= Salário Líquido:   R$", round(salario_liquido, 2))
