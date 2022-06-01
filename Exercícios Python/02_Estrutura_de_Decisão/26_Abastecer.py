# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
#   até 20 litros, desconto de 3% por litro
#   acima de 20 litros, desconto de 5% por litro
# Gasolina:
#   até 20 litros, desconto de 4% por litro
#   acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do l
# itro do álcool é R$ 1,90.

print('Abastecendo')
tipo_combustivel = input('[A] - Alcool, [G] - Gasolina ')

preco_alc = 1.90
preco_gas = 2.50

if tipo_combustivel in ('aAgG'):
    if tipo_combustivel in ('Aa'):
        print('OPÇÃO SELECIONADA [ALCOOL]')
        litros = float(input('Quantos Litros?'))
        if litros <= 0:
            print('Quantidade inválida')
            while litros <= 0:
                litros = float(input('Quantos Litros?'))
        if litros <= 20.0:
            desconto = litros * 0.03
            preco_final = litros * preco_alc - desconto
        elif litros > 20.0:
            desconto = litros * 0.05
            preco_final = litros * preco_alc - desconto
    elif tipo_combustivel in ('gG'):
        print('OPÇÃO SELECIONADA [GASOLINA]')
        litros = float(input('Quantos Litros?'))
        if litros <= 20.0:
            desconto = litros * 0.04
            preco_final = litros * preco_gas - desconto
        elif litros > 20.0:
            desconto = litros * 0.06
            preco_final = litros * preco_gas - desconto

print(f'{litros} Litros, R$ {round(preco_final,2)}')
