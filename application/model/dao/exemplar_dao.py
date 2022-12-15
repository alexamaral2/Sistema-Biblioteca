from application.model.entity.livro import Exemplar
from application.model.dao.livro_dao import LivroDao

class ExemplarDao:   
    livros = LivroDao()
    
    lista_exemplares = [ 
            
        Exemplar(1, livros.consultar_livro_id(1), True, 0, 10)
        
        ]   

    @classmethod
    def inserir(cls,id,livro, circular, qtd):
        i,exemplar, exemplarExiste = cls.verificar_se_exemplar_existe(livro)
        if exemplarExiste == True:
            cls.lista_exemplares[i] = Exemplar(exemplar.id,cls.livros.consultar_livro_id(livro), circular, 0, cls.aumentar_quantidade(exemplar.id))
        
        else:
            return cls.lista_exemplares.append(Exemplar(id,cls.livros.consultar_livro_id(livro), circular, 0, 1))
    
    @classmethod
    def alterar(cls,id,livro, circular, qtd):
        for i in range(len(cls.consultar())):
            if cls.lista_exemplares[i].id == id:
                cls.lista_exemplares[i] = Exemplar(id,livro, circular, 0, qtd)
                
                from application.model.dao import emprestimo_dao
                emprestimo = emprestimo_dao.EmprestimoDao()
                emprestimo.atualiza_emprestimo(id)

    
    @classmethod
    def excluir(cls,id,livro, circular, qtd):
        exemplar = cls.consultar_exemplar_id_existe(id)
        if exemplar.qtd > 0:
            from application.model.dao.emprestimo_dao import EmprestimoDao
            emprestimos = EmprestimoDao()
            exemplar_esta_vinculado_a_emprestimo = emprestimos.verificar_se_emprestimo_existe_pelo_id_exemplar(id)
            
            if exemplar_esta_vinculado_a_emprestimo != True:
                for i in range(len(cls.consultar())):
                    if cls.lista_exemplares[i].id == id:
                        cls.lista_exemplares[i] = Exemplar(id,livro, circular, 0,  qtd- 1)
                        break
            else:
                print("Atenção, Exemplar está vinculado a Emprestimo!")
                return False
        elif exemplar.qtd == 1:
            from application.model.dao.emprestimo_dao import EmprestimoDao
            emprestimos = EmprestimoDao()
            exemplar_esta_vinculado_a_emprestimo = emprestimos.verificar_se_emprestimo_existe_pelo_id_exemplar(id)
            
            if exemplar_esta_vinculado_a_emprestimo != True:
                for i in range(len(cls.consultar())):
                    if cls.lista_exemplares[i].id == id:
                        cls.lista_exemplares[i] = Exemplar(id,livro, circular, 1,  qtd- 1)
                        break
            else:
                print("Atenção, Exemplar está vinculado a Emprestimo!")
                return False
        else:
            return False
    
    
    @classmethod
    def excluir_pelo_emprestimo(cls,id,livro, circular, qtd):
        exemplar = cls.consultar_exemplar_id_existe(id)
        if exemplar.qtd > 0:
            for i in range(len(cls.consultar())):
                if cls.lista_exemplares[i].id == id:
                    cls.lista_exemplares[i] = Exemplar(id,livro, circular, 0,  qtd- 1)
                    break
        elif exemplar.qtd == 1:
            for i in range(len(cls.consultar())):
                if cls.lista_exemplares[i].id == id:
                    cls.lista_exemplares[i] = Exemplar(id,livro, circular, 1,  qtd- 1)
                    break
        else:
            return False
    
    @classmethod
    def atualizar_livro_exemplar(cls,livro):
        i, exemplar, exemplarExiste = cls.verificar_se_exemplar_existe(livro)
        
        if exemplarExiste == True:
            cls.lista_exemplares[i] = Exemplar(exemplar.id,cls.livros.consultar_livro_id(livro), exemplar.circular, 0, exemplar.qtd)
        else:
            return None
    
    @classmethod
    def consultar(cls):
        return cls.lista_exemplares
    
    @classmethod
    def verificar_se_exemplar_existe(cls , id):
        for i, exemplar in enumerate(cls.consultar()):
            if exemplar.livro.id == id:
                return i,exemplar, True
        return False, False , False
            
    @classmethod
    def verificar_se_exemplar_circular(cls , id):
        for exemplar in cls.consultar():
            if exemplar.id == id:
                if exemplar.circular == True:
                    return True
                else:
                    return False    
    
    @classmethod
    def aumentar_quantidade(cls , id):
        for exemplar in cls.consultar():
            if exemplar.id == id:
                return exemplar.qtd + 1 
    
    @classmethod
    def consultar_exemplar_id (cls, valor):
        for exemplar in cls.lista_exemplares:
            if exemplar.id == valor:
                return exemplar
        return False

    @classmethod
    def consultar_exemplar_id_existe(cls, valor):
        for exemplar in cls.lista_exemplares:
            if exemplar.status == 0 and exemplar.livro.status == 0:
                if exemplar.id == valor and exemplar.qtd > 0:
                    return exemplar
        return False
            
    @classmethod
    def gerar_id_exemplar(cls): 
          if len(cls.consultar()) == 0:
              return 1 
          else:
              for exemplar in cls.lista_exemplares:
                  posicao = exemplar.id
              return posicao + 1    

    @classmethod
    def visualizar_se_exemplar_existe(cls):
        print("-=-=- Lista de Exemplares-=-=")
        exemplar = ExemplarDao()
        exemplares_cadastrados = 0

        for exemplares in exemplar.consultar():
            if exemplares.qtd > 0:
                if exemplares.livro.status == 0:
                    exemplares_cadastrados += 1
                    return True
           
        if exemplares_cadastrados == 0:
            return False
    
    @classmethod
    def consultar_exemplar_titulo(cls, titulo):
        for exemplares in cls.consultar():
           if exemplares.livro.titulo == titulo:
                if exemplares.qtd > 0:
                    if exemplares.livro.status == 0:
                        return exemplares       
        return False
    
    @classmethod
    def qtd_total_exemplar(cls):
        qtd_exemplar = 0
        if len(cls.consultar()) > 0:
            for exemplar in cls.consultar():
                if exemplar.status == 0:
                    qtd_exemplar += exemplar.qtd
            return qtd_exemplar