#PRIMEIRA CLASSE
class Escritor():
    def __init__(self, nome):
        self.__nome = nome
        self.ferramenta = None
    #GETTER
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
    
#SEGUNDA CLASSE
class Caneta():
    def __init__(self, marca):
        self.__marca = marca
    #GETTER
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta está escrevendo...')

#TERCEIRA CLASSE
class MaquinaDeEscrever():
    def escrever(self):
        print('Máquina está escrevendo...')