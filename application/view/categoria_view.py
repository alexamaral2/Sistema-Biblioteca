from application.model.dao.categoria_dao import CategoriaDao

class MenuCategoriaView:

    @staticmethod
    def categoria_nao_localizada():
        print("Categoria não Localizada")
    
    @staticmethod
    def msg_sim_ou_nao(tipo):
        try:
            retorno = input(f"Deseja {tipo} a categoria [S/N]: ")
            while retorno != "S" and retorno != "N":
                print("Atenção, valor inválido!")
                retorno = input(f"Deseja {tipo} a categoria [S/N]: ")     
            return retorno
        except ValueError:
            print("Atenção, valor inválido!")

    @classmethod
    def cadastrar_categoria(cls):
        try:
            print("-=-= 1 - CADASTRAR CATEGORIA -=-=")
            nome = input("Digite o nome da Categoria: ")
            while nome == "" or nome is None:
                print("Atenção, Valor Inválido!")
                nome = input("Digite o nome da Categoria: ")
            
            descricao  = input("Digite a descrição da Categoria: ")
            while descricao == "" or descricao is None:
                print("Atenção, Valor Inválido!")
                descricao  = input("Digite a descrição da Categoria: ")
            
            assunto = input("Digite o assunto da Categoria: ")
            while assunto == "" or assunto is None:
                print("Atenção, Valor Inválido!")
                assunto = input("Digite o assunto da Categoria: ")
                
            return nome,descricao,assunto 
        
        except ValueError:
            print("Atenção, Valor Inválido!")
            
    @classmethod
    def alterar_categoria(cls):
        try:
            print("-=-= 2 - ALTERAR CATEGORIA -=-=")
            nome = input("Digite o nome da Categoria: ")
            while nome == "" or nome is None:
                print("Atenção, Valor Inválido!")
                nome = input("Digite o nome da Categoria: ")
                        
            descricao  = input("Digite a descrição da Categoria: ")
            while descricao == "" or descricao is None:
                print("Atenção, Valor Inválido!")
                descricao  = input("Digite a descrição da Categoria: ")
                        
            assunto = input("Digite o assunto da Categoria: ")
            while assunto == "" or assunto is None:
                print("Atenção, Valor Inválido!")
                assunto = input("Digite o assunto da Categoria: ")
            
            return nome, descricao, assunto 
        
        except ValueError:
            print("Atenção, Valor Inválido!")
    
    @staticmethod
    def consultar_categoria_id():
        try:
            n_categoria = int(input("Digite o n° da categoria: "))
            return n_categoria
        except ValueError:
            print("Antenção, Valor Inválido!")
    
    @classmethod
    def visualizar_categorias(cls):
        print("-=-=- Lista de Categorias-=-=")
        categoria = CategoriaDao()
        categorias_cadastradas = 0

        for categorias in categoria.consultar():
            if categorias.status == 0:
                print(f" N° Categoria: {categorias.id} | Titulo: {categorias.nome} | Descrição: {categorias.descricao} | Assunto: {categorias.assunto}")
                print("-=" *4)
                categorias_cadastradas += 1
                
        if categorias_cadastradas == 0:
            print("Não há categorias!")
            print("-=" *4)
    
    @staticmethod
    def msg(texto):
        print("-" *4)
        print(f"Categoria {texto}!")
