from application.view.exemplar_view import MenuExemplarView
from application.view.emprestimo_view import MenuEmprestimoView
from application.view.menu_view import MenuView
from application.model.dao.reserva_dao import ReservaDao
from application.view.reserva_view import MenuReservaView
from application.model.dao.usuario_dao import UsuarioDao
from application.view.usuario_view import UsuarioView
from application.model.dao.emprestimo_dao import EmprestimoDao
from application.controller import biblioteca_controller
from datetime import *
import time

class ReservaController:
    
    def __init__(self):
        self.modelEmprestimo = EmprestimoDao()
        self.viewExemplar = MenuExemplarView()
        self.view = MenuView()
        self.model = ReservaDao()
        self.viewEmprestimo = MenuEmprestimoView()
        self.viewReserva = MenuReservaView()
        self.viewUsuario = UsuarioView()
        self.model_usuario = UsuarioDao()
        
    def menu_reserva(self):
        while True:
            
            opcao = self.view.menu_reserva() 
            
            if opcao == 1:
                if opcao == 1:
                        exemplar_nome = self.viewExemplar.consultar_exemplar_nome()
                        retorno = self.viewEmprestimo.exibir_emprestimo_nome(exemplar_nome)
                        if retorno == False:
                            id_emprestimo = self.viewEmprestimo.selecionar_emprestimo()
                            
                            while id_emprestimo == False:
                                self.viewEmprestimo.msg_valor_invalido()
                                id_emprestimo = self.viewEmprestimo.selecionar_emprestimo()
                            
                            if id_emprestimo != False:
                                emprestimo = self.modelEmprestimo.consultar_emprestimo_pelo_id(id_emprestimo)
                                if emprestimo != False:
                                    nome = self.viewUsuario.input_nome_usuario()
                                    retorno, usuario = self.viewUsuario.exbir_usuario_nome(nome)

                                    if retorno == False:
                                        if usuario != False:
                                            retorno_msg = self.viewReserva.msg_sim_ou_nao("Cadastrar")
                                            if retorno_msg == "S":
                                                retorno = self.model.inserir_reserva(self.model.gerar_id_reserva(), usuario.id, emprestimo.id, emprestimo.data_devolucao)
                                                if retorno == True:
                                                    self.viewReserva.msg_reserva("Cadastrada")
                                else:
                                    self.viewEmprestimo.msg_nao_localizado()                    
                                
            elif opcao == 2:
                while True:
                    opcao = self.viewReserva.tipos_consulta_emprestimo()
                    
                    if opcao == 1:
                        self.viewReserva.exibir_todas_reservas()
                    elif opcao == 2:
                        data_inicial, data_final = self.viewReserva.input_intervalo_emprestimo()
                        verificar_data_inicial = self.modelEmprestimo.verificar_se_data_e_valida(data_inicial)
                        verificar_data_final = self.modelEmprestimo.verificar_se_data_e_valida(data_final)
                   
                        if verificar_data_inicial == True and verificar_data_final == True:
                           self.viewReserva.exibir_reserva_intervalo(data_inicial, data_final)
                        else:
                           print("Atenção, Data Inválida!")
                    elif opcao == 3:
                        self.menu_reserva()
                    
            elif opcao == 3:
                self.viewReserva.exibir_todas_reservas()
                retorno = self.model.visualizar_se_reserva_existe()
                if retorno != False:
                    reserva = self.viewReserva.selecionar_reserva()
                    retorno, reserva = self.model.verificar_reserva_id(reserva)
                    if retorno == True:
                        retorno_msg = self.viewReserva.msg_sim_ou_nao("Cancelar")
                        if retorno_msg == "S":
                            retorno = self.model.excluir(reserva.id , reserva.usuario.id , reserva.emprestimo.id, reserva.data_reserva)
                            if retorno == True:
                                self.viewReserva.msg_reserva("Cancelada")
                    else:
                        self.viewReserva.msg_nao_localizado()

            elif opcao == 4:
                biblioteca = biblioteca_controller.BibliotecaController()
                biblioteca.inicializa()
            else:
                self.view.opcao_invalida()   