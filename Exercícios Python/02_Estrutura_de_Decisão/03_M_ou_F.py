# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("[M] ou [F] ")

if sexo == ("m") or sexo == ("M"):
    print("MASCULINO")
elif sexo == ("f") or sexo == ("F"):
    print("FEMININO")
else:
    print("SEXO INVÁLIDO")
