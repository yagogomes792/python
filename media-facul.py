a1 = float(input('Insira a nota da primeira atividade: '))
a2 = float(input('Insira a nota da segunda atividade: '))
a3 = float(input('Insira a nota da terceira atividade: '))
a4 = float(input('Insira a nota da quarta atividade: '))
n2 = float(input('Insira a nota da prova N2: '))

m1 = (a1 + a2 + a3 + a4) / 4 * 0.4
m2 = n2 * 0.6
mf = m1 + m2

if mf >= 6.0:
    print('Sua nota foi {}, você passou, PARABÉNS!'.format(mf))
elif mf < 6.0:
    print('Sua nota foi {}, você não passou, faça a prova SUB!'.format(mf))
    
sub = float(input('Insira a nota da prova SUB: '))
final = sub * 0.6 + (m1)

if final > 6.0:
    print('Sua nota final foi {}, você passou, PARABÉNS!'.format(final))
else:
    print('Sua nota final foi {}, você foi REPROVADO!'.format(final))

