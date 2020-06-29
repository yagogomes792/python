from datetime import datetime
from random import randint

#CLASSE DO PROGRAMA. A PARTIR DAQUI OS OBJETOS SERÃO INSTÂNCIADOS
class Pessoa:
    #VARIÁVEL DE CLASSE. PODE SER UTILIZADA EM TODAS AS INSTÂNCIAS DA CLASSE (GLOBAL)
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    #ATRIBUTOS DA CLASSE
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    #MÉTODOS PARA INSTÂNCIAS. SÓ PODE SER USADAS COM INSTÂNCIAÇÃO
    def falar(self, assunto=''):
        if self.comendo:
            print(f'{self.nome} não pode falar, pois está comendo')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        
        print(f'{self.nome} está conversando sobre {assunto}')
        self.falando = True
    

    def pfalar(self):
        if not self.falando:
            print(f'{self.nome} já parou de falar')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False


    def comer(self, alimento=''):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} não pode comer, pois está falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
    

    def pcomer(self, alimento=''):
        if not self.comendo:
            print(f'{self.nome} já parou de comer')
            return
        print(f'{self.nome} não está comendo')
        self.comendo = False

    
    def get_nascimento(self):
        print(self.ano_atual - self.idade)
    
    #EXEMPLO DE UTILIZAÇÃO DO MÉTODO DE CLASSE A PARTIR DE UMA VARIÁVEL DE CLASSE
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    #EXEMPLO DE UTILIZAÇÃO DE MÉTODO ESTÁTICO. PODE SER UTILIZADO, TANTO COM A CLASSE, QUANTO COM A INSTÂNCIA
    @staticmethod
    def get_id():
        id = randint(00000, 99999)
        return id