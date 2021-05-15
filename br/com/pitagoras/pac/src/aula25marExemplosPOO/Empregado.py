from br.com.pitagoras.pac.src.aula25marExemplosPOO.Pessoa import Pessoa


class Empregado(Pessoa):
    def __init__(self, nome, idade, id):
        super().__init__(nome=nome, idade=idade)
        self.id = id

    # TODO: criar um método chamado calcular_pagamento, que recebe as horas trabalhadas.
    # A hora padrão tem valor de 7.5, porém,
    # se for maior do que 21 anos, a hora passa a ser acrescida de 2.5
    # O método deve retornar o valor total.

    def calcular_pagamento(self, horas_trabalhadas):
        taxa_basica = 7.5
        if self.idade >= 21:
            taxa_basica += 2.5

        return (horas_trabalhadas * taxa_basica)
