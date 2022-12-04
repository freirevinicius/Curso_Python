#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado

dias = int(input('Quantos dias alugado?'))
km = int(input('Quantos Km rodados?'))
total_a_pagar = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(total_a_pagar))