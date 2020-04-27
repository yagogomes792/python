from random import randint

print('Olá, tente adivinhar qual número eu escolho entre 0 e 10.')
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Escolha seu número: '))
    palpite +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
    
print('Você acertou! O número escolhido foi {}, PARABÉNS'.format(computador))
print('Você tentou {} vezes'.format(palpite))
