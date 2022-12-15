from application.view.menu_view import MenuView
from application.controller import biblioteca_controller
from application.view.relatorio_gerencial_view import MenuRelatorioGerencial
from application.view.emprestimo_view import MenuEmprestimoView
from application.model.dao.emprestimo_dao import EmprestimoDao
from application.model.dao.relatorio_gerencial_dao import RelatorioGerencialDao

class RelatorioGerencialController:
    
    def __init__(self):
        self.view = MenuView()
        self.emprestimo_view = MenuEmprestimoView()
        self.model = RelatorioGerencialDao()
        self.view_menu_gerencial = MenuRelatorioGerencial()
        self.model_emprestimo = EmprestimoDao()
        
    def menu_relatorio(self):
        while True:
            
            opcao = self.view.menu_relatorio()
            if opcao == 1:
                data_inicial, data_final = self.emprestimo_view.input_intervalo_emprestimo()
                verificar_data_inicial = self.model_emprestimo.verificar_se_data_e_valida(data_inicial)
                verificar_data_final = self.model_emprestimo.verificar_se_data_e_valida(data_final)
                    
                if verificar_data_inicial == True and verificar_data_final == True:
                    dic_emprestimo = self.model.gerar_relatorio_gerencial_por_periodo_emprestimo(data_inicial, data_final)
                    dic_reserva = self.model.gerar_relatorio_gerencial_por_periodo_reserva(data_inicial, data_final)
                    lista = self.model.lista_qtd_emprestimos(dic_emprestimo, dic_reserva)
                    
                    if lista != False:
                        lista = self.model.bubbleSort(lista)
                        self.view_menu_gerencial.exibir_relatorio_gerencial(lista)
                    else:
                        self.view_menu_gerencial.msg_retorno_consulta()
                        
                
            elif opcao == 2:
                biblioteca = biblioteca_controller.BibliotecaController()
                biblioteca.inicializa()
            else:
                self.view.opcao_invalida()   