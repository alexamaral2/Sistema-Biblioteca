from application.model.dao.emprestimo_dao import EmprestimoDao
from application.model.dao.reserva_dao import ReservaDao
from application.model.dao.livro_dao import LivroDao
from application.model.dao.exemplar_dao import ExemplarDao
from datetime import *
import time

class RelatorioGerencialDao:
    emprestimo = EmprestimoDao()
    livro = LivroDao()
    reserva = ReservaDao()

    @classmethod
    def gerar_relatorio_gerencial_por_periodo_emprestimo(cls, data_inicial, data_final):
        dic_emprestimo = {}  
        date_data_inicial = time.strptime(data_inicial, "%d/%m/%Y")
        date_data_final = time.strptime(data_final, "%d/%m/%Y")
  
        for emprestimo in cls.emprestimo.exibir_todos_emprestimos():
          if time.strptime(emprestimo.data_emprestimo, "%d/%m/%Y") >= date_data_inicial and time.strptime(emprestimo.data_emprestimo, "%d/%m/%Y") <= date_data_final:
               emprestimo_titulo = emprestimo.exemplar.livro.titulo
               if emprestimo_titulo in dic_emprestimo:
                  dic_emprestimo[emprestimo_titulo] += 1
               else:
                  dic_emprestimo[emprestimo_titulo] = 1
               
        return dic_emprestimo

    @classmethod
    def gerar_relatorio_gerencial_por_periodo_reserva(cls, data_inicial, data_final):
        dic_reserva = {}  
        date_data_inicial = time.strptime(data_inicial, "%d/%m/%Y")
        date_data_final = time.strptime(data_final, "%d/%m/%Y")
  
        for reserva in cls.reserva.exibir_todas_as_reservas():
          if time.strptime(reserva.data_reserva, "%d/%m/%Y") >= date_data_inicial and time.strptime(reserva.data_reserva, "%d/%m/%Y") <= date_data_final:
               reserva_titulo = reserva.emprestimo.exemplar.livro.titulo
               if reserva_titulo in dic_reserva:
                  dic_reserva[reserva_titulo] += 1
               else:
                  dic_reserva[reserva_titulo] = 1
               
        return dic_reserva

    @staticmethod
    def lista_qtd_emprestimos(dic_emprestimo, dic_reserva):
       exemplares = ExemplarDao()
       lista_livros = []
       contador = 0
       if len(exemplares.consultar()) > 0:
        for exemplar in exemplares.consultar():
              if exemplar.livro.titulo in dic_emprestimo and exemplar.livro.titulo in dic_reserva:
                    lista_livros.append({"titulo": exemplar.livro.titulo  , "isbn" : exemplar.livro.isbn , "autores" : exemplar.livro.autores , "edicao" : exemplar.livro.edicao , "editora" : exemplar.livro.editora, "ano" : exemplar.livro.ano, "qtd_emprestimo" : dic_emprestimo[exemplar.livro.titulo], "qtd_reserva" : dic_reserva[exemplar.livro.titulo]})
                    contador += 1
              elif exemplar.livro.titulo in dic_emprestimo and exemplar.livro.titulo not in dic_reserva:
                    lista_livros.append({"titulo": exemplar.livro.titulo  , "isbn" : exemplar.livro.isbn , "autores" : exemplar.livro.autores , "edicao" : exemplar.livro.edicao , "editora" : exemplar.livro.editora, "ano" : exemplar.livro.ano, "qtd_emprestimo" : dic_emprestimo[exemplar.livro.titulo], "qtd_reserva" : 0})
                    contador += 1
              elif exemplar.livro.titulo not in dic_emprestimo and exemplar.livro.titulo in dic_reserva:
                    lista_livros.append({"titulo": exemplar.livro.titulo  , "isbn" : exemplar.livro.isbn , "autores" : exemplar.livro.autores , "edicao" : exemplar.livro.edicao , "editora" : exemplar.livro.editora, "ano" : exemplar.livro.ano, "qtd_emprestimo" : 0, "qtd_reserva" : dic_reserva[exemplar.livro.titulo]})
                    contador += 1
        
        if contador > 0 :
          return lista_livros
        else:
          return False        
  

    @staticmethod
    def bubbleSort(alist):
      for passnum in range(len(alist)-1,0,-1):
          for i in range(passnum):
              if alist[i]["qtd_emprestimo"] < alist[i+1]["qtd_emprestimo"]:
                  temp = alist[i]
                  alist[i] = alist[i+1]
                  alist[i+1] = temp
      return alist