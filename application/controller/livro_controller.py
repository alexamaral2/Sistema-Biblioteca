from application.view.menu_livro_view import MenuLivroView
from application.view.menu_view import MenuView
from application.model.dao.livro_dao import LivroDao
from application.controller import biblioteca_controller

class LivroController: 

    def __init__(self):
        self.view = MenuView()
        self.viewLivro = MenuLivroView()
        self.model = LivroDao()
 
    def menu_livro(self):
        while True:
                opcao = self.view.menu_livro()

                if opcao == 1:
                    titulo,isbn ,autores, edicao, editora, ano, assuntos = self.viewLivro.cadastrar_livro()
                    msg = self.viewLivro.msg_sim_ou_nao("Adicionar")
                    if msg == "S":
                        retorno = self.model.inserir(self.model.gerar_id_Livro(),titulo,isbn ,autores, edicao, editora, ano, assuntos)
                        if retorno != False:
                            self.viewLivro.msg("Adicionado")
                
                elif opcao == 2:
                    self.viewLivro.visualizar_livros()
                    retorno = self.model.visualizar_se_livro_existe()
                    if retorno == True:
                        idLivro = self.viewLivro.consultar_livro_id()
                        livro = self.model.consultar_livro_id_existe(idLivro)
                            
                        if livro != False:
                            titulo,isbn ,autores, edicao, editora, ano, assuntos = self.viewLivro.alterar_livro()
                            msg = self.viewLivro.msg_sim_ou_nao("Alterar")
                            if msg == "S":
                                retorno = self.model.alterar(livro.id, titulo,isbn ,autores, edicao, editora, ano, assuntos)
                                if retorno != False:
                                    self.viewLivro.msg("Alterado")
                        else:
                            self.viewLivro.livro_nao_localizado()


                elif opcao == 3:
                    self.viewLivro.visualizar_livros()
                    retorno = self.model.visualizar_se_livro_existe()
                    if retorno == True:
                        idLivro = self.viewLivro.consultar_livro_id()
                        livro = self.model.consultar_livro_id_existe(idLivro)
                        
                        if livro != False:
                            msg = self.viewLivro.msg_sim_ou_nao("Excluir")
                            if msg == "S":
                                self.model.excluir(livro.id,livro.titulo,livro.isbn,livro.autores, livro.edicao, livro.editora, livro.ano, livro.assuntos)
                                self.viewLivro.msg("Excluido")
                        else:
                            self.viewLivro.livro_nao_localizado()    

                elif opcao == 4:
                    self.viewLivro.visualizar_livros()
                elif opcao == 5:
                    biblioteca = biblioteca_controller.BibliotecaController()
                    biblioteca.inicializa()
                else:
                    self.view.opcao_invalida()