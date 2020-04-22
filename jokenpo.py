from random import randint
from time import sleep

itens = ('Pedra','Papel', 'Tesoura')
computador = randint(0,2)

print('''Escolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual a sua Jogada? '))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: #Pedra
    if jogador == 0:
        print('Os dois jogaram {} o jogo EMPATOU!'.format(itens[0]))
    elif jogador == 1:
        print ('Você ganhou!')
    elif jogador == 2:
        print('O computador ganhou!')
    else:
        print('Jogada inválida')

elif computador == 1: #Papel
    if jogador == 0:
        print('O computador ganhou!')
    elif jogador == 1:
        print('O jogo empatou!')
    elif jogador == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida')

elif computador == 2: #Tesoura
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('O computador ganhou!')
    elif jogador == 2:
        print('O jogo empatou!')
    else:
        print('Jogada inválida')