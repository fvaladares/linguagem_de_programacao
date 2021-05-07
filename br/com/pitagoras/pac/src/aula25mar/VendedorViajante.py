from br.com.pitagoras.pac.src.aula25mar.Empregado import Empregado


class VendedorViajante(Empregado):
    def __init__(self, nome, idade, id, regiao, vendas):
        super().__init__(nome=nome, idade=idade, id=id)
        self.regiao = regiao
        self.vendas = vendas

    def bonus(self):
        return self.vendas * .5
