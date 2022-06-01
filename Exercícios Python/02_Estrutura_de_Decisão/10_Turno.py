# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino
# ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

turno = input("Qual o turno? [M]-Matutino, [V]-Vespertino, [N]-Noturno ")

if turno in ("mM"):
    print("Bom Dia!")
elif turno in ("vV"):
    print("Boa Tarde!")
elif turno in ("nN"):
    print("Boa Noite!")
else:
    print("Valor Inválido, Encerrando!")
