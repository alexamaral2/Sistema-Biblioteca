class Livro:
    #Status 0 - Livro Ativo
    #Stauts 1 - Livro Excluido

    def __init__(self, id = None, titulo = None , isbn = None , autores = None, edicao = None , editora = None, ano = None, assuntos = None, status = 0):
        self.__id = id
        self.__titulo = titulo
        self.__isbn = isbn
        self.__autores = autores
        self.__edicao = edicao 
        self.__editora = editora
        self.__ano = ano
        self.__assuntos = assuntos
        self.__status = status

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor
    
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, valor):
        self.__isbn = valor
    
    @property
    def autores(self):
        return self.__autores
    
    @autores.setter
    def isbn(self, valor):
        self.__isbn = valor
    
    @property
    def edicao(self):
        return self.__edicao
    
    @edicao.setter
    def edicao(self, valor):
        self.__edicao = valor
    
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, valor):
        self.__editora = valor

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        self.__ano = valor
    
    @property
    def assuntos(self):
        return self.__assuntos
    
    @assuntos.setter
    def assuntos(self, valor):
        self.__assuntos = valor
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, valor):
        self.__status = valor

class Exemplar():
    def __init__(self, id = None, livro = None , circular = None, status = None , qtd = None):
        self.__id = id
        self.__livro = livro
        self.__circular = circular
        self.__status = status
        self.__qtd = qtd
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = id
    
    @property
    def livro(self):
        return self.__livro
    
    @livro.setter
    def livro(self,valor):
        self.__livro = valor
        
    @property
    def circular(self):
        return self.__circular
    
    @circular.setter
    def circular(self,valor):
        self.__circular = valor
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor
    
    @property
    def qtd(self):
        return self.__qtd

    @qtd.setter
    def qtd(self, valor):
        self.__qtd = valor
    

class Categoria:
    def __init__(self, id = None, nome = None, descricao = None, assunto = None ,status = None):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__assunto = assunto
        self.__status = status
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__nome = valor
    
    @property
    def assunto(self):
        return self.__assunto

    @assunto.setter
    def assunto(self, valor):
        self.__assunto = valor
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor