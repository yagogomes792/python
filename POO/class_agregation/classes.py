#EXEMPLO DE CLASSE QUE PRECISA DOS ATRIBUTOS/MÉTODOS DE OUTRA CLASSE PARA FUNCIONAR
class Cart:
    def __init__(self):
        #LISTA ONDE SERÃO INSERIDOS OS DADOS DE OUTRA CLASSE
        self.produtos = []
    #RESPONSÁVEL POR INSERIR PRODUTOS NA LISTA
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    #RESPONSÁVEL POR LISTAR OS PRODUTOS DA LISTA
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    #RESPONSÁVEL POR SOMAR OS PRODUTOS DA LISTA
    def soma_produto(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


#CLASSE QUE IRÁ FORNECER DADOS PARA A CLASSE PRINCIPAL
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
