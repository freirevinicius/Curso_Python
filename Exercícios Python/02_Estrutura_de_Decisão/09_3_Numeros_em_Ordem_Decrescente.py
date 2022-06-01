# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input("Digite o primeiro número"))
b = int(input("Digite o segundo número"))
c = int(input("Digite o terceiro número"))

# (a,b,c)
# (a,c,b)
# (b,a,c)
# (b,c,a)
# (c,a,b)
# (c,b,a)

if a > b and a > c and c < a and c < b:
    print(a, b, c)
elif a > b and a > c and b < a and b < c:
    print(a, c, b)
elif b > a and b > c and c < a and c < b:
    print(b, a, c)
elif b > a and b > c and b < a and b < c:
    print(b, c, a)
elif c > a and c > b and a < b and a < c:
    print(c, b, a)
elif c > a and c > b and b < a and b < c:
    print(c, a, b)
