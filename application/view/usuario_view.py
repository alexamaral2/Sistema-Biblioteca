import getpass
from application.model.dao.usuario_dao import UsuarioDao

class UsuarioView:
    @staticmethod
    def cadastro_suceso():
        print("Usuário Cadastrado com sucesso!!")
    
    @staticmethod
    def msg_implementacao():
        print("Atenção, Sistema em Implementação!!")
    
    @staticmethod
    def msg_cadastro():
        print('Não Foi possivel cadastrar o usuário: ')
    
    @staticmethod
    def menu_inicial():
        print("=-=-=-=-= Biblioteca =-=-=-=-=")
    
    @staticmethod
    def dia_da_semana(data, dia):
        print(f"=-=- {dia} - {data} -=-=\n")
   
    @staticmethod
    def nome_usuario(nome):
        print(f"Usuario: {nome}")
               
    
    @staticmethod
    def cadastrar():
        try:
            print("=-=-=-=- 1 - Cadastrar Usuário =-=-=-=-")

            login = input("Digite o login do usuário: ")
            while login == "" or login == None:
                print("Atenção, valor inválido!")
                login = input("Digite o login do usuário: ")
            
            senha = input("Digite a senha do usuário: ")
            while senha == "" or senha == None:
                print("Atenção, valor inválido!")
                senha = input("Digite a senha do usuário: ")
            
            nome = input("Digite o nome do usuario: ")
            while nome == "" or nome == None:
                print("Atenção, valor inválido!")
                nome = input("Digite o nome do usuario: ")    
            
            print("=-=- Tipo Usuário =-=-")
            print('1 - Aluno ')
            print('2 - Professor ')
            print('3 - Funcionario ')
            print('4 - Bibliotecario ')
            print('5 - Administrador ')

            tipo_usuario = int(input("Digite o n° de tipo do usuário: "))
            while tipo_usuario < 1 or tipo_usuario > 5:
                print("Atenção, tipo de usuário inválido!")
                tipo_usuario = int(input("Digite o n° de tipo do usuário: "))

            dicionario = {1:'Aluno' , 2:'Professor' ,3:'Funcionario' , 4:'Bibliotecario' , 5:'Administrador'}
            retorno = dicionario.get(tipo_usuario)
            return login,senha,nome,retorno
        except ValueError:
            return False, False, False , False
    
    @staticmethod
    def input_nome_usuario():
        try:
            nome_usuario = input("Digite o nome do usuário: ")
            while nome_usuario == "" or nome_usuario == None:
                print("Atenção, valor Inválido")
                nome_usuario = input("Digite o nome do usuário: ")
            return nome_usuario
        except ValueError:
            print("Valor Inválido!")
               
    @staticmethod
    def biblioteca_fechada():
        print("Biblioteca Fechada!!")
        print("Dias de Funcionamento: De Segunda-Feira a Sexta-Feira")

    @staticmethod
    def finalizar():
        print("Encerrando Programa..")
        print("Programa Encerrado!")
        exit()
    
    @staticmethod
    def menu_login():
        login = input("Digite o login (ou 0 para sair): ")
        return login
    
    @staticmethod
    def menu_senha():
        senha = getpass.getpass("Digite a senha (ou 0 para sair): ")
        return senha
    @staticmethod
    def msg(valor):
        print(f"{valor} inválido(a), Tente Novamente!")
    
    @staticmethod
    def exbir_usuario_nome(nome):
        usuario = UsuarioDao()
        usuario_nome = usuario.exibir_usuario_nome(nome)
        print("=-=-=-=- Lista de Usuários =-=-=-=-")
        if usuario_nome != False:
            print(f"N° Usuário: {usuario_nome.id} | Nome Usuário: {usuario_nome.nome}")
            print("-=-=-=-=")
            msg = False
            usuario_final = usuario_nome
        else:
            print("Usuário Inexistente!")
            msg = True
            usuario_final = False
        
        return msg,usuario_final
    
    @staticmethod
    def exbir_usuarios():
        usuario = UsuarioDao()
        qtd_usuarios = 0 
        
        print("=-=-=-=- Lista de Usuários =-=-=-=-")
        for usuarios in usuario.exibir_todos_usuarios():
            print(f"N° Usuário: {usuarios.id} | Nome Usuário: {usuarios.nome} | Tipo: {usuarios.tipo}")
            print("-=-=-=-=")
            qtd_usuarios += 1
        
        if qtd_usuarios == 0:
            print("Não há usuários cadastrados no sistema!")
    
    @staticmethod
    def msg_tentativas():
        print("Numero de Tentativas Excedida!")
        print("Encerrando programa..")
        print("Programa Encerrado!!")