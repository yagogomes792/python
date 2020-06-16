from lib.interface import cabeçalho, menu, leiaInt
from lib.arquivo import *

arq = 'Cadastro-de-pessoas.txt'

if not fileExists(arq):
    createFile(arq)

cabeçalho('Menu principal')

while True:
    res = menu(['Cadastrar uma pessoa','Listar pessoas cadastradas','Sair do programa'])
    if res == 1:
        cabeçalho('Cadastre uma nova pessoa')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        register(arq, nome, idade)
    elif res == 2:
        readFile(arq)
    elif res == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        cabeçalho('ERRO! Insira um valor válido')
