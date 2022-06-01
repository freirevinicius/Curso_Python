# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma Letra ")

if letra in ("aeiou") or letra in ("AEIOU"):
    print("A letra é uma VOGAL")
elif (letra.isnumeric()):
    print("É UM NÚMERO")
else:
    print("A letra é uma CONSOANTE")
