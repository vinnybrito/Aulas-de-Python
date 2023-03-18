from ContaBancaria import ContaBancaria

class Cliente:
    def __init__(self, id = '', nome = '', idade = 0, email = '', conta = ContaBancaria ):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__conta = conta

        def exibirDadosConta(self):
            return ("Agência: " + str(self.conta.agencia))


    #------------------------------GETTERS AND SETTERS------------------------------#

    @property
    def id(self):
        return self.__id
   
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome
   
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
   
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def email(self):
        return self.__email
   
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def conta(self):
        return self.__conta
   
    @email.setter
    def conta(self, conta):
        self.__conta = conta
