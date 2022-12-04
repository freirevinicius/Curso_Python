# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('VALOR DA CASA R$'))
salario = float(input('SALÁRIO R$'))
anos = int(input('EM QUANTOS ANOS VAI PAGAR?'))
parcelas = valor_casa / (anos * 12)
valor_minimo = salario * 0.30

print('Para pagar uma casa de R${:.2f} em {} anos, a parcela será de R${:.2f}'.format(valor_casa, anos, parcelas))

if parcelas <= valor_minimo:
    print('Empréstimo APROVADO.')
else:
    print('Empréstimo NÃO APROVADO.')