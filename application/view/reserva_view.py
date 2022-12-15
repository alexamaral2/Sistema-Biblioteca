from application.model.dao.reserva_dao import ReservaDao
from datetime import *
import time

class MenuReservaView:    
   
    @staticmethod
    def msg_nao_localizado():
        print("Reserva não localizada!")
    
    @staticmethod
    def msg_valor_invalido():
        print("Atenção, Valor Inválido!")

    @staticmethod
    def consultar_reserva():
        try:
            print("=-=-=-=- Reserva -=-=-=-=")
            print("1- Reservar Exemplar")
            print("2- Exibir Usuários")
            print("3- Exibir Emprestimos")
            print("4- Voltar")

            opcao = int(input("Digite uma opção: "))
            while opcao == "" or opcao == None:
                print("Atenção, Valor Inválido!")
                opcao = int(input("Digite uma opção: "))
            return opcao
        except ValueError:
            return False
    
    @staticmethod
    def msg_reserva(valor):
        print(f"Reserva {valor}!")
    
    @staticmethod
    def msg_sim_ou_nao(tipo):
        try:
            retorno = input(f"Deseja {tipo} a reserva [S/N]: ")
            while retorno != "S" and retorno != "N":
                print("Atenção, valor inválido!")
                retorno = input(f"Deseja {tipo} a reserva [S/N]: ")     
            return retorno
        except ValueError:
            print("Atenção, valor inválido!")
    
    @staticmethod
    def tipos_consulta_emprestimo():
        try:
            print("=-=-=-=- Consultar Reserva =-=-=-=-")
            print("1 - Exibir Todas Reservas Ativas")
            print("2 - Exibir por Intervalo")
            print("3 - Voltar")
            opcao = int(input("Digite uma opção: "))
            
            return opcao
        except ValueError:
            print("Atenção, Valor Inválido!")
    
    @staticmethod
    def selecionar_reserva():
        try:
            n_reserva = int(input("Digite o n° da Reserva: ")) 
            while n_reserva == "" or n_reserva == None:  
                print("Atenção, valor inválido!")
                n_reserva = int(input("Digite o n° da Reserva: ")) 
            return n_reserva
        
        except ValueError: 
            return False
            
    @staticmethod
    def input_intervalo_emprestimo():
        data_inicial = input("Digite a data inicial (dd/mm/aaaa): ")
        while data_inicial == "" or data_inicial == None:
            print("Atenção, Data Inválida!")
            data_inicial = input("Digite a data inicial: ")
        
        data_final = input("Digite a data final (dd/mm/aaaa): ")
        while data_final == "" or data_final == None:
            print("Atenção, Data Inválida!")
            data_final = input("Digite a data final (dd/mm/aaaa): ")
        return data_inicial, data_final
        
    @staticmethod
    def exibir_reserva_intervalo(data_inicial, data_final):
        date_data_inicial = time.strptime(data_inicial, "%d/%m/%Y")
        date_data_final = time.strptime(data_final, "%d/%m/%Y")
        
        reservas = ReservaDao()
        qtd_reserva = 0
        
        print("=-=-=-=- Lista de Reservas =-=-=-=-")
        for reserva in reservas.exibir_todas_as_reservas():
            if time.strptime(reserva.data_reserva , "%d/%m/%Y") >= date_data_inicial and time.strptime(reserva.data_reserva, "%d/%m/%Y") <= date_data_final:
               if reserva.status == 1: 
                    if reserva.tipo_usuario_cancelamento_reserva == "Usuario":
                        print(f"N° Reserva : {reserva.id} | Nome Usuário: {reserva.usuario.nome} | Livro: {reserva.emprestimo.exemplar.livro.titulo} | Data Reserva: {reserva.data_reserva} | Cancelado: Sim | Responsável Cancelamento: Usuário")
                        print("=-=-=-=-")
                        qtd_reserva += 1
                       
                    elif reserva.tipo_usuario_cancelamento_reserva == "Sistema":
                        print(f"N° Reserva : {reserva.id} | Nome Usuário: {reserva.usuario.nome} | Livro: {reserva.emprestimo.exemplar.livro.titulo} | Data Reserva: {reserva.data_reserva} | Cancelado: Sim | Responsável Cancelamento: Sistema")
                        print("=-=-=-=-")
                        qtd_reserva += 1
                    
                    elif reserva.status_emprestimo == True:
                        print(f"N° Reserva : {reserva.id} | Nome Usuário: {reserva.usuario.nome} | Livro: {reserva.emprestimo.exemplar.livro.titulo} | Data Reserva: {reserva.data_reserva} | Emprestimo Efetuado: Sim")
                        print("=-=-=-=-")
                        qtd_reserva += 1
               else:
                    print(f"N° Reserva : {reserva.id} | Nome Usuário: {reserva.usuario.nome} | Livro: {reserva.emprestimo.exemplar.livro.titulo} | Data Reserva: {reserva.data_reserva} | Cancelado: Não")
                    print("=-=-=-=-")
                    qtd_reserva += 1
    
        if qtd_reserva == 0:
            print("Atenção, Não houve reservas no periodo especificado!")
                
    
    @staticmethod
    def exibir_todas_reservas():
        reservas = ReservaDao()
        qtd_reserva = 0
        
        print("=-=-=-=- Lista de Reserva =-=-=-=-")
        for reserva in reservas.exibir_todas_as_reservas():
            if reserva.status == 0:
                print(f"N° Reserva : {reserva.id} | Nome Usuário: {reserva.usuario.nome} | Livro: {reserva.emprestimo.exemplar.livro.titulo} | Data Reserva: {reserva.data_reserva}")
                qtd_reserva += 1
                
        if qtd_reserva == 0:
            print("Atenção, Não há Reservas!!")