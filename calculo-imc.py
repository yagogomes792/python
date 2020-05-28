peso = float(input('Insira o seu peso: (kg)'))
altura = float(input('Insira a sua altura: (m)'))

imc = peso / (altura**2)

if imc <= 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do peso!'.format(imc))
elif imc <= 24.9:
    print('Seu IMC é {:.1f}. Seu peso está normal!'.format(imc))
elif imc <=29.9:
    print('Seu IMC é {:.1f}. Você está com sobrepeso!'.format(imc))
elif imc <= 34.9:
    print('Seu IMC é {:.1f}. Você está com obesidade grau 1!'.format(imc))
elif imc <= 39.9:
    print('Seu IMC é {:.1f}. Você está com obesidade grau 2!'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está com obesidade grau 3!'.format(imc))