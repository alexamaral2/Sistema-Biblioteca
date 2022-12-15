from application.model.dao.reserva_dao import ReservaDao

class MenuRelatorioGerencial:    
   
    @staticmethod
    def msg_nao_localizado():
        print("Não foi possivel localizar!")
    
    @staticmethod
    def msg_valor_invalido():
        print("Atenção, Valor Inválido!")
    
    @staticmethod
    def msg_retorno_consulta():
        print("Atenção, Nenhum resultado correspondente a pesquisa!")
    
    @staticmethod
    def exibir_relatorio_gerencial(lista):
        print("=-=-=-=- RELATÓRIO GERENCIAL =-=-=-=-")
        for livro in lista:
            print(f"Titulo: {livro['titulo']} | ISBN: {livro['isbn']} | Autore(s): {livro['autores']} | Edição: {livro['edicao']} | Editora: {livro['editora']} | Ano: {livro['ano']} | Qtd Emprestimo: {livro['qtd_emprestimo']} | Qtd Reserva: {livro['qtd_reserva']}") 
            print("=-=-=-=-")

    @staticmethod
    def exibir_todas_reservas():
        reservas = ReservaDao()
        qtd_reserva = 0
        
        print("=-=-=-=- Lista de Reserva =-=-=-=-")
        for reserva in reservas.exibir_todas_as_reservas():
            if reserva.status == 0:
                print(f"N° Reserva : {reserva.id} | Nome Usuário: {reserva.usuario.nome} | Livro: {reserva.exemplar.livro.titulo} | Data Reserva: {reserva.data_reserva}")
                qtd_reserva += 1
                
        if qtd_reserva == 0:
            print("Atenção, Não há Reservas!!")