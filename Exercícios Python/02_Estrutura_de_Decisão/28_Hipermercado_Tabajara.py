# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
# de carne da promoção, porém não há limites para a quantidade de carne por cliente.
#  Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
# sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
# comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print('HIPERMERCADO TABAJARA')
print('PROMOÇÃO DE CARNES')
print('CARNES DISPONÍVEIS:')
print('[1] [Filé Duplo]')
print('[2] [Alcatra]')
print('[3] [Picanha]')

tipo_carne = int(input('Qual o tipo de carne escolhido? [1] [2] [3]\n'))
quantidade_carne = float(input('Qual a quantidade? [Kg]\n'))
pagamento = int(input('Qual a forma de pagamento [1] Cartão, [2] Outra\n'))

preco_file_menor = 4.90
preco_file_maior = 5.80

preco_alcatra_menor = 5.90
preco_alcatra_maior = 6.80

preco_picanha_menor = 6.90
preco_picanha_maior = 7.80

if tipo_carne == 1:
    tipo_carne_str = 'Filé Duplo'
    if quantidade_carne < 5:
        preco_total = quantidade_carne * preco_file_menor
    else:
        preco_total = quantidade_carne * preco_file_maior
elif tipo_carne == 2:
    tipo_carne_str = 'Alcatra'
    if quantidade_carne < 5:
        preco_total = quantidade_carne * preco_alcatra_menor
    else:
        preco_total = quantidade_carne * preco_alcatra_maior
elif tipo_carne == 3:
    tipo_carne_str = 'Picanha'
    if quantidade_carne < 5:
        preco_total = quantidade_carne * preco_picanha_menor
    else:
        preco_total = quantidade_carne * preco_picanha_maior
else:
    print('TIPO DE CARNE INVÁLIDO. ENCERRANDO!')

desconto = preco_total * 0.05
valor_final = preco_total - desconto

if pagamento == 1:
    pagamento_str = 'Cartão Tabajara.'
else:
    pagamento_str = 'Outros'

print('       CUPOM FISCAL:')
print('Produto:', tipo_carne_str)
print(f'Quantidade: {quantidade_carne} Kg')
print('Forma de Pagamento: ', pagamento_str)
print('Valor Real: R$ {:.2f}'.format(preco_total))
print('Valor do desconto R$', round(desconto, 2))
print('VALOR FINAL: R$', round(valor_final, 2))
