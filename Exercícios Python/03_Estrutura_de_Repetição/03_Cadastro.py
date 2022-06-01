# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

from ast import And


print('CADASTRAR')

nome = input('INSIRA O NOME [Mais de 3 caracteres]: ')
while len(nome) <= 3: #contador de caracteres
    nome = input('INSIRA O NOME [Mais de 3 caracteres]: ')

idade =  int(input('INSIRA A IDADE: [Entre 0 e 150]: '))
while idade < 0 or idade > 150:
    idade =  int(input('INSIRA A IDADE: [Entre 0 e 150]: '))

salario = float(input('INSIRA O SALÁRIO: [Maior que 0]: '))
while salario <= 0:
    salario = float(input('INSIRA O SALÁRIO: [Maior que 0]: '))

sexo = input('SEXO [F] ou [M]: ')
while sexo != ('f') and sexo != ('F') and sexo != ('m') and sexo != ('M'):
    sexo = input('SEXO [F] ou [M]: ')

estado_civil = input('ESTADO CIVIL [S]Solteiro(a) [C]Casado(a) [V]Viúvo(a) [D]Divorciado(a): ')
while estado_civil != ('S') and estado_civil != ('s') and estado_civil != ('C') and estado_civil != ('c') and estado_civil != ('v') and estado_civil != ('V') and estado_civil != ('d') and estado_civil != ('D'):
    estado_civil = input('ESTADO CIVIL [S]Solteiro(a) [C]Casado(a) [V]Viúvo(a) [D]Divorciado(a): ')

if sexo in('mM'):
    sexo_str = 'Masculino'
else:
    sexo_str = 'Feminino'

if estado_civil in ('sS'):
    estado_civil_str = 'Solteiro(a)'
elif estado_civil in ('cC'):
    estado_civil_str = 'Casado(a)'
elif estado_civil in ('vV'):
    estado_civil_str = 'Viúvo(a)'
else:
    estado_civil_str = 'Divorciado(a)'

print(f'Cadastro efetuado com sucesso Nome: {nome}; Idade: {idade} anos; Salário: R${salario}; Sexo: {sexo_str}; Estado Civil: {estado_civil_str}')