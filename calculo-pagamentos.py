valor = float(input('Qual o valor do produto? R$'))

print('''Formas de pagamento:
[ 1 ] A vista dinheiro/cheque
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opt = int(input('Escolha uma opção: '))

if opt == 1:
    total = valor - ( valor * 10/100)
    print('Você terá um desconto de 10% ' 'e pagará no total R${}'.format(total))
elif opt == 2:
    total = valor - ( valor * 5/100)
    print('Você terá um desconto de 5% ' 'e pagará no total R${}'.format(total))
elif opt == 3:
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))
    print('Você pagará o valor normal')
elif opt == 4:
    total = valor + (valor * 20/100)
    totalparc =int(input('Qual será a quantidade de parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${}'.format(totalparc, parcela ))
    print('Voce terá um acréscimo de 20% ' 'e pagará R${}'.format(total))
else:
    print('Opção de pagamento inválida!')