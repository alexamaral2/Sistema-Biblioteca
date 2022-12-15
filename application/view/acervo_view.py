from application.model.dao.livro_dao import LivroDao
from application.model.dao.acervo_dao import AcervoDao

class MenuAcervoView:

    @staticmethod
    def acervo_nao_localizado():
        print("Livro não Localizado")
    
    @staticmethod
    def consultar_acervo():
        try:
            print("-=-= 4- Acervo -=-=")
            pesquisa = input("Digite a Categoria/Nome do Livro que deseja: ")
            while pesquisa == "" or pesquisa is None:
                print("Atenção, Valor Inválido!")
                pesquisa = input("Digite a Categoria/Nome do Livro que deseja: ")
            return pesquisa
        except:
            print("Valor inválido!")
    
    @classmethod
    def visualizar_acervo(cls , valor):
        print("-=-=- Lista de Acervo(s)-=-=")
        lista_acervo = AcervoDao()
        lista_acervo.consultar_acervo(valor)      

        print("-=" *4)

    
    @staticmethod
    def msg(texto):
        print("-" *4)
        print(f"Livro {texto}!")