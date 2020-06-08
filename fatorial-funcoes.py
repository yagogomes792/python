
def fatorial(num, show=False):
    """
    calculo de numeros fatoriais.
    num: numero fatorado
    show: (opcional )deve ou nao mostrar o calculo
    for: laco de repeticao para decrementar o numero a ser fatorado
    f *= c: f se transforma no resultado da multiplicacao de c e o multiplica pelo decremento
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(8, show=True))


