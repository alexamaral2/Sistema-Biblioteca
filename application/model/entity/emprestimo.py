class Emprestimo:
    def __init__(self, id = None, usuario = None, exemplar = None, data_emprestimo = None, data_devolucao = None, status_devolucao = None, status_cancelado = None, status_entrega_com_atraso = None, status = None):
        self.__id = id
        self.__usuario = usuario
        self.__exemplar = exemplar
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
        self.__status_devolucao = status_devolucao
        self.__status_cancelado = status_cancelado
        self.__status_entrega_com_atraso = status_entrega_com_atraso
        self.__status = status
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor

    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, valor):
        self.__usuario = valor
    
    @property
    def exemplar(self):
        return self.__exemplar
    
    @exemplar.setter
    def exemplar(self, valor):
        self.__exemplar = valor
    
    @property
    def data_emprestimo(self):
        return self.__data_emprestimo

    @data_emprestimo.setter
    def data_emprestimo(self, valor):
        self.__data_emprestimo = valor

    @property
    def data_devolucao(self):
        return self.__data_devolucao
    
    @data_devolucao.setter
    def data_devolucao(self, valor):
        self.__data_devolucao = valor
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, valor):
        self.__status = valor
    
    @property
    def status_devolucao(self):
        return self.__status_devolucao
    
    @status_devolucao.setter
    def status_devolucao(self, valor):
        self.__status_devolucao = valor
    
    @property
    def status_cancelado(self):
        return self.__status_cancelado
    
    @status_cancelado.setter
    def status_cancelado(self, valor):
        self.__status_cancelado = valor
    
    
    @property
    def status_entrega_com_atraso():
        return self.__status_entrega_com_atraso

    @status_entrega_com_atraso.setter
    def status_entrega_com_atraso(self, valor):
        self.__status_entrega_com_atraso = valor