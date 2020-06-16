def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Insira uma opção válida!')
        else:
            return n


def linha(tam=40):
    return f'-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabeçalho('Selecione uma opção')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Qual a sua opção: ')
    return opc
