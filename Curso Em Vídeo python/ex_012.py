#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Preço do produto? R$'))
novo_preco = preco - (preco * 5 / 100)

print('Na promoção o produto que custava R${:.2f}, com desconto de 5% passará a custar R${:.2f}'.format(preco,novo_preco))