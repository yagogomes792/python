#CLASSE PRINCIPAL QUE FUNCIONARÁ COMO BASE PARA AS OUTRAS CLASSES (CLASSE PAI OU SUPERCLASSE)
class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    #GETTER
    @property
    def nome(self):
        return self.__nome
    #SETTER
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    #GETTER
    @property
    def idade(self):
        return self.__idade
    #SETTER
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
#CLASSE QUE HERDA OS ATRIBUTOS DA CLASSE PAI. É CHAMADA DE SUBCLASSE
class Cliente(Pessoa):
    def falar(self):
        print(f'{self.nome} está falando...')
    #MÉTODO ESPECÍFICO DA CLASSE CLIENTE
    def comprar(self):
        print(f'{self.nome} está comprando...')
#CLASSE QUE HERDA OS ATRIBUTOS DA CLASSE PAI. É CHAMADA DE SUBCLASSE
class Aluno(Pessoa):
    def falar(self):
        print(f'{self.nome} está falando...')
    #MÉTODO ESPECÍFICO DA CLASSE ALUNO
    def estudar(self):
        print(f'{self.nome} está estudando...')