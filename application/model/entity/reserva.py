#Tipo_cancelamento_reserva - Usuário ou Sistema

class Reserva:
    def __init__(self, id, usuario, emprestimo, data_reserva, status_emprestimo, tipo_usuario_cancelamento_reserva , status):
        self.__id = id
        self.__usuario = usuario
        self.__emprestimo = emprestimo
        self.__data_reserva = data_reserva
        self.__status_emprestimo = status_emprestimo
        self.__tipo_usuario_cancelamento_reserva = tipo_usuario_cancelamento_reserva
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
    def emprestimo(self):
        return self.__emprestimo
    
    @emprestimo.setter
    def emprestimo(self, valor):
        self.__emprestimo = valor
    
    @property
    def data_reserva(self):
        return self.__data_reserva
    
    @data_reserva.setter
    def data_reserva(self, valor):
        self.__data_reserva = valor
    
    @property
    def status_emprestimo(self):
        return self.__status_emprestimo
    
    @status_emprestimo.setter
    def status_emprestimo(self, valor):
        self.__status_emprestimo = valor
        
    @property
    def tipo_usuario_cancelamento_reserva(self):
        return self.__tipo_usuario_cancelamento_reserva
    
    @tipo_usuario_cancelamento_reserva.setter
    def tipo_usuario_cancelamento_reserva(self, valor):
        self.__tipo_usuario_cancelamento_reserva = valor
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor