from application.controller import biblioteca_controller
from application.controller import administrador_controller

class MenuView:

    @classmethod
    def inicializa(cls, usuario, data, dia):
        return cls.menu_principal(usuario,data, dia)

    
    @classmethod
    def menu_administrador(cls, usuario, data, dia):
        try:
            print(f"\n=-=-=-=- Biblioteca | Usuário: {usuario} =-=-=-=-")
            print(f"=-          {dia} - {data}          =-")
            print("=-=-=-=- Relatório Gerencial =-=-=-=-")
            print("== Selecione uma opção: ===")
            print("1 - Livro / Exemplar")
            print("2 - Empréstimos em Aberto")
            print("3 - Reservas em Aberto")
            print("4 - Usuários")
            print("5 - Emprestimos em Atraso")
            print("6 - Sair")
            
            return int(input("Digite uma opção: "))
            
        except ValueError:
            print("Atenção, Valor Inválido!")
            
            usuario_administrador = administrador_controller.AdministradorBibliotecaController()
            usuario_administrador.menu()
    
    @classmethod
    def menu_usuario(cls):
        try:
            print("=-=-= USUARIO -=-=-=")
            print("1 - Cadastrar")
            print("2 - Consultar")
            print("3 - Voltar")
            
            return int(input("Digite uma opção: "))
        
        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Usuario"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)
    
    @staticmethod
    def menu_principal(usuario, data, dia):
        try:
            print(f"\n=-=-=-=- Biblioteca | Usuário: {usuario} =-=-=-=-")
            print(f"=-          {dia} - {data}          =-")
            print("== Selecione uma opção: ===")
            print("1 - Livro")
            print("2 - Exemplar")
            print("3 - Categoria")
            print("4 - Acervo")
            print("5 - Emprestimo")
            print("6 - Reserva")
            print("7 - Gerar Relatório")
            print("8 - Usuário")
            print("9 - Sair")
            
            return int(input("Digite uma opção: "))
            
        except ValueError:
            print("Atenção, Valor Inválido!")
            
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.inicializa()
    
    @staticmethod
    def lista_menu():
        lista_menu = ["Livro", "Exemplar" , "Categoria" , "Acervo", "Emprestimo" ,"Reserva", "Relatório Gerencial" , "Usuario"]
        return lista_menu
    
    @classmethod
    def exibir_menu_except(cls,tipo):
        i = 0 
        for i,lista in enumerate(cls.lista_menu()):
            if lista == tipo:
                return i + 1
    @classmethod
    def menu_livro(cls):
        try:
            while True:
                print("--=-=- Livro --=-=-")
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Excluir")
                print("4 - Consultar")
                print("5 - Voltar")

                return int(input("Digite uma opção: "))
        
        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Livro"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)
    
    @classmethod
    def menu_exemplar(cls):
        try:
            print("--=-=- Exemplar --=-=-")
            print("1 - Cadastrar")
            print("2 - Alterar")
            print("3 - Excluir")
            print("4 - Consultar")
            print("5 - Voltar")
            return int(input("Digite uma opção: "))
        
        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Exemplar"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)

    @classmethod
    def menu_categoria(cls):
        try:
            print("=-=-= Categoria -=-=-=")
            print("1 - Cadastrar")
            print("2 - Alterar")
            print("3 - Excluir")
            print("4 - Consultar")
            print("5 - Voltar")
            
            return int(input("Digite uma opção: "))
        
        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Categoria"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)
            
    @classmethod
    def menu_emprestimo(cls):
        try:
            print("=-=-= Emprestimo -=-=-=")
            print("1 - Realizar novo Emprestimo")
            print("2 - Consultar Emprestimo")
            print("3 - Devolver Exemplar")
            print("4 - Voltar")
            
            opcao = int(input("Digite uma opção: "))
            while opcao == "" or opcao == None:
                print("Atenção, Valor Inválido!!")
                opcao = int(input("Digite uma opção: "))
            return opcao
        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Emprestimo"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)
    
    @classmethod
    def menu_reserva(cls):
        try:
            print("=-=-= Reserva -=-=-=")
            print("1 - Realizar nova Reserva")
            print("2 - Consultar Reservas")
            print("3 - Cancelar Reserva")
            print("4 - Voltar")
            
            opcao = int(input("Digite uma opção: "))
            while opcao == "" or opcao == None:
                print("Atenção, Valor Inválido!!")
                opcao = int(input("Digite uma opção: "))
            return opcao
        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Reserva"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)

    @classmethod
    def menu_acervo(cls):
        try:
            while True:
                print("-=-=-= Acervo Biblioteca -=-=-=")
                print("1 - Consultar Acervo")
                print("2 - Voltar")

                return int(input("Digite uma opção: "))

        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Acervo"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)
    
    @classmethod
    def menu_relatorio(cls):
        try:
            while True:
                print("-=-=-= Relatorio Gerencial -=-=-=")
                print("1 - Gerar Relatório")
                print("2 - Voltar")

                return int(input("Digite uma opção: "))

        except ValueError:
            print("Atenção, Valor Inválido!")
            tipo = "Relatório Gerencial"
            opcao = cls.exibir_menu_except(tipo)
            biblioteca = biblioteca_controller.BibliotecaController()
            biblioteca.menu(opcao)

    @staticmethod
    def finalizar():
        print("Encerrando Programa..")
        print("Programa Encerrado!")
        exit()
    
    @classmethod
    def opcao_invalida(cls):
        print("Atenção, Opção Inválida")