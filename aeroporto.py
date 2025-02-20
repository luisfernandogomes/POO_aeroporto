class Imovel:
    def __init__(self, tamanho, finalidade, valor, localidade, dono, a_venda):


class Aeroporto(Imovel):
    def __init__(self,tamanho, finalidade, valor, localidade, dono, a_venda=True, qntd_Avioes):
        super().__init__(tamanho, finalidade, valor, localidade, dono, a_venda, qntd_Avioes )
        self.qntd_Avioes = qntd_Avioes
        self.tamanho = tamanho
        self.localidade = localidade
        self.dono = dono
        self.valor = valor
        self.embarques = embarques
        self.a_venda = a_venda
        tamanho, qntd_Avioes, tamanho, localidade, dono, valor, embarques
