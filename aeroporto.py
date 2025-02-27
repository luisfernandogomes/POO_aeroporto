class Imovel:
    def __init__(self, tamanho, finalidade, valor, localidade, dono, a_venda=False):
        self.tamanho = tamanho
        self.finalidade = finalidade
        self.valor = valor
        self.localidade = localidade
        self.dono = dono
        self.a_venda = a_venda

    def alugar(self):
        if self.a_venda:
            self.a_venda = False

            if self.valor > 10:
                self.valor /= 10
                print(f'O aeroporto está sendo alugado pelo valor de {self.valor} milhões')
                print(f'O aeroporto está alugado agora')
            else:
                self.valor /= 10
                print(f'O aeroporto está sendo alugado pelo valor de {int(self.valor * 1000)} mil')
                print(f'O aeroporto está alugado agora')
        else:
            print(f'O aeroporto não está disponivel para alugar')

    def status(self):
        if self.tamanho > 10:
            print('aeroporto porte grande')
        elif self.tamanho < 5:
            print('aeroporto porte pequeno')
        else:
            print('aeroporto porte médio')
        print(self.finalidade)
        self.dono = 'imobiliaria'
        if self.a_venda:
            print('aeroporto está a venda')
        else:
            print('aeroporto não está a venda')
        print(f'Está localizado em {self.localidade}')

    def colocar_a_vender(self):
        if self.a_venda:
            print(f'O imovel de {self.dono} já está a venda')
        else:
            print(f'O imovel foi colocado a venda')
            self.a_venda = True

    def parar_de_vender(self):
        if self.a_venda:
            self.a_venda = False
            print(f'O aeroporto não está mais a venda agora')
        else:
            print(f'O aeroporto não está a venda, não tem como parar de vender')


class Aeroporto(Imovel):
    def __init__(self, tamanho, finalidade, valor, localidade, dono, a_venda=False, ativo=False):
        super().__init__(tamanho, finalidade, valor, localidade, dono)
        self.tamanho = tamanho
        self.finalidade = finalidade
        self.valor = valor
        self.localidade = localidade
        self.dono = dono
        self.a_venda = a_venda
        self.qntd_Avioes = 0
        self.funcionarios = 0
        self.ativo = ativo
        self.embarques = 0

    def status(self):
        if self.tamanho > 10:
            print('aeroporto porte grande')
        elif self.tamanho <= 5:
            print('aeroporto porte pequeno')
        else:
            print('aeroporto porte médio')
        self.finalidade = 'comercial'
        print(f'o/os donos do aeroporto é {self.dono}')
        if self.a_venda:
            print(f'está a venda')
        else:
            print(f'não está a venda')

        print(f'total de mebraques {self.embarques}')

        if self.ativo:
            print('aeroporto está em funcionamento')
        else:
            print('aeroporto não está em funcionamento')
        print(f' está ativo no aeroporto {self.qntd_Avioes} avioes')
        print(f'O aeroporto está localizado no {self.localidade}')
        print(f'O aeroporto está avaliado em {self.valor}')
        print(f'O aeroporto tem {self.funcionarios} funcionarios')

    def colocar_a_vender(self):
        print(f'aeroporto não pode ser colocado a venda')

    def decolar(self):
        if self.ativo:
            if self.qntd_Avioes > 0:
                self.qntd_Avioes -= 1
                print(f'O aeroporto tem {self.qntd_Avioes} aviões agora')
                self.embarques += 1
                print(f'O aeroporto tem um embarque a mais agora, total de {self.embarques}')
            else:
                print(f'Não tem aviões disponiveis para embarques, {self.qntd_Avioes}')
        else:
            print(f'o aeroporto não está em funcionamento')

    def aterrissagem(self):
        if self.ativo:
            self.qntd_Avioes += 1
            print(f'O aeroporto {self.dono} tem {self.qntd_Avioes}')
        else:
            print(f'O aeroporto não está em funcionamento')

    def comprar_aviao(self):
        if self.ativo:
            self.qntd_Avioes += 5
            print(f'o {self.dono} comprou um avião')
        else:
            print(f'O aeroporto não está em funcionamento')

    def contratar_funcionarios(self):
        if self.a_venda:
            print(f'O aeroporto do {self.dono} está a venda, não é possivel')
        if not self.ativo:
            print(f'O aeroporto não está em funcionamento, não pode contratar novos funcionarios')
        else:
            self.funcionarios += 10
            print(f'O aeroporto tem funcionarios {self.funcionarios}')
    def abrir_aeroporto(self):
        if self.ativo:
            print(f'O aeroporto já está em funcionamento')
        else:
            self.ativo = True
            print(f'O aeroporto está em funcionamento agora')


imovel1 = Imovel(10, 'comercio', 15, 'Guarulhos', 'Imobiliaria Brasil', True)
porto1 = Aeroporto(10, 'comercial', '17 bilhões', 'Guarulhos', 'Empresa Invapar', False, False)
porto1.status()
