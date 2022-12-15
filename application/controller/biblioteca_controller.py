from application.view.menu_view import MenuView
from application.controller.livro_controller import LivroController
from application.controller.exemplar_controller import ExemplarController
from application.controller.categoria_controller import CategoriaController
from application.controller.acervo_controller import AcervoController
from application.controller.emprestimo_controller import EmprestimoController
from application.controller.reserva_controller import ReservaController
from application.view.usuario_view import UsuarioView
from application.model.dao.usuario_dao import UsuarioDao
from application.model.dao.reserva_dao import ReservaDao
from application.controller.relatorio_gerencial_controller import RelatorioGerencialController

class BibliotecaController:
    def __init__(self):
        self.livroController = LivroController()
        self.exemplarController = ExemplarController()
        self.categoriaController = CategoriaController()
        self.acervoController = AcervoController()
        self.emprestimoController = EmprestimoController()
        self.reservaController = ReservaController()
        self.modelUsuario = UsuarioDao()
        self.view = MenuView()
        self.viewUsuario = UsuarioView()
        self.modelReserva = ReservaDao()
        self.relatorio_gerencial_controller = RelatorioGerencialController()
        
    
    def exibir_usuario(self):
        return self.modelUsuario.exibir_usuario_login()
    
    def data_atual(self):
        data, dia = self.modelUsuario.verifica_dia_semana()
        return data,dia
    
    def inicializa(self):
        while True:
            usuario = self.exibir_usuario()
            data, dia = self.data_atual()
            opcao = self.view.inicializa(usuario.login, data, dia)
            self.menu(opcao)
        
    def menu(self,opcao):
        #Cancelando Reservas Automaticamente na inicialização
        self.modelReserva.cancelar_reserva_automaticamente()
        
        if opcao == 1:
            self.livroController.menu_livro()
            
        elif opcao == 2:
            self.exemplarController.menu_exemplar()
        
        elif opcao == 3:    
            self.categoriaController.menu_Categoria()
        
        elif opcao == 4:
            self.acervoController.menu_livro()
        
        elif opcao == 5:
            self.emprestimoController.menu_emprestimo()
        
        elif opcao == 6:
            self.reservaController.menu_reserva()
            
        elif opcao == 7:
            self.relatorio_gerencial_controller.menu_relatorio()
        
        elif opcao == 8:
            from application.controller.usuario_controller import UsuarioController
            usuario = UsuarioController()
            usuario.menu_usuario()
        
        elif opcao == 9: 
                from application.controller.usuario_controller import UsuarioController
                usuario = UsuarioController()
                usuario.inicializa()
               
        else:
            self.view.opcao_invalida()


