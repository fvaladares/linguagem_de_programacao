class Person:
    """
        Este é um exemplo básico de uma classe
        veja como é legal inserir aqui um texto
        explicando como a sua classe funciona...
    """

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

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
