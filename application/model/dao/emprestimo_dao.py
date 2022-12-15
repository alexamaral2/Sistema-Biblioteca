from application.model.entity.emprestimo import Emprestimo
from application.model.dao.usuario_dao import UsuarioDao
from application.model.dao.exemplar_dao import ExemplarDao
from datetime import *
import time


class EmprestimoDao:
    exemplar = ExemplarDao()
    usuario = UsuarioDao()
    
    lista_emprestimo = [
        
        Emprestimo(1, usuario.exibir_usuario_id(1), exemplar.consultar_exemplar_id(1) ,"27/05/2022" , "07/06/2022", False,"Não","", 0)
    ]

    @classmethod
    def exibir_todos_emprestimos(cls):
        return cls.lista_emprestimo
    
    
    @classmethod
    def emprestar(cls, id , id_usuario , id_exemplar):
        verificar_pendencia = cls.verficar_se_usuario_tem_pendencia(id_usuario)
        verificar_tipo_usuario = cls.usuario.verificar_tipo_usuario(id_usuario)
        verificar_status_usuario_suspenso = cls.usuario.verificar_status_suspenso(id_usuario)
        qtd_exemplares_por_periodo = 2
         
        if verificar_status_usuario_suspenso != True:
            if verificar_tipo_usuario == True:
                if verificar_pendencia != True:

                    qtd_emprestimos_aluno_funcionario = 3
                    qtd_emprestimos = cls.verificar_qtd_emprestimos_usuario(id_usuario)

                    if qtd_emprestimos >= 0 and qtd_emprestimos < qtd_emprestimos_aluno_funcionario:
                        verificar_se_usuario_esta_com_exemplar = cls.verificar_se_usuario_esta_com_exemplar_de_mesmo_titulo(id_exemplar,id_usuario)
                        if verificar_se_usuario_esta_com_exemplar != True:
                            data_emprestimo = str(date.today().strftime("%d/%m/%Y"))
                            data_devolucao = cls.calcular_data_devolucao(id_exemplar,id_usuario)
                            
                            qtd_exemplares_emprestado_na_data = cls.consultar_qtd_exemplar_emprestado_pelo_titulo_na_data_desejada(data_devolucao, id_exemplar)
                            if qtd_exemplares_emprestado_na_data < qtd_exemplares_por_periodo:
                                cls.lista_emprestimo.append(Emprestimo(id,cls.usuario.exibir_usuario_id(id_usuario), cls.exemplar.consultar_exemplar_id(id_exemplar) ,data_emprestimo,data_devolucao,False,"Não","",0))

                                from application.model.dao.exemplar_dao import ExemplarDao
                                exemplares = ExemplarDao()
                                exemplar = exemplares.consultar_exemplar_id(id_exemplar)
                                exemplares.excluir_pelo_emprestimo(exemplar.id , exemplar.livro , exemplar.circular, exemplar.qtd)

                                return True
                            
                            else:
                                print("Só podem ser emprestado 2 exemplares por período!")
                        else:
                            print("Atenção, O Exemplar está emprestado ao Usuário!")
                    else:
                        print(f"Atenção, O usuário excedeu o limite de {qtd_emprestimos_aluno_funcionario} emprestimos!")
                else:
                    print("Atenção, O Usuário está com pedência(s) na Biblioteca!")
            elif verificar_tipo_usuario == False:
                if verificar_pendencia != True:
                
                    qtd_emprestimos_professor = 5
                    qtd_emprestimos = cls.verificar_qtd_emprestimos_usuario(id_usuario)

                    if qtd_emprestimos >= 0 and qtd_emprestimos < qtd_emprestimos_professor:
                        verificar_se_usuario_esta_com_exemplar = cls.verificar_se_usuario_esta_com_exemplar_de_mesmo_titulo(id_exemplar, id_usuario)
                        if verificar_se_usuario_esta_com_exemplar != True:
                            data_emprestimo = str(date.today().strftime("%d/%m/%Y"))
                            data_devolucao = cls.calcular_data_devolucao(id_exemplar,id_usuario)

                            qtd_exemplares_emprestado_na_data = cls.consultar_qtd_exemplar_emprestado_pelo_titulo_na_data_desejada(data_devolucao, id_exemplar)
                            if qtd_exemplares_emprestado_na_data < qtd_exemplares_por_periodo:
                                cls.lista_emprestimo.append(Emprestimo(id,cls.usuario.exibir_usuario_id(id_usuario), cls.exemplar.consultar_exemplar_id(id_exemplar) ,data_emprestimo,data_devolucao,False,"Não","", 0))

                                from application.model.dao.exemplar_dao import ExemplarDao
                                exemplares = ExemplarDao()
                                exemplar = exemplares.consultar_exemplar_id(id_exemplar)
                                exemplares.excluir(exemplar.id , exemplar.livro , exemplar.circular, exemplar.qtd)

                                return True
                            else:
                                print("Só podem ser emprestado 2 exemplares por período!")
                        else:
                            print("Atenção, O Exemplar está emprestado ao Usuário!")
                    else:
                        print(f"Atenção, O usuário excedeu o limite de {qtd_emprestimos_professor} emprestimos!")
                else:
                    print("Atenção, O Usuário está com pedência(s) na Biblioteca!")
            else:
                print("Atenção, Emprestimos permitidos para Aluno, Funcionário e Professor!")
        else:
            print("Atenção, Usuário está suspenso de pegar livros!")

    
    @classmethod
    def cancelar_emprestimo(cls, id, usuario, exemplar, data_emprestimo, data_devolucao):
        verificar_pendencia = cls.verficar_se_usuario_tem_pendencia(usuario)
        if verificar_pendencia == False:
            for i in range(len(cls.exibir_todos_emprestimos())):
                if cls.lista_emprestimo[i].id == id:
                    cls.lista_emprestimo[i] = Emprestimo(id, cls.usuario.exibir_usuario_id(usuario), cls.exemplar.consultar_exemplar_id(exemplar), data_emprestimo, data_devolucao, True,"Não",False, 1)
                    
                    from application.model.dao.exemplar_dao import ExemplarDao
                    exemplares = ExemplarDao()
                    exemplar = exemplares.consultar_exemplar_id(exemplar)
            
                    exemplares.inserir(exemplar.id, exemplar.livro.id , exemplar.circular, 1)
                    return True
        
        elif verificar_pendencia == True:
            
            for i in range(len(cls.exibir_todos_emprestimos())):
                if cls.lista_emprestimo[i].id == id:
                    cls.lista_emprestimo[i] = Emprestimo(id, cls.usuario.exibir_usuario_id(usuario), cls.exemplar.consultar_exemplar_id(exemplar), data_emprestimo, data_devolucao, True,"Não", True,1)
                    
                    from application.model.dao.usuario_dao import UsuarioDao
                    usuario_atualiza = UsuarioDao()
                    usuario_atualiza.atualizar_usuario(usuario, True)
                    
                    from application.model.dao.exemplar_dao import ExemplarDao
                    exemplares = ExemplarDao()
                    exemplar = exemplares.consultar_exemplar_id(exemplar)
                    exemplares.inserir(exemplar.id, exemplar.livro.id, exemplar.circular, 1)
                    
                    print("Emprestimo devolvido com atraso, Usuário suspenso por 30 dias!")
                    return False
            
    @classmethod
    def atualiza_emprestimo(cls ,id_exemplar):
        for i, emprestimo in enumerate(cls.exibir_todos_emprestimos()):
            if emprestimo.exemplar.id == id_exemplar:
                cls.lista_emprestimo[i] = Emprestimo(emprestimo.id, emprestimo.usuario, cls.exemplar.consultar_exemplar_id(id_exemplar), emprestimo.data_emprestimo, emprestimo.data_devolucao, emprestimo.status_devolucao,emprestimo.status_cancelado, emprestimo.status)
        
    @classmethod
    def verificar_qtd_emprestimos_usuario(cls, id_usuario):
        qtd_emprestimos = 0
        
        for emprestimo in cls.lista_emprestimo:
            if emprestimo.usuario.id == id_usuario:
                if emprestimo.status_devolucao == False:
                    qtd_emprestimos += 1
        
        return qtd_emprestimos 
    
    @classmethod
    def calcular_data_devolucao(cls, id_exemplar, id_usuario):
        qtd_dias_professor = 15 
        qtd_dias_aluno_funcionario = 10
        
        retorno = cls.exemplar.verificar_se_exemplar_circular(id_exemplar)
        verificar_tipo_usuario = cls.usuario.verificar_tipo_usuario(id_usuario)
        
        if retorno == True:
            
            dia_da_semana = (datetime.today().weekday())
            dia_da_semana += 1
            
            if verificar_tipo_usuario == True:
            
                data_devolucao = date.today() + timedelta(days=qtd_dias_aluno_funcionario)
            
            else:
                data_devolucao = date.today() + timedelta(days=qtd_dias_professor)   


            dicionario = {1: "01", 2: "02", 3: "03", 4:"04" , 5:"05" , 6:"06" , 7:"07" , 8:"08" , 9:"09"}

            mes_dicionario = dicionario.get(data_devolucao.month,"None")
            dia_dicionario = dicionario.get(data_devolucao.day,"None")
            
            if dia_dicionario != "None":
                dia = dia_dicionario
            else:
                dia = data_devolucao.day
                
            if mes_dicionario != "None":
                data = f'{dia}/{mes_dicionario}/{data_devolucao.year}'
                return data

            else:
                data = f'{dia}/{data_devolucao.month}/{data_devolucao.year}'
                return data
        else:
            dia_da_semana = (datetime.today().weekday())
            dia_da_semana += 1
            
            if dia_da_semana == 5:   
                data_devolucao = date.today() + timedelta(days=3)
            
            elif dia_da_semana == 6:   
                data_devolucao = date.today() + timedelta(days=2)
            
            elif dia_da_semana == 7:   
                data_devolucao = date.today() + timedelta(days=1)    
            
            else:
                data_devolucao = date.today() + timedelta(days=1)   
            
            dicionario = {1: "01", 2: "02", 3: "03", 4:"04" , 5:"05" , 6:"06" , 7:"07" , 8:"08" , 9:"09"}
            mes_dicionario = dicionario.get(data_devolucao.month,"None")
            dia_dicionario = dicionario.get(data_devolucao.day,"None")
            
            if dia_dicionario != "None":
                dia = dia_dicionario
            else:
                dia = data_devolucao.day
            
            if mes_dicionario != "None":
                data = f'{dia}/{mes_dicionario}/{data_devolucao.year}'
                return data

            else:
                data = f'{dia}/{data_devolucao.month}/{data_devolucao.year}'
                return data

    @classmethod
    def verficar_se_usuario_tem_pendencia(cls, id_usuario):
        data_atual = formatted_date1 = time.strptime(str(date.today().strftime("%d/%m/%Y")), "%d/%m/%Y")
        
        for emprestimo in cls.exibir_todos_emprestimos():
           if emprestimo.status == 0: 
                if emprestimo.usuario.id == id_usuario:
                    if emprestimo.status_devolucao == False:
                        if data_atual > time.strptime(emprestimo.data_devolucao, "%d/%m/%Y"):
                            return True
                        else:
                            return False    
    
    @classmethod
    def verficar_se_devolucao_esta_atrasada(cls, id_devolucao):
        data_atual = formatted_date1 = time.strptime(str(date.today().strftime("%d/%m/%Y")), "%d/%m/%Y")
        
        for emprestimo in cls.exibir_todos_emprestimos():
            if emprestimo.id == id_devolucao:
                if emprestimo.status_devolucao == False:
                    if data_atual > time.strptime(emprestimo.data_devolucao, "%d/%m/%Y"):
                        return True
                    else:
                        return False   
    
    @classmethod
    def verificar_se_usuario_esta_com_exemplar_de_mesmo_titulo(cls, id_exemplar, id_usuario):
        for emprestimo in cls.exibir_todos_emprestimos():
           if emprestimo.status == 0: 
                if emprestimo.usuario.id == id_usuario:
                    if emprestimo.exemplar.id == id_exemplar:
                        if emprestimo.status_devolucao == False:
                            return True
                        else:
                            return False

    @classmethod
    def consultar_emprestimo_intervalo(cls, data_inicial, data_final):
        date_data_inicial = time.strptime(data_inicial, "%d/%m/%Y")
        date_data_final = time.strptime(data_final, "%d/%m/%Y")
        
        for emprestimo in cls.exibir_todos_emprestimos():
            if time.strptime(emprestimo.data_emprestimo, "%d/%m/%Y") >= date_data_inicial and time.strptime(emprestimo.data_emprestimo, "%d/%m/%Y") <= date_data_final:
                return True
            else:
                return False
    
    @classmethod
    def consultar_qtd_exemplar_emprestado_pelo_titulo_na_data_desejada(cls, data_desejada, id_exemplar):
        date_data_desejada = time.strptime(data_desejada, "%d/%m/%Y")
        
        qtd_exemplares_emprestados = 0
        for emprestimo in cls.exibir_todos_emprestimos():
            if emprestimo.status == 0 and emprestimo.status_devolucao == False:
                    if emprestimo.exemplar.id == id_exemplar:
                        if date_data_desejada == time.strptime(emprestimo.data_devolucao, "%d/%m/%Y"):
                            qtd_exemplares_emprestados += 1
        return qtd_exemplares_emprestados
                         
            
    @classmethod
    def gerar_id_emprestimo(cls): 
          if len(cls.exibir_todos_emprestimos()) == 0:
              return 1
          else:
              for emprestimo in cls.lista_emprestimo:
                  posicao = emprestimo.id
              return posicao + 1   
                
    @staticmethod
    def verificar_se_data_e_valida(data):
        """
        A função validar_data efetua a validação de uma data digitada pelo usuário (DD/MM/AAAA).
        :param texto: Data digitada pelo usuário(DD/MM/AAAA)
        :return: False (caso a data seja inválida) e True (caso a data seja válida)
        """
        data_digitada = str(data[6:]+'-'+data[3:5]+'-'+data[0:2])
        while True:
            try:
                verif = date.fromisoformat(data_digitada)
                return True
            except ValueError:
                return False
    
    @classmethod
    def verificar_emprestimo_id(cls, id_emprestimo):
        for emprestimo in cls.exibir_todos_emprestimos():
            if emprestimo.id == id_emprestimo:
                if emprestimo.status == 0:
                    return True, emprestimo
                else:
                    return False , False
        return False, False
    @classmethod
    def visualizar_se_emprestimo_existe(cls):
        emprestimos_cadastrados = 0

        for emprestimos in cls.lista_emprestimo:
            if emprestimos.status == 0:
                emprestimos_cadastrados += 1
                return True
           
        if emprestimos_cadastrados == 0:
            return False

    @classmethod
    def verificar_se_emprestimo_existe_pelo_id_exemplar(cls, id):
        contador = 0

        for emprestimo in cls.lista_emprestimo:
            if emprestimo.status == 0:
                if emprestimo.exemplar.id == id:
                    contador += 1
        
        if contador > 0:
            return True
        else:
            return False
    
    @classmethod
    def consultar_emprestimo_pelo_id(cls, id):
        for emprestimo in cls.exibir_todos_emprestimos():
            if emprestimo.id == id:
                return emprestimo
        return False
                
        