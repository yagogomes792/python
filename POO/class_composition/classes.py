#CLASSE PRINCIPAL
class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        #LISTA ONDE SERÃO INSERIDOS OS ENDEREÇOS DA CLASSE ENDERECO
        self.enderecos = []
    #GETTER
    @property
    def nome(self):
        return self.__nome
    #SETTER
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    #GETTER
    @property
    def idade(self):
        return self.idade
    #SETTER
    @idade.setter
    def idade(self, idade):
        self.idade = idade
    
    #MÉTODO PARA INSERIR OS ENDEREÇOS DA CLASSE ENDERECO NA LISTA ENDERECOS DA CLASSE CLIENTE
    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    #MÉTODO PARA LISTAR OS ENDEREÇOS
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    #MÉTODO QUE MOSTRA QUAL OBJETO FOI DELETADO
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')
#CLASSE QUE FORNECERÁ DADOS PARA O ATRIBUTO ENDERECOS NA CLASSE CLIENTE (A CLASSE ENDERECO PERTENCE À CLASSE CLIENTE)
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    #MÉTODO PARA MOSTRAR QUAL OBJETO FOI DELETADO
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')