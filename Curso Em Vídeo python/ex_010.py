#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

reais = float(input('Quantos reais tem na carteira? R$'))
dolar = reais / 3.27

print ('Você pode comprar US${:.2f} com R${:.2f}'.format(dolar,reais))