from application.view.menu_view import MenuView
from application.view.acervo_view import MenuAcervoView
from application.controller import biblioteca_controller

class AcervoController: 

    def __init__(self):
        self.view = MenuView()
        self.viewAcervo = MenuAcervoView()
 
    def menu_livro(self):
        while True:
                opcao = self.view.menu_acervo()

                if opcao == 1:
                     pesquisa = self.viewAcervo.consultar_acervo()
                     self.viewAcervo.visualizar_acervo(pesquisa)
                
                elif opcao == 2:
                    biblioteca = biblioteca_controller.BibliotecaController()
                    biblioteca.inicializa()
                        
                else:
                    self.view.opcao_invalida()