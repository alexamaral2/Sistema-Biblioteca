from application.model.entity.usuario import Usuario
from datetime import *
import time

class UsuarioDao:
    lista_login = []
    
    lista_usuario = [
        
        Usuario(1, "funcionario" ,"teste1" , "Funcionario", "Funcionario", False),
        Usuario(2, "bibliotecario" ,"teste2" , "Bibliotecario", "Bibliotecario", False),
        Usuario(3, "professor", "teste3" ,"Professor", "Professor", False),
        Usuario(4, "aluno", "teste4" ,"Aluno", "Aluno", False),
        Usuario(5, "admin", "123" ,"Administrador", "Administrador", False),
    ]
    
    
    @classmethod
    def cadastrar(cls, id,login, senha, nome, tipo_usuario):
        verificar_se_usuario_existe = cls.verificar_se_usuario_ja_foi_cadastrado(login, nome)
        if verificar_se_usuario_existe != True:
            cls.lista_usuario.append(Usuario(id, login, senha, nome, tipo_usuario, False))
            msg = False
        else:
            print("Atenção, já existe um usuário com o mesmo login")
            msg = True
        return msg
    
    @classmethod
    def exibir_todos_usuarios(cls):
        return cls.lista_usuario
    
    @classmethod
    def exibir_usuario_id(cls, valor):
        for usuario in cls.exibir_todos_usuarios():
            if usuario.id == valor:
                return usuario
    
    @classmethod
    def verificar_login(cls,valor):
        qtd_usuario = 0
        
        for usuario in cls.exibir_todos_usuarios():
            if usuario.login == valor:
                qtd_usuario += 1
        
        if qtd_usuario == 1:
            return True
        else: 
            return False
    
    @classmethod
    def verificar_senha(cls,valor_login, valor_senha):
        qtd_senha = 0
        for usuario in cls.exibir_todos_usuarios():
           if usuario.login == valor_login: 
                if usuario.senha == valor_senha:
                    usuario_login = usuario
                    qtd_senha += 1
        
        if qtd_senha == 1:
            return True, usuario_login
        else:
            return False, None
            
            

    @staticmethod
    def verifica_dia_semana():
        dia_da_semana = (datetime.today().weekday())
        dia_da_semana +=1
        dicionario = {1: "Segunda-Feira", 2: "Terça-Feira", 3: "Quarta-Feira", 4:"Quinta-Feira" , 5:"Sexta-Feira" , 6:"Sábado" , 7: "Domingo"}
        dia = dicionario.get(dia_da_semana, "None")
        
        if dia_da_semana >= 1 and dia_da_semana <= 7:
            if dia != "None":
                return date.today().strftime('%d/%m/%Y'), dia
        else:
            return False , None
    
    @classmethod
    def armazenar_usuario_login(cls,id,login,senha , nome ,tipo, status):
        return cls.lista_login.append(Usuario(id, login, senha, nome , tipo, status))
    
    
    @classmethod
    def verificar_tipo_usuario(cls, id):
        for usuario in cls.exibir_todos_usuarios():
            if usuario.id == id:
                if usuario.tipo == "Aluno" or usuario.tipo == "Funcionario":
                    return True
                elif usuario.tipo == "Professor":
                    return False
        return "None"
    
    @classmethod
    def limpar_lista_login(cls):
        return cls.lista_login.clear()
        
    @classmethod
    def exibir_usuario_login(cls):
        for usuario in cls.exibir_todos_usuarios():
            for usuario_login in cls.lista_login:
                if usuario.id == usuario_login.id:    
                    return usuario
    
    @classmethod
    def verificar_se_usuario_ja_foi_cadastrado(cls, login, nome):
        for usuario in cls.exibir_todos_usuarios():
            if usuario.login == login or usuario.nome == nome:
                return True

    @classmethod
    def exibir_usuario_nome(cls, nome):
        qtd_usuario = 0
        for usuario in cls.exibir_todos_usuarios():
            if usuario.nome == nome:    
                usuario_nome = usuario
                qtd_usuario +=1
        
        if qtd_usuario == 1:
            return usuario_nome
        else:
            return False
    
    @classmethod
    def verificar_se_usuario_existe(cls , id):
        for i, usuario in enumerate(cls.exibir_todos_usuarios()):
            if usuario.id == id:
                return i,usuario, True
        return False, False , False

    @classmethod
    def atualizar_usuario(cls,usuario, status_suspenso):
        i, usuario, usuarioExiste = cls.verificar_se_usuario_existe(usuario)
        
        if usuarioExiste == True:
            cls.lista_usuario[i] = Usuario(usuario.id, usuario.login, usuario.senha, usuario.nome ,usuario.tipo, status_suspenso)
        else:
            return None
    
    @classmethod
    def verificar_status_suspenso(cls ,id):
        for usuario in cls.exibir_todos_usuarios():
            if usuario.id == id:
                if usuario.status_suspenso == True:
                    return True
                else:
                    return False

    @classmethod
    def gerar_id_usuario(cls): 
          if len(cls.exibir_todos_usuarios()) == 0:
              return 1
          else:
              for usuario in cls.exibir_todos_usuarios():
                  posicao = usuario.id
              return posicao + 1 