from application.model.dao.exemplar_dao import ExemplarDao
from application.model.dao.livro_dao import LivroDao
from application.model.entity.livro import Exemplar

class MenuExemplarView:

    @staticmethod
    def exemplar_nao_localizado():
        print("Exemplar não Localizado")
    
    @staticmethod
    def msg_sim_ou_nao(tipo):
        try:
            retorno = input(f"Deseja {tipo} o exemplar [S/N]: ")
            while retorno != "S" and retorno != "N":
                print("Atenção, valor inválido!")
                retorno = input(f"Deseja {tipo} o exemplar [S/N]: ")     
            return retorno
        except ValueError:
            print("Atenção, valor inválido!")
    
    @classmethod
    def cadastrar_exemplar(cls):
        try:
            print("-=-= 2 - CADASTRAR EXEMPLAR -=-=")
            exemplar = int(input("Digite o n° do livro: "))

            return exemplar
        
        except ValueError:
            print("Atenção, Valor Inválido!")
    
    @classmethod
    def alterar_exemplar(cls):
        try:
            print("-=-= 2 - ALTERAR EXEMPLAR -=-=")
            print("O Exemplar é Circular: ")
            print("1- Sim")
            print("2- Não")
            
            circular = int(input("Digite a opção: "))
            while circular < 1 or circular > 2:
                print("Atenção, Opção Inválida!")
                circular = int(input("Digite a opção: "))
            if circular == 1:
                circular = True
            elif circular == 2:
                circular = False

            return circular
        
        except ValueError:
            print("Atenção, Valor Inválido!")
            return "0"
   
    @staticmethod
    def consultar_exemplar_nome():
        try:
            exemplar = input("Digite o nome do exemplar: ")
            while exemplar == "" or exemplar == None:
                print("Atenção, valor inválido!")
                exemplar = input("Digite o nome do exemplar: ")
            return exemplar
        except ValueError:
            print("Valor Inválido")
    
    @staticmethod
    def qtd_exemplar_total():
        exemplares = ExemplarDao()
        
        qtd = exemplares.qtd_total_exemplar()
        print("\n----")
        print(f"* Quantidade Total de Exemplares: {qtd}")
    
    @staticmethod
    def consultar_exemplar_id():
        try:
            exemplar = int(input("Digite o n° do exemplar: "))
            return exemplar
        except ValueError:
            print("Valor Inválido")
    
    @staticmethod
    def visualizar_exemplar_pelo_titulo(titulo):
        exemplar = ExemplarDao()
        exemplares = exemplar.consultar_exemplar_titulo(titulo)
        print("-=-=- Lista de Exemplares-=-=")
        if exemplares != False:
            if exemplares.status == True:
                 print(f" N° Exemplar: {exemplares.id} | Titulo: {exemplares.livro.titulo} | ISBN: {exemplares.livro.isbn} | Autores: {exemplares.livro.autores} | Edição: {exemplares.livro.edicao} | Editora: {exemplares.livro.editora} | Ano: {exemplares.livro.ano} | Assunto(s): {exemplares.livro.assuntos} | Qtd: {exemplares.qtd} | Circular = Sim")
                 msg = False
                 exemplares_final = exemplares
            
            elif exemplares.status == False:
                print(f" N° Exemplar: {exemplares.id} | Titulo: {exemplares.livro.titulo} | ISBN: {exemplares.livro.isbn} | Autores: {exemplares.livro.autores} | Edição: {exemplares.livro.edicao} | Editora: {exemplares.livro.editora} | Ano: {exemplares.livro.ano} | Assunto(s): {exemplares.livro.assuntos} | Qtd: {exemplares.qtd} | Circular = Sim")
                msg = False
                exemplares_final = exemplares
        else:
            print("Atenção, Não há o exemplar desejado!")
            msg = True
            exemplares_final = False
        
        return msg,exemplares_final
    
    @classmethod
    def visualizar_exemplares(cls):
        print("-=-=- Lista de Exemplares-=-=")
        exemplar = ExemplarDao()
        exemplares_cadastrados = 0

        for exemplares in exemplar.consultar():
            if exemplares.qtd > 0:
                if exemplares.livro.status == 0:
                    if exemplares.circular == True:
                        print(f" N° Exemplar: {exemplares.id} | Titulo: {exemplares.livro.titulo} | ISBN: {exemplares.livro.isbn} | Autores: {exemplares.livro.autores} | Edição: {exemplares.livro.edicao} | Editora: {exemplares.livro.editora} | Ano: {exemplares.livro.ano} | Assunto(s): {exemplares.livro.assuntos} | Qtd: {exemplares.qtd} | Circular = Sim")
                        print("-=" *4)
                    elif exemplares.circular == False:
                        print(f" N° Exemplar: {exemplares.id} | Titulo: {exemplares.livro.titulo} | ISBN: {exemplares.livro.isbn} | Autores: {exemplares.livro.autores} | Edição: {exemplares.livro.edicao} | Editora: {exemplares.livro.editora} | Ano: {exemplares.livro.ano} | Assunto(s): {exemplares.livro.assuntos} | Qtd: {exemplares.qtd} | Circular = Não")
                        print("-=" *4)
                    exemplares_cadastrados += 1             
           
        if exemplares_cadastrados == 0:
            print("Não há exemplares!")
            print("-=" *4)
    
    @staticmethod
    def msg(texto):
        print("-" *4)
        print(f"Exemplar {texto}!")
