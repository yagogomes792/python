#EXEMPLO DE UTILIZAÇÃO DE GETTERS AND SETTERS

class Produto:

    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
    

    def desconto(self, taxa):
        self.preço = self.preço - (self.preço * (taxa / 100))
        print(f'O produto {self.nome} com desconto de {taxa}% fica {self.preço:.2f}')
    

    #GETTER
    @property
    def nome(self):
        return self._nome
    
    #SETTER
    @nome.setter
    def nome(self, nome):
         self._nome = nome.title()
    

    #GETTER
    @property
    def preço(self):
        return self._preço
    
    #SETTER
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        
        self._preço = valor