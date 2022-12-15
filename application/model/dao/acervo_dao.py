from application.model.entity.biblioteca import Acervo
from application.model.dao.exemplar_dao import ExemplarDao
from application.model.dao.livro_dao import LivroDao
from application.model.dao.categoria_dao import CategoriaDao

class AcervoDao:
    def __init__(self) -> None:
        self.categoria = CategoriaDao()
        self.livro = LivroDao()
        self.exemplar = ExemplarDao() 
        
        self.lista_acervo = [
            Acervo(1,self.categoria.consultar_categoria_id(1),[self.livro.consultar_livro_id(1)],[self.exemplar.consultar_exemplar_id(1)])

        ]
    
    def consultar_acervo (self , pequisa_usuario):
        for acervo in self.lista_acervo:
            for livro in acervo.livro:
                for exemplar in acervo.exemplar:
                    if livro.status == 0 and acervo.categoria.status == 0:    
                        if acervo.categoria.nome == pequisa_usuario:
                            if livro.titulo == exemplar.livro.titulo and exemplar.qtd > 0:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos} | Qtd de exemplares: {exemplar.qtd}")
                                consultar_livro = False

                            else:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos}")
                                consultar_livro = False

                        elif acervo.categoria.descricao == pequisa_usuario:
                            if livro.titulo == exemplar.livro.titulo and exemplar.qtd > 0:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos} | Qtd de exemplares: {exemplar.qtd}")
                                consultar_livro = False
                            else:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos}")
                                consultar_livro = False

                        elif acervo.categoria.assunto == pequisa_usuario:
                            if livro.titulo == exemplar.livro.titulo and exemplar.qtd > 0:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos} | Qtd de exemplares: {exemplar.qtd}")
                                consultar_livro = False

                            else:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos}")
                                consultar_livro = False

                        elif livro.titulo == pequisa_usuario:
                            if livro.titulo == exemplar.livro.titulo and exemplar.qtd > 0:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos} | Qtd de exemplares: {exemplar.qtd}")
                                consultar_livro = False
                            else:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos}")
                                consultar_livro = False
                        else:
                             consultar_livro = True
                    else:
                         consultar_livro = True
        
        #Se o Livro não estiver vinculado a Categoria
        if consultar_livro == True:
            from application.model.dao.livro_dao import LivroDao
            from application.model.dao.exemplar_dao import ExemplarDao
            
            livros = LivroDao()
            exemplares = ExemplarDao()
            qtd_livros_exemplar = 0
            
            for livro in livros.consultar():
                for exemplar in exemplares.consultar():
                    if livro.titulo == pequisa_usuario:
                        if livro.status == 0:
                            if livro.titulo == exemplar.livro.titulo and exemplar.qtd > 0:
                                print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos} | Qtd de exemplares: {exemplar.qtd}")
                                qtd_livros_exemplar += 1
                    
            if qtd_livros_exemplar == 0:
                
                qtd_livros = 0
                for livro in livros.consultar():
                    if livro.titulo == pequisa_usuario:    
                        if livro.status == 0:
                            print(f"N° Livro: {livro.id} | Titulo: {livro.titulo} | ISBN: {livro.isbn} | Autores: {livro.autores} | Edição: {livro.edicao} | Editora: {livro.editora} | Ano: {livro.ano} | Assunto(s): {livro.assuntos}")
                            qtd_livros += 1
                
                if qtd_livros == 0:
                    print("Atenção, Não foi possivel localizar o livro!")
                  
    def verificar_livro_categoria(self, valor):
        for acervo in self.lista_acervo:
            if acervo.categoria.id == valor:
                return True
        return False
        