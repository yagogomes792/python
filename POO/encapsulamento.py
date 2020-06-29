"""
_ = private/protected (O atributo permanece publico e pode ser editado, mas por boa pratica é melhor não modificá-la)
__ = private ( O atributo também pode ser chamado fora da classe, mas é criado um novo atributo. 
    O atributo da classe permanece o mesmo)
"""
class BaseDeDados:
    def __init__(self):
        #atributo "privado"
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados


    #método para inserir dados em um dicionário
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    #método para mostrar dados do dicionário
    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    #métodos para apagar dados de um dicionário
    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]