from application.model.dao.livro_dao import LivroDao

class MenuLivroView:

    @staticmethod
    def livro_nao_localizado():
        print("Livro não Localizado")

    @staticmethod
    def msg_sim_ou_nao(tipo):
        try:
            retorno = input(f"Deseja {tipo} o livro [S/N]: ")
            while retorno != "S" and retorno != "N":
                print("Atenção, valor inválido!")
                retorno = input(f"Deseja {tipo} o livro [S/N]: ")     
            return retorno
        except ValueError:
            print("Atenção, valor inválido!")

    @classmethod
    def cadastrar_livro(cls):
        try:
            print("-=-= 1 - CADASTRAR LIVRO -=-=")
            titulo = input("Digite o nome do Livro: ")
            while titulo == "" or titulo is None:
                print("Atenção, Valor Inválido!")
                titulo = input("Digite o nome do Livro: ")
            
            isbn  = input("Digite a isbn do livro: ")
            while isbn == "" or isbn is None:
                print("Atenção, Valor Inválido!")
                isbn  = input("Digite a isbn do livro: ")
                
            autores = input("Digite os autores do livro: ")
            while autores == "" or autores is None:
                print("Atenção, Valor Inválido!")
                autores = input("Digite os autores do livro: ")
                    
            edicao  = input("Digite a edição do livro: ")
            while edicao == "" or edicao is None:
                print("Atenção, Valor Inválido!")
                edicao  = input("Digite a edição do livro: ")
            
            editora = input("Digite a editora do livro: ")
            while editora == "" or editora is None:
                print("Atenção, Valor Inválido!")
                editora = input("Digite a editora do livro: ")
                
            ano = input("Digite o ano de lançançamento do livro: ")
            while ano == "" or ano is None:
                print("Atenção, Valor Inválido!")
                ano = input("Digite o ano de lançançamento do livro: ")
                
            assuntos = input("Digite os assuntos do livro: ")
            while assuntos == "" or assuntos is None:
                print("Atenção, Valor Inválido!")
                assuntos = input("Digite os assuntos do livro: ")
            
            return titulo,isbn ,autores, edicao, editora, ano, assuntos 
        
        except ValueError:
            print("Atenção, Valor Inválido!")
            
    @classmethod
    def alterar_livro(cls):
        try:
            print("-=-= 2 - ALTERAR LIVRO -=-=")
            
            titulo = input("Digite o nome do Livro: ")
            while titulo == "" or titulo is None:
                print("Atenção, Valor Inválido!")
                titulo = input("Digite o nome do Livro: ")
                        
            isbn  = input("Digite a isbn do livro: ")
            while isbn == "" or isbn is None:
                print("Atenção, Valor Inválido!")
                isbn  = input("Digite a isbn do livro: ")
                
            autores = input("Digite os autores do livro: ")
            while autores == "" or autores is None:
                print("Atenção, Valor Inválido!")
                autores = input("Digite os autores do livro: ")
                    
            edicao  = input("Digite a edição do livro: ")
            while edicao == "" or edicao is None:
                print("Atenção, Valor Inválido!")
                edicao  = input("Digite a edição do livro: ")
                        
            editora = input("Digite a editora do livro: ")
            while editora == "" or editora is None:
                print("Atenção, Valor Inválido!")
                editora = input("Digite a editora do livro: ")
                
            ano = input("Digite o ano de lançançamento do livro: ")
            while ano == "" or ano is None:
                print("Atenção, Valor Inválido!")
                ano = input("Digite o ano de lançançamento do livro:")
                
            assuntos = input("Digite os assuntos do livro: ")
            while assuntos == "" or assuntos is None:
                print("Atenção, Valor Inválido!")
                assuntos = input("Digite os assuntos do livro: ")
            
            return titulo,isbn ,autores, edicao, editora, ano, assuntos 
        
        except ValueError:
            print("Atenção, Valor Inválido!")
    
    @staticmethod
    def consultar_livro_id():
        try:
            n_livro = int(input("Digite o n° do Livro: ")) 
            return n_livro
        except ValueError:
            print("Atenção, Valor inválido!")
    
    @classmethod
    def visualizar_livros(cls):
        print("-=-=- Lista de Livros-=-=")
        livro = LivroDao()
        livros_cadastrados = 0

        for livros in livro.consultar():
            if livros.status == 0:
                print(f" N° Livro: {livros.id} | Titulo: {livros.titulo} | ISBN: {livros.isbn} | Autores: {livros.autores} | Edição: {livros.edicao} | Editora: {livros.editora} | Ano: {livros.ano} | Assunto(s): {livros.assuntos} ")
                print("-="*4)
                livros_cadastrados += 1
           
        if livros_cadastrados == 0:
            print("Não há livros!")
            print("-" *4)
    
    @staticmethod
    def msg(texto):
        print("-" *4)
        print(f"Livro {texto}!")
