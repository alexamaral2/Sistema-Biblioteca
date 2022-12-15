class Acervo:
    def __init__(self,id, categoria, livro, exemplar):
        self.__id = id
        self.__categoria = categoria
        self.__livro = livro
        self.__exemplar = exemplar
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor
    
    @property
    def livro(self):
        return self.__livro
    
    @livro.setter
    def livro(self, valor):
        self.__livro = valor
    
    @property
    def exemplar(self):
        return self.__exemplar
    
    @exemplar.setter
    def exemplar(self, valor):
        self.__exemplar = valor