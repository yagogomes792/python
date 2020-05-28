from random import randint
print('Jogo do Par ou Ímpar')
print('-='*11)
c = 0

while True:    
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    soma = jogador + computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} o total é {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            c += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu!')
            c +=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!')
print('Game Over')
print(f'Você ganhou {c} vezes')