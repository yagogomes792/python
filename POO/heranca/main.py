#ASSOSSIAÇÃO = USA, AGREGAÇÃO = TEM, COMPOSIÇÃO = É DONO, HERANÇA = É
# HERANÇA É QUANDO UM OBJETO É OUTRO OBJETO
from classes import Pessoa, Cliente, Aluno

#INSTANCIAÇÃO DA CLASSE CLIENTE
c1 = Cliente('Yago', 27)
#MÉTODO DE AMBAS AS CLASSES
c1.falar()
#MÉTODO ESPECÍFICO DA CLASSE CLIENTE
c1.comprar()

print()

#INSTANCIAÇÃO DA CLASSE ALUNO
a1 = Aluno('Jonas', 32)
#MÉTODO DE AMBAS AS CLASSES
a1.falar()
#MÉTODO ESPECÍFICO DA CLASSE ALUNO
a1.estudar()