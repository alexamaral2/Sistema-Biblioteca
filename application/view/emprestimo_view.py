from application.model.dao.emprestimo_dao import EmprestimoDao
from datetime import *
import time

class MenuEmprestimoView:    
    @staticmethod
    def msg_data_devolucao_menor_atual():
        print("Atenção, A data de devolução não pode ser menor que a data atual..!!")
    
    @staticmethod
    def msg_valor_invalido():
        print("Valor Inválido!")
    
    @staticmethod
    def msg_nao_localizado():
        print("Emprestimo não localizado!")
    
    @staticmethod
    def msg_valor_invalido():
        print("Atenção, Valor Inválido!")
   
    @staticmethod
    def data_devolucao():
        try:
            data = input("Digite a data de devolução (formato: dd/mm/aaaa): ")
            while data == "" or data == None:
                print("Valor inválido!")
                data = input("Digite a data de devolução (formato: dd/mm/aaaa): ")
            return data
        except ValueError:
            print("Atenção, valor inválido!")
    @staticmethod
    def menu_emprestar():
        try:
            print("=-=-=-=- Emprestar -=-=-=-=")
            print("1- Emprestar Exemplar")
            print("2- Exibir Usuários")
            print("3- Exibir Exemplares")
            print("4- Voltar")

            opcao = int(input("Digite uma opção: "))
            while opcao == "" or opcao == None:
                print("Atenção, Valor Inválido!")
                opcao = int(input("Digite uma opção: "))
            return opcao
        except ValueError:
            return False
            
    @staticmethod
    def emprestar_input():
        usuario = input("Digite o nome do usuário: ")
        while usuario == "" or usuario == None:
            usuario = input("Digite o nome do usuário: ")
        
        while exemplar == "" or exemplar == None:
            exemplar = input("Digite o nome do Exemplar: ")
        
        return usuario, exemplar
    
    
    @staticmethod
    def msg_emprestimo(valor):
        if valor == "Devolvido":
            print(f"Exemplar {valor}!")
        else:
            print(f"Emprestimo {valor}!")
    
    @staticmethod
    def msg_sim_ou_nao(tipo):
        try:
            retorno = input(f"Deseja {tipo} o emprestimo [S/N]: ")
            while retorno != "S" and retorno != "N":
                print("Atenção, valor inválido!")
                retorno = input(f"Deseja {tipo} o emprestimo [S/N]: ")     
            return retorno
        except ValueError:
            print("Atenção, valor inválido!")
    
    @staticmethod
    def tipos_consulta_emprestimo():
        try:
            print("=-=-=-=- Consultar Emprestimo =-=-=-=-")
            print("1 - Exibir Todos Emprestimos Ativos")
            print("2 - Exibir por Intervalo")
            print("3 - Voltar")
            opcao = int(input("Digite uma opção: "))
            
            return opcao
        except ValueError:
            print("Atenção, Valor Inválido!")
    
    @staticmethod
    def selecionar_emprestimo():
        try:
            n_emprestimo = int(input("Digite o n° do emprestimo: ")) 
            while n_emprestimo == "" or n_emprestimo == None:  
                print("Atenção, valor inválido!")
                n_emprestimo = int(input("Digite o n° do emprestimo: ")) 
            return n_emprestimo
        
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
    def exibir_emprestimo_nome(nome_exemplar):
        emprestimos = EmprestimoDao()
        qtd_emprestimo = 0
        msg = True
        
        for emprestimo in emprestimos.exibir_todos_emprestimos():
            if emprestimo.status == 0:
                if emprestimo.exemplar.livro.titulo == nome_exemplar:
                   if emprestimo.exemplar.circular == True: 
                        if emprestimo.status_devolucao == False:
                             print(f"N° Emprestimo : {emprestimo.id} | Nome Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.exemplar.livro.titulo} | Data Emprestimo: {emprestimo.data_emprestimo} | Data Devolução: {emprestimo.data_devolucao} | Devolvido: Não")
                             print("=-=-=-=-")
                             msg = False
            
        if msg == True:
            print("Não há emprestimos para esse exemplar!")
        
        return msg
            
    
    @staticmethod
    def exibir_emprestimo_intervalo(data_inicial, data_final):
        date_data_inicial = time.strptime(data_inicial, "%d/%m/%Y")
        date_data_final = time.strptime(data_final, "%d/%m/%Y")
        
        emprestimo = EmprestimoDao()
        qtd_emprestimo = 0
        
        print("=-=-=-=- Lista de Emprestimos =-=-=-=-")
        for emprestimo in emprestimo.exibir_todos_emprestimos():
            if time.strptime(emprestimo.data_emprestimo, "%d/%m/%Y") >= date_data_inicial and time.strptime(emprestimo.data_emprestimo, "%d/%m/%Y") <= date_data_final:
                if emprestimo.status_devolucao == False:
                    print(f"N° Emprestimo : {emprestimo.id} | Nome Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.exemplar.livro.titulo} | Data Emprestimo: {emprestimo.data_emprestimo} | Data Devolução: {emprestimo.data_devolucao} | Cancelado: {emprestimo.status_cancelado} | Devolvido: Não")
                    print("=-=-=-=-")
                    qtd_emprestimo += 1
                else:
                    print(f"N° Emprestimo : {emprestimo.id} | Nome Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.exemplar.livro.titulo} | Data Emprestimo: {emprestimo.data_emprestimo} | Data Devolução: {emprestimo.data_devolucao} | Cancelado: {emprestimo.status_cancelado} | Devolvido: Sim")
                    print("=-=-=-=-")
                    qtd_emprestimo += 1
    
        if qtd_emprestimo == 0:
            print("Atenção, Não houve emprestimos no periodo especificado!")
                
    
    @staticmethod
    def exibir_todos_emprestimos():
        emprestimos = EmprestimoDao()
        qtd_emprestimo = 0
        
        print("=-=-=-=- Lista de Emprestimos =-=-=-=-")
        for emprestimo in emprestimos.exibir_todos_emprestimos():
         if emprestimo.status == 0:
            if emprestimo.status_devolucao == False:
                print(f"N° Emprestimo : {emprestimo.id} | Nome Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.exemplar.livro.titulo} | Data Emprestimo: {emprestimo.data_emprestimo} | Data Devolução: {emprestimo.data_devolucao} | Devolvido: Não")
                print("=-=-=-=-")
                qtd_emprestimo += 1
            else:
                print(f"N° Emprestimo : {emprestimo.id} | Nome Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.exemplar.livro.titulo} | Data Emprestimo: {emprestimo.data_emprestimo} | Data Devolução: {emprestimo.data_devolucao} | Devolvido: Sim")
                print("=-=-=-=-")
                qtd_emprestimo += 1
        
        if qtd_emprestimo == 0:
            print("Atenção, Não há Emprestimos!!")
    
    @staticmethod
    def exibir_todos_emprestimos_atrasados():
        emprestimos = EmprestimoDao()
        qtd_emprestimo = 0
        data_atual = str(date.today().strftime("%d/%m/%Y"))
        
        print("=-=-=-=- Lista de Emprestimos em Atraso =-=-=-=-")
        for emprestimo in emprestimos.exibir_todos_emprestimos():
            if emprestimo.status == 0:
               if emprestimo.status_devolucao == False:
                   if time.strptime(data_atual, "%d/%m/%Y") > time.strptime(emprestimo.data_devolucao, "%d/%m/%Y"):
                        print(f"N° Emprestimo : {emprestimo.id} | Nome Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.exemplar.livro.titulo} | Data Emprestimo: {emprestimo.data_emprestimo} | Data Devolução: {emprestimo.data_devolucao} | Devolvido: Não | *Em Atraso")
                        print("=-=-=-=-")
                        qtd_emprestimo += 1

        if qtd_emprestimo == 0:
            print("Atenção, Não há Emprestimos Atrasados!!")