from application.model.dao.reserva_dao import ReservaDao
from application.model.dao.usuario_dao import UsuarioDao
from application.view.exemplar_view import MenuExemplarView
from application.view.emprestimo_view import MenuEmprestimoView
from application.view.reserva_view import MenuReservaView


class AdministradorBibliotecaController:
    def __init__(self):
        from application.view.menu_view import MenuView
        self.menu_view_principal = MenuView()
        
        self.modelReserva = ReservaDao()
        self.modelUsuario = UsuarioDao()
        self.menuExemplar = MenuExemplarView()
        self.menuEmprestimo = MenuEmprestimoView()
        self.menuReserva = MenuReservaView()
 
    def menu(self):
        usuario = self.modelUsuario.exibir_usuario_login()
        data, dia = self.modelUsuario.verifica_dia_semana()
        
        #Cancelando Reservas Automaticamente na inicialização
        self.modelReserva.cancelar_reserva_automaticamente()
        
        while True:
            opcao = self.menu_view_principal.menu_administrador(usuario.nome,data,dia)
            if opcao == 1:
                from application.view.menu_livro_view import MenuLivroView
                from application.view.exemplar_view import MenuExemplarView
                
                livro = MenuLivroView()
                exemplar = MenuExemplarView()
                
                livro.visualizar_livros()
                exemplar.visualizar_exemplares()
                
                exemplar.qtd_exemplar_total()

            elif opcao == 2:
                self.menuEmprestimo.exibir_todos_emprestimos()
            
            elif opcao == 3:
                self.menuReserva.exibir_todas_reservas()
            
            elif opcao == 4:
                from application.view.usuario_view import UsuarioView
                usuario_view = UsuarioView()
                usuario_view.exbir_usuarios()
            
            elif opcao == 5:
                self.menuEmprestimo.exibir_todos_emprestimos_atrasados()
            
            elif opcao == 6:
                from application.controller.usuario_controller import UsuarioController
                usuario = UsuarioController()
                usuario.inicializa()
            else:
                from application.view.menu_view import MenuView
                menu = MenuView()
                menu.opcao_invalida()
