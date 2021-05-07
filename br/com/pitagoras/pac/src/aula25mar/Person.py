class Person:
    """
        Este é um exemplo básico de uma classe
        veja como é legal inserir aqui um texto
        explicando como a sua classe funciona...
    """

    # Construtor da classe Person (Inicializador) # Método especial.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Imprimir o objeto. Sobrescrevendo o comportamento do método presente na clase Object.
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos de idade'

    def meu_nome(self):
        return self.nome

    def mais_um_ano(self):
        self.idade += 1
        return self.idade

    def fazer_aniversario(self):
        return f"""
            Feliz aniversário {self.nome}, você tinha: {self.idade} anos.
            Agora você tem: {self.mais_um_ano()} :P
        """
        # print(f'Feliz aniversário {self.nome}, você tinha: {self.idade} anos.')
        # self.idade += 1
        # print(f'Agora você tem: {self.idade} :P')

    # TODO: criar um método chamado calcular_pagamento, que recebe as horas trabalhadas.
    # A hora padrão tem valor de 7.5, porém,
    # se for maior do que 21 anos, a hora passa a ser acrescida de 2.5
    # O método deve retornar o valor total.
    def calcular_pagamento(self, horas_trabalhadas):
        taxa_basica = 7.5
        if self.idade >= 21:
            taxa_basica += 2.5

        return (horas_trabalhadas * taxa_basica)

    # TODO: criar um método para determinar se a pessoa é ou não um adolescente.
    # O método terá o nome é adolecente, e retorna true, caso seja verdade.
    def eh_adolescente(self):
        if self.idade < 18:
            return True
        else:
            return False


def my_print(p):
    print(f'Nome: {p.nome}')
    print(f'Idade: {p.idade}')


if __name__ == '__main__':
    p1 = Person(nome='Fabricio', idade=39)
    p2 = Person(idade=39, nome='Miguel Murta')
    p3 = p1

    print('p1')
    my_print(p1)
    print(p1)
    print('p2')
    my_print(p2)
    print(p2)
    print('p3')
    my_print(p3)

    print(p3.fazer_aniversario())
    # print(f'Imprimindo P3: {p3}')
    #
    # print(f'Nome do objeto p1 {p1.meu_nome()}')
    #
    # print(p1.__doc__)
    # print(print.__doc__)
    # print(None)
