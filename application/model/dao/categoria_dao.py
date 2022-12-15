from application.model.entity.livro import Categoria

class CategoriaDao:
    
    lista_categoria = [
        Categoria(1,"nome-categoria" ,"descricao-teste" ,"assunto-teste" , 0)
    ]
    
    @classmethod
    def inserir(cls, id,nome,descricao,assunto):
        retorno = cls.verificar_se_categoria_existe_nome(nome)
        if retorno == False:
            return cls.lista_categoria.append(Categoria(id,nome,descricao,assunto, 0))
        else:
            print("Atenção, Já existe uma categoria com o mesmo nome!")
            return False
    
    @classmethod
    def alterar(cls,id,nome,descricao,assunto):
        retorno = cls.verificar_se_categoria_existe_nome(nome)
        if retorno == False:
            for i in range(len(cls.consultar())):
                if cls.lista_categoria[i].id == id:
                    cls.lista_categoria[i] = Categoria(id,nome,descricao,assunto, 0)
        else:
            print("Atenção, Já existe uma categoria com o mesmo nome!")
            return False
    
    @classmethod
    def excluir(cls,id,nome, descricao, assunto):
        from application.model.dao.acervo_dao import AcervoDao
        categorias = AcervoDao()
        verificar_categoria = categorias.verificar_livro_categoria(id)
        
        if verificar_categoria != True:
            for i in range(len(cls.consultar())):
                if cls.lista_categoria[i].id == id:
                    cls.lista_categoria[i] = Categoria(id,nome,descricao,assunto, 1)
                    return True
        else:
            print("Atenção, Categoria está Vinculada ao Livro no Acervo!")
            return False
    
    @classmethod
    def consultar(cls):
        return cls.lista_categoria
    
    @classmethod
    def consultar_categoria_id (cls , valor):
        for categoria in cls.consultar():
            if categoria.id == valor:
                return categoria
        return False
    
    @classmethod
    def consultar_categoria_id_existe (cls , valor):
        for categoria in cls.consultar():
            if categoria.id == valor:
                if categoria.status == 0:
                    return categoria
        return False
    
    @classmethod
    def consultar_categoria_nome(self, nome):
        for categoria in self.lista_categoria:
            if categoria.nome == nome:
                return categoria
            else:
                return f'Categoria não localizada'
        return

    @classmethod
    def gerar_id_categoria(cls): 
          if len(cls.consultar()) == 0:
              return 1
          else:
              for categoria in cls.lista_categoria:
                  posicao = categoria.id
              return posicao + 1   
    
    def visualizar_se_categoria_existe(cls):
        categoria = CategoriaDao()
        categorias_cadastradas = 0

        for categorias in categoria.consultar():
            if categorias.status == 0:
                categorias_cadastradas += 1
                return True
           
        if categorias_cadastradas == 0:
            return False
    
    @classmethod
    def verificar_se_categoria_existe_nome(cls, nome_categoria):
        for categoria in cls.consultar():
           if categoria.status == 0:
                if categoria.nome == nome_categoria:
                    return True
        return False