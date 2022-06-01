# Faça um programa que leia um nome de usuário e a sua senha e não aceite
#  a senha igual ao nome do usuário, mostrando uma mensagem de erro
#  e voltando a pedir as informações.

import getpass  # FUNÇÃO P/ ESCONDER A SENHA

print('CADASTRAR.')
usuario = input('Usuário: ')
senha = getpass.getpass('Senha: ')  # não mostra nada digitado

while usuario == senha:
    print('A SENHA NÃO PODE SER IGUAL AO USUÁRIO')
    senha = getpass.getpass('Senha:')
else:
    print('CADASTRO EFETUADO COM SUCESSO')
