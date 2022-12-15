from application.view.exemplar_view import MenuExemplarView
from application.view.menu_livro_view import MenuLivroView
from application.view.menu_view import MenuView
from application.model.dao.livro_dao import LivroDao
from application.model.dao.exemplar_dao import ExemplarDao
from application.controller import biblioteca_controller

class ExemplarController:
    
    def __init__(self):
        
        self.view = MenuView()
        self.viewExemplar = MenuExemplarView()
        self.viewLivro = MenuLivroView()
        self.model = LivroDao()
        self.modelExemplar = ExemplarDao()
        
    def menu_exemplar(self):
        while True:
            
            opcao = self.view.menu_exemplar()

            if opcao == 1:
                    self.viewLivro.visualizar_livros()
                    retorno = retorno = self.model.visualizar_se_livro_existe()
                    if retorno == True:
                        exemplar = self.viewExemplar.cadastrar_exemplar()
                        if self.model.consultar_livro_id_existe(exemplar) != False:
                            msg = self.viewExemplar.msg_sim_ou_nao("Adicionar")
                            if msg == "S":
                                self.modelExemplar.inserir(self.modelExemplar.gerar_id_exemplar(),exemplar,True , 1)
                                self.viewExemplar.msg("Adicionado")
                        else:
                            self.viewLivro.livro_nao_localizado()
                
            elif opcao == 2:
                self.viewExemplar.visualizar_exemplares()
                retorno = self.modelExemplar.visualizar_se_exemplar_existe()
                if retorno == True:
                    id_exemplar = self.viewExemplar.consultar_exemplar_id()
                    exemplar = self.modelExemplar.consultar_exemplar_id_existe(id_exemplar)

                    if exemplar != False:
                        circular = self.viewExemplar.alterar_exemplar()
                        if circular != "0":
                            msg = self.viewExemplar.msg_sim_ou_nao("Alterar")
                            if msg == "S":
                                self.modelExemplar.alterar(exemplar.id,exemplar.livro,circular,exemplar.qtd)
                                self.viewExemplar.msg("Alterado")
                    else:
                        self.viewExemplar.exemplar_nao_localizado()
                    

            elif opcao == 3:
                self.viewExemplar.visualizar_exemplares()
                retorno = self.modelExemplar.visualizar_se_exemplar_existe()
                if retorno == True:
                    idExemplar = self.viewExemplar.consultar_exemplar_id()
                    exemplar = self.modelExemplar.consultar_exemplar_id_existe(idExemplar)
                    
                    if exemplar != False:
                        msg = self.viewExemplar.msg_sim_ou_nao("Excluir")
                        if msg == "S":
                            retorno = self.modelExemplar.excluir(exemplar.id,exemplar.livro, exemplar.circular, exemplar.qtd)
                            if retorno != False:
                                self.viewExemplar.msg("Excluido")
                    else:
                        self.viewExemplar.exemplar_nao_localizado()    

            elif opcao == 4:
                self.viewExemplar.visualizar_exemplares()
            elif opcao == 5:
                biblioteca = biblioteca_controller.BibliotecaController()
                biblioteca.inicializa()
            else:
                self.view.opcao_invalida()   