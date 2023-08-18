from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia = '', numero = '', saldo = 0, rentabilidade = 0.0):

        super().__init__(agencia, numero, saldo)
        self.__rentabilidade = rentabilidade

    #------------------------------GETTERS AND SETTERS------------------------------#

    @property
    def rentabilidade(self):
        return self.__rentabilidade
   
    @rentabilidade.setter
    def rentabilidade(self, rentabilidade):
        self.__rentabilidade = rentabilidade