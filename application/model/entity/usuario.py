class Usuario:
    def __init__(self, id, login, senha , nome, tipo , status_suspenso):
        self.__id = id
        self.__login = login
        self.__senha = senha
        self.__nome = nome
        self.__tipo = tipo
        self.__status_suspenso = status_suspenso
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor
    
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, valor):
        self.__login = valor
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, valor):
        self.__senha = valor
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def status_suspenso(self):
        return self.__status_suspenso
    
    @status_suspenso.setter
    def status_suspenso(self, valor):
        self.__status_suspenso = valor