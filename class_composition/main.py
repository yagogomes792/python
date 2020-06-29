#COMPOSIÇÃO É O TIPO MAIS FORTE DE RELAÇÃO ENTRE CLASSES, POIS UMA CLASSE PODE SER O DONO DE OBJETOS DE UMA OUTRA CLASSE
#CASO ESSA CLASSE SEJA APAGADA OS OBJETOS TAMBÉM NÃO FUNCIONARÃO MAIS EM OUTRA CLASSE
from classes import Cliente
#OBJETO DA CLASSE CLIENTE QUE UTILIZA DADOS DA CLASSE ENDERECO, CASO O OBJETO CLIENTE SEJA DELETADO O OBJETO DE ENDERECO
#TAMBÉM SERÁ DELETADO
c1 = Cliente('Yago', 27)
c1.inserir_endereco('São Paulo', 'SP')
print(c1.nome)
c1.lista_enderecos()
del c1

c2 = Cliente('Robert', 32)
c2.inserir_endereco('Rio de Janeiro', 'RJ')
print(c2.nome)
c2.lista_enderecos()
del c2

c3 = Cliente('Ana', 19)
c3.inserir_endereco('Curitiba', 'PR')
print(c3.nome)
c3.lista_enderecos()

print('##################################################')
#CASO O OBJETO NÃO FOSSE DELETADO MANUALMENTE O GARBAGE COLLECTOR DELETA OS OBJETOS DEVIDO AOS MÉTODOS INSTANCIADOS