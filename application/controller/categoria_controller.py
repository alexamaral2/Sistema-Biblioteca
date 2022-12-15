from application.view.menu_livro_view import MenuLivroView
from application.view.menu_view import MenuView
from application.view.categoria_view import MenuCategoriaView
from application.model.dao.categoria_dao import CategoriaDao
from application.controller import biblioteca_controller

class CategoriaController: 

    def __init__(self):
        self.view = MenuView()
        self.viewLivro = MenuLivroView()
        self.viewCategoria = MenuCategoriaView()
        self.modelCategoria = CategoriaDao()
        
 
    def menu_Categoria(self):
        while True:
                opcao = self.view.menu_categoria()

                if opcao == 1:
                    nome, descricao, assunto = self.viewCategoria.cadastrar_categoria()
                    msg = self.viewCategoria.msg_sim_ou_nao("Adicionar")
                    if msg == "S":
                        retorno = self.modelCategoria.inserir(self.modelCategoria.gerar_id_categoria(),nome, descricao, assunto)
                        if retorno != False:
                            self.viewCategoria.msg("Adicionada")
                
                elif opcao == 2:
                    self.viewCategoria.visualizar_categorias()
                    retorno = self.modelCategoria.visualizar_se_categoria_existe()
                    if retorno == True:
                        idCategoria = self.viewCategoria.consultar_categoria_id()
                        categoria = self.modelCategoria.consultar_categoria_id_existe(idCategoria)

                        if categoria != False:
                            nome, descricao, assunto = self.viewCategoria.alterar_categoria()
                            msg = self.viewCategoria.msg_sim_ou_nao("Alterar")
                            if msg == "S":    
                                retorno = self.modelCategoria.alterar(categoria.id, nome, descricao, assunto)
                                if retorno != False:
                                    self.viewCategoria.msg("Alterada")
                        else:
                            self.viewCategoria.categoria_nao_localizada()
                        

                elif opcao == 3:
                    self.viewCategoria.visualizar_categorias()
                    retorno = self.modelCategoria.visualizar_se_categoria_existe()
                    if retorno == True:
                        idCategoria = self.viewCategoria.consultar_categoria_id()
                        categoria = self.modelCategoria.consultar_categoria_id_existe(idCategoria)

                        if categoria != False:
                            msg = self.viewCategoria.msg_sim_ou_nao("Excluir")
                            if msg == "S":
                                verificando = self.modelCategoria.excluir(categoria.id,categoria.nome, categoria.descricao, categoria.descricao)
                                if verificando == True:
                                    self.viewCategoria.msg("Excluida")
                        else:
                            self.viewCategoria.categoria_nao_localizada()    

                elif opcao == 4:
                    self.viewCategoria.visualizar_categorias()
                elif opcao == 5:
                    biblioteca = biblioteca_controller.BibliotecaController()
                    biblioteca.inicializa()
                else:
                    self.view.opcao_invalida()