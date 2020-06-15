def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('Você digitou um valor inválido, tente novamente!')
            continue
        else:
            return n 


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Você digitou um valor inválido, tente novamente!')
            continue
        else:
            return n


num = leiaInt('Insira um número inteiro: ')
num2 = leiaFloat('Insira um número real: ')
print(f'O número inteiro que você digitou foi {num} e o real foi {num2}')