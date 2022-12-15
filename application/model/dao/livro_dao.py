from application.model.entity.livro import Livro


class LivroDao:
 
    lista_livros = [ 
        
        Livro(1, "titulo-teste" , "isbn-teste", "autores-teste", "edicao-teste" , "editora-teste", "ano-teste",
        "assunto-teste", 0)
        ]   

    @classmethod
    def inserir(cls,id, titulo, isbn, autores, edicao, editora, ano, assuntos):
        i, livro, retorno = cls.verificar_se_livro_existe(titulo)
        if retorno == 1: 
            cls.lista_livros[i] = Livro(livro.id, livro.titulo, isbn, autores, edicao, editora, ano, assuntos, 0)
            
            #Atualizando as informações do Livro no Exemplar
            from application.model.dao.exemplar_dao import ExemplarDao
            exemplar = ExemplarDao()
            exemplar.atualizar_livro_exemplar(livro.id)
        
        elif retorno == 3:
            cls.lista_livros.append(Livro(id, titulo, isbn, autores, edicao, editora, ano, assuntos, 0))
        else:
            print("Atenção, Já existe um livro cadastrado com o mesmo titulo!")
            return False
    
    @classmethod
    def alterar(cls,id, titulo, isbn, autores, edicao, editora, ano, assuntos):
        i, livro, retorno = cls.verificar_se_livro_existe(titulo)
        
        if retorno != 2:
            for i in range(len(cls.consultar())):
                if cls.lista_livros[i].id == id:
                    cls.lista_livros[i] = Livro(id, titulo, isbn, autores, edicao, editora, ano, assuntos, 0)

                    #Atualizando as informações do Livro no Exemplar
                    from application.model.dao.exemplar_dao import ExemplarDao
                    exemplar = ExemplarDao()
                    exemplar.atualizar_livro_exemplar(id)
        else:
            print("Atenção, Já existe um livro cadastrado com o mesmo titulo!")
            return False
          
    @classmethod
    def excluir(cls, id, titulo, isbn, autores, edicao, editora, ano, assuntos):
        for i in range(len(cls.consultar())):
            if cls.lista_livros[i].id == id:
                cls.lista_livros[i] = Livro(id, titulo, isbn, autores, edicao, editora, ano, assuntos, 1)
                
                #Atualizando as informações do Livro no Exemplar
                from application.model.dao.exemplar_dao import ExemplarDao
                exemplar = ExemplarDao()
                exemplar.atualizar_livro_exemplar(id)

    @classmethod
    def consultar(cls):
        return cls.lista_livros
    
    @classmethod
    def consultar_livro_id (cls, valor):
        for livro in cls.lista_livros:
            if livro.id == valor:
                return livro
        return False
    
    @classmethod
    def consultar_livro_id_existe (cls, valor):
        for livro in cls.lista_livros:
            if livro.id == valor and livro.status == 0:
                return livro
        return False
            
    @classmethod
    def gerar_id_Livro(cls): 
          if len(cls.consultar()) == 0:
              return 1
          else:
              for livro in cls.lista_livros:
                  posicao = livro.id
              return posicao + 1    
    
    # 1 - Livro Excluido
    # 2 - Livro Já Cadastrado
    # 3 - Não há o livro com o titulo desejado cadastrado
    @classmethod
    def verificar_se_livro_existe(cls , titulo):
        for i, livro in enumerate(cls.consultar()):
            if livro.titulo == titulo:
               if livro.status == 1:
                return i,livro, 1
               else:
                   return None, None, 2
            return None , None , 3
    
    def visualizar_se_livro_existe(cls):
        livro = LivroDao()
        livros_cadastrados = 0

        for livros in livro.consultar():
            if livros.status == 0:
                livros_cadastrados += 1
                return True
           
        if livros_cadastrados == 0:
            return False
               
