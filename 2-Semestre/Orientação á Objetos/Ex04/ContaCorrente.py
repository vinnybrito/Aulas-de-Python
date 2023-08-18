from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia = '', numero = '', saldo = 0, checkEspecial = ''):

        super().__init__(agencia, numero, saldo)
        self.__checkEspecial = checkEspecial

    #------------------------------GETTERS AND SETTERS------------------------------#
    
    @property
    def cpf(self):
        return self.__cpf
   
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf