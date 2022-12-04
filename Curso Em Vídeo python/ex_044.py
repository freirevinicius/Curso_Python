#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Valor das compras: R$'))
pagamento = int(input('''FORMAS DE PAGAMENTO
[1] - À VISTA DINHEIRO/CHEQUE
[2] - À VISTA CARTÃO
[3] - 2x NO CARTÃO
[4] - 3x OU MAIS NO CARTÃO
Selecione uma opção...'''))   

if pagamento == 1:
    preco_final = preco - (preco * 0.10)
    print('À VISTA DINHEIRO/CHEQUE; Desconto = 10%')
    print('Valor da compra R${:.2f}'.format(preco))
    print('Valor com desconto R${:.2f}'.format(preco_final))
elif pagamento == 2:
    preco_final = preco - (preco * 0.05)
    print('À VISTA CARTÃO; Desconto = 5%')
    print('Valor da compra R${:.2f}'.format(preco))
    print('Valor com desconto R${:.2f}'.format(preco_final))
elif pagamento == 3:
    print('2x NO CARTÃO; Sem desconto e sem acrescimo;')
    print('Valor da compra R${:.2f}'.format(preco))
elif pagamento == 4:
    preco_final = preco + (preco * 0.20)
    print('3x OU MAIS NO CARTÃO; Acrescimo = 20%')
    print('Valor da compra R${:.2f}'.format(preco))
    print('Valor com desconto R${:.2f}'.format(preco_final))
else:
    print('OPÇÃO INVÁLIDA; ENCERRANDO...')