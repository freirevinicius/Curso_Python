# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.

val_hora = float(input("Qual o valor da hora? "))
hora = float(input("Quantas horas trabalhadas? "))

sal = val_hora * hora

print("Sua hora é R${} e você trabalhou {}h, portanto seu salário é R${}" .format(
    val_hora, hora, round(sal, 2)))
