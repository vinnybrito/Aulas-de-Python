class ContaBancaria:
    def __init__(self, agencia = '', numero = '', saldo = 0.0):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    #------------------------------GETTERS AND SETTERS------------------------------#

    @property
    def agencia(self):
        return self.__agencia
   
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero
   
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo
   
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo