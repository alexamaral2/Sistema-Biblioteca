from application.model.entity.reserva import Reserva
from application.model.dao.emprestimo_dao import EmprestimoDao
from application.model.dao.exemplar_dao import ExemplarDao
from application.model.dao.usuario_dao import UsuarioDao 
from datetime import *
import time

class ReservaDao:
    emprestimo = EmprestimoDao()
    usuario = UsuarioDao()
    exemplar = ExemplarDao()
    
    lista_reserva = [
        
        Reserva(1, usuario.exibir_usuario_id(1), emprestimo.consultar_emprestimo_pelo_id(1), "25/05/2022", False, "", 0)
    ]
    
    @classmethod
    def exibir_todas_as_reservas(cls):
        return cls.lista_reserva
   
    @classmethod
    def inserir_reserva(cls,id, id_usuario , id_emprestimo, data_reserva):
        verificar_status_usuario = cls.usuario.verificar_status_suspenso(id_usuario)
        msg = False
        verificar_tipo_usuario = cls.usuario.verificar_tipo_usuario(id_usuario)
        
        if verificar_tipo_usuario != "None":
            if verificar_status_usuario != True:
                verificar_pendencia =  cls.emprestimo.verficar_se_usuario_tem_pendencia(id_usuario)

                if verificar_pendencia != True:
                    verificar_reserva_pendente = cls.verficar_se_usuario_tem_reserva_pendente(id_usuario, id_emprestimo)
                    if verificar_reserva_pendente != True:
                        retorno_emprestimo = cls.verificar_se_emprestimo_foi_reservado(id_emprestimo)
                        if retorno_emprestimo != True:
                            cls.lista_reserva.append(Reserva(id, cls.usuario.exibir_usuario_id(id_usuario) , cls.emprestimo.consultar_emprestimo_pelo_id(id_emprestimo), data_reserva, False, "", 0))
                            msg = True
                        else:
                            print("Atenção, O Emprestimo já foi reservado!")
                    else:
                        print("Atenção, O usuário já fez uma reserva desse exemplar!")
                else:
                    print("Atenção, Usuário possui pendências na Biblioteca!")
            else:
                print("Atenção, Usuário está suspenso de Reservar Livro!")
        else:
            print("Atenção, Reserva permitido somente para Aluno, Professor e Funcionário!")
        
        return msg
    
    @classmethod
    def excluir(cls, id, id_usuario, id_emprestimo, data_reserva):
        for i in range(len(cls.exibir_todas_as_reservas())):
            if cls.lista_reserva[i].id == id:
                cls.lista_reserva[i] = Reserva(id, cls.usuario.exibir_usuario_id(id_usuario), cls.emprestimo.consultar_emprestimo_pelo_id(id_emprestimo), data_reserva, False, "Usuario" , 1)       
                msg = True
        return msg
            
    @classmethod
    def verficar_se_usuario_tem_reserva_pendente(cls, id_usuario, id_emprestimo):
        qtd_reserva_usuario = 0
        
        for reserva in cls.exibir_todas_as_reservas():
           if reserva.status == 0: 
               if reserva.usuario.id == id_usuario:
                   if reserva.emprestimo.id == id_emprestimo:
                        qtd_reserva_usuario += 1
        
        if qtd_reserva_usuario > 0:
            return True
        else:
            return False
    
    @classmethod
    def verificar_reserva_id(cls, valor):
        qtd_reserva = 0
        
        for reserva in cls.exibir_todas_as_reservas():
            if reserva.status == 0:
                if reserva.id == valor:
                    reserva_final = reserva
                    qtd_reserva += 1
        
        if qtd_reserva > 0:
                return True,reserva_final
        else: 
            return False, False
                
    @classmethod
    def consultar_reserva_intervalo(cls, data_inicial, data_final):
        date_data_inicial = time.strptime(data_inicial, "%d/%m/%Y")
        date_data_final = time.strptime(data_final, "%d/%m/%Y")
        
        for reserva in cls.exibir_todas_as_reservas():
            if time.strptime(reserva.data_reserva, "%d/%m/%Y") >= date_data_inicial and time.strptime(reserva.data_reserva, "%d/%m/%Y") <= date_data_final:
                return True
            else:
                return False
    
    @staticmethod
    def somar_dias(data_reserva):
        date = datetime.strptime(data_reserva, '%d/%m/%Y').date()
        data_reserva_soma = date + timedelta(days=3)
        
        
        dicionario = {1: "01", 2: "02", 3: "03", 4:"04" , 5:"05" , 6:"06" , 7:"07" , 8:"08" , 9:"09"}

        mes_dicionario = dicionario.get(data_reserva_soma.month,"None")
        dia_dicionario = dicionario.get(data_reserva_soma.day,"None")
        
        if dia_dicionario != "None":
            dia = dia_dicionario
        else:
            dia = data_reserva_soma.day
            
        if mes_dicionario != "None":
            data = f'{dia}/{mes_dicionario}/{data_reserva_soma.year}'
            return data

        else:
            data = f'{dia}/{data_reserva_soma.month}/{data_reserva_soma.year}'
            return data 
    
    @classmethod
    def cancelar_reserva_automaticamente(cls):
        
        data_atual = str(date.today().strftime("%d/%m/%Y"))
        data_atual_formatada = time.strptime(data_atual, "%d/%m/%Y")
        
        for i, reserva in enumerate(cls.exibir_todas_as_reservas()):
            if reserva.status == 0:
                data_formatada = cls.somar_dias(reserva.data_reserva)
                if time.strptime(data_formatada, "%d/%m/%Y") < data_atual_formatada:
                    cls.lista_reserva[i] = Reserva(reserva.id, reserva.usuario, reserva.emprestimo, reserva.data_reserva, False, "Sistema", 1)
    
    @classmethod
    def gerar_id_reserva(cls): 
          if len(cls.exibir_todas_as_reservas()) == 0:
              return 1
          else:
              for reserva in cls.lista_reserva:
                  posicao = reserva.id
              return posicao + 1 
    
    @classmethod
    def visualizar_se_reserva_existe(cls):
        reservas_cadastradas = 0

        for reserva in cls.lista_reserva:
            if reserva.status == 0:
                reservas_cadastradas += 1
                return True
           
        if reservas_cadastradas == 0:
            return False
    
    @classmethod
    def verificar_se_emprestimo_foi_reservado(cls, id_emprestimo):
        for reserva in cls.exibir_todas_as_reservas():
            if reserva.status == 0:
                if reserva.emprestimo.id == id_emprestimo:
                    return True
        return False