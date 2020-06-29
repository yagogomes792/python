#NA ASSOSSIAÇÃO UMA CLASSE NÃO PEDENDE DA OUTRA PARA FUNCIONAR, BASTA VOCÊ FAZER REALAÇÃO DE UM ATRIBUTO

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

e = Escritor('Yago')
print(e.nome)
c = Caneta('Bic')
print(c.marca)
m = MaquinaDeEscrever()
m.escrever()

#REALIZANDO ASSOCIAÇÃO ENTRE AS CLASSES ESCRITOR E CANETA/MAQUINADEESCREVER
e.ferramenta = c
#e.ferramenta = m
e.ferramenta.escrever()