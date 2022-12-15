from application.view.menu_view import MenuView
from application.view.emprestimo_view import MenuEmprestimoView
from application.controller import biblioteca_controller
from application.model.dao.emprestimo_dao import EmprestimoDao
from application.view.exemplar_view import MenuExemplarView
from application.view.usuario_view import UsuarioView
from application.model.dao.usuario_dao import UsuarioDao
from datetime import *
import time

class EmprestimoController:
    
    def __init__(self):
        
        self.view = MenuView()
        self.viewEmprestimo = MenuEmprestimoView()
        self.model = EmprestimoDao()
        self.viewExemplar = MenuExemplarView()
        self.viewUsuario = UsuarioView()
        self.model_usuario = UsuarioDao()
        
    def menu_emprestimo(self):
        while True:
            
            opcao = self.view.menu_emprestimo()  
            
            if opcao == 1:
                while True:
                    opcao = self.viewEmprestimo.menu_emprestar()

                    if opcao == 1:
                        exemplar_nome = self.viewExemplar.consultar_exemplar_nome()
                        retorno,exemplar = self.viewExemplar.visualizar_exemplar_pelo_titulo(exemplar_nome)
                        if retorno == False:
                            nome = self.viewUsuario.input_nome_usuario()
                            retorno, usuario = self.viewUsuario.exbir_usuario_nome(nome)
                            
                            if retorno == False:
                                if usuario != False:
                                    retorno_msg = self.viewEmprestimo.msg_sim_ou_nao("Cadastrar")
                                    if retorno_msg == "S":
                                        retorno = self.model.emprestar(self.model.gerar_id_emprestimo(), usuario.id, exemplar.id)
                                        if retorno == True:
                                            self.viewEmprestimo.msg_emprestimo("Cadastrado")
                    elif opcao == 2:
                        self.viewUsuario.exbir_usuarios()
                    elif opcao == 3:
                        self.viewExemplar.visualizar_exemplares()
                    elif opcao == 4:
                        self.menu_emprestimo()
                    elif opcao == False:
                        self.viewEmprestimo.msg_valor_invalido()
                    else:
                        self.view.opcao_invalida()               
            elif opcao == 2:
              while True:
                opcao = self.viewEmprestimo.tipos_consulta_emprestimo()
                if opcao == 1:
                     self.viewEmprestimo.exibir_todos_emprestimos()
                elif opcao == 2:
                    data_inicial, data_final = self.viewEmprestimo.input_intervalo_emprestimo()
                    verificar_data_inicial = self.model.verificar_se_data_e_valida(data_inicial)
                    verificar_data_final = self.model.verificar_se_data_e_valida(data_final)
                    
                    if verificar_data_inicial == True and verificar_data_final == True:
                        self.viewEmprestimo.exibir_emprestimo_intervalo(data_inicial,data_final)
                    else:
                        print("Atenção, Data Inválida!")
                elif opcao == 3:
                     self.menu_emprestimo()
                else:
                    self.view.opcao_invalida()
            elif opcao == 3:
                self.viewEmprestimo.exibir_todos_emprestimos()
                retorno = self.model.visualizar_se_emprestimo_existe()
                if retorno != False:
                    id_emprestimo = self.viewEmprestimo.selecionar_emprestimo()
                    while id_emprestimo == False:
                        print("Atenção, Valor inválido!")
                        id_emprestimo = self.viewEmprestimo.selecionar_emprestimo()
                    status, emprestimo = self.model.verificar_emprestimo_id(id_emprestimo)
                    
                    if status != False:
                       verificar_atraso = self.model.verficar_se_devolucao_esta_atrasada(emprestimo.id)
                       if verificar_atraso != True:
                            retorno_msg = self.viewEmprestimo.msg_sim_ou_nao("Devolver")
                            if retorno_msg == "S":
                                retorno = self.model.cancelar_emprestimo(emprestimo.id, emprestimo.usuario.id, emprestimo.exemplar.id, emprestimo.data_emprestimo, emprestimo.data_devolucao)
                            if retorno == True:
                                self.viewEmprestimo.msg_emprestimo("Devolvido")
                       else:
                            data_devolucao = self.viewEmprestimo.data_devolucao()
                            while time.strptime(data_devolucao, "%d/%m/%Y") < time.strptime(str(date.today().strftime("%d/%m/%Y")), "%d/%m/%Y"):
                                self.viewEmprestimo.msg_data_devolucao_menor_atual()
                                data_devolucao = self.viewEmprestimo.data_devolucao()

                            retorno = self.model.verificar_se_data_e_valida(data_devolucao)
                            while retorno == False:
                                print("Atenção, Data Inválida!")
                                data_devolucao = self.viewEmprestimo.data_devolucao()
                                retorno = self.model.verificar_se_data_e_valida(data_devolucao)
                                
                            retorno_msg = self.viewEmprestimo.msg_sim_ou_nao("Devolver")
                            if retorno_msg == "S":
                                retorno = self.model.cancelar_emprestimo(emprestimo.id, emprestimo.usuario.id, emprestimo.exemplar.id, emprestimo.data_emprestimo, data_devolucao)
                                if retorno == True:
                                    self.viewEmprestimo.msg_emprestimo("Devolvido")
                    else:
                        self.viewEmprestimo.msg_nao_localizado()

            elif opcao == 4:
                biblioteca = biblioteca_controller.BibliotecaController()
                biblioteca.inicializa()
            else:
                self.view.opcao_invalida()   