from application.model.dao.usuario_dao import UsuarioDao
from application.model.entity.usuario import Usuario
from application.view.usuario_view import UsuarioView
from application.model.dao.reserva_dao import ReservaDao
from application.controller.biblioteca_controller import BibliotecaController
from application.controller.administrador_controller import AdministradorBibliotecaController

class UsuarioController:
    def __init__(self):
        self.usuario_administrador_controller = AdministradorBibliotecaController()
        self.view = UsuarioView()
        self.model = UsuarioDao()
        self.model_reserva = ReservaDao()
        self.biblioteca_controller = BibliotecaController()
    
    def inicializa(self):
        #Cancelando Reservas Automaticamente na inicialização
        self.model_reserva.cancelar_reserva_automaticamente()
        
        self.view.menu_inicial()
        data, dia = self.model.verifica_dia_semana()
       
        if data != False:
            self.view.dia_da_semana(data,dia)
            login = self.view.menu_login()
            cont_login = 0
            if login != "0":
                while self.model.verificar_login(login) != True:
                   self.view.msg("login")
                   login = self.view.menu_login() 
                   cont_login += 1

                   if login == "0":
                       self.view.finalizar()

                   elif cont_login == 3:
                       self.view.msg_tentativas()
                       exit()
            else:
                self.view.finalizar()
               
            if cont_login != 3:
                cont_senha = 0

                senha = self.view.menu_senha()
                verificar_senha, usuario = self.model.verificar_senha(login,senha)
                
                if senha != "0":
                
                    while verificar_senha != True:
                        self.view.msg("senha")
                        senha = self.view.menu_senha()
                        verificar_senha, usuario = self.model.verificar_senha(login,senha)
                        cont_senha += 1

                        if senha == "0":
                             self.view.finalizar()

                        elif cont_senha == 3:
                            self.view.msg_tentativas()
                            exit()
                else:
                     self.view.finalizar()
                
                if login != "0" and senha != "0":
                    if cont_senha !=3:            
                        self.model.limpar_lista_login()
                        self.model.armazenar_usuario_login(usuario.id, usuario.login , usuario.senha , usuario.nome, usuario.tipo, usuario.status_suspenso)
                        if usuario.tipo == "Bibliotecario":
                            self.biblioteca_controller.inicializa()
                        elif usuario.tipo == "Administrador":
                            self.usuario_administrador_controller.menu()
                        else:
                            self.view.msg_implementacao()
                            exit()
                else:
                    self.view.finalizar()
        else:
            self.view.biblioteca_fechada()
            
    def menu_usuario(self):
        from application.view.menu_view import MenuView
        menu_principal = MenuView()
        
        while True:
            opcao = menu_principal.menu_usuario()
            
            if opcao == 1:
                 login,senha,nome,tipo_usuario = self.view.cadastrar()
                 
                 if login != False:
                     retorno = self.model.cadastrar(self.model.gerar_id_usuario(), login, senha, nome, tipo_usuario)
                     if retorno == False:
                         self.view.cadastro_suceso()
                 else:
                     self.view.msg_cadastro() 
                 
            elif opcao == 2:
                self.view.exbir_usuarios()
            elif opcao == 3:
                self.biblioteca_controller.inicializa()
            else:    
                menu_principal.opcao_invalida()
                
        
    

