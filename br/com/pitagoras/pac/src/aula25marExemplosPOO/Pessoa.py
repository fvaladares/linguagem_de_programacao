class Pessoa:
    """
        Este é um exemplo básico de uma classe
        veja como é legal inserir aqui um texto
        explicando como a sua classe funciona...
    """

    contandor_de_instancia = 0

    @staticmethod
    def metodo_estatico():
        print('Método estático invocado....')

    # cls = Class
    @classmethod
    def incrementar_contador_instancia(cls):
        cls.contandor_de_instancia += 1

    @classmethod
    def get_quantidade_pessoas(cls):
        return cls.contandor_de_instancia

    @classmethod
    def potenciacao(cls, base, expoente):
        return base ** expoente

    # Construtor da classe Pessoa (Inicializador) # Método especial.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.id = Pessoa.contandor_de_instancia
        Pessoa.incrementar_contador_instancia()

    # Imprimir o objeto. Sobrescrevendo o comportamento do método presente na clase Object.
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos de idade e ID = {self.id}'

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


#
if __name__ == '__main__':
    p1 = Pessoa(nome='Fabricio', idade=39)
    p2 = Pessoa(idade=7, nome='Miguel Murta')

    print(p1)
    print(p2)

    print(f'Quantidade de pessoas: {Pessoa.get_quantidade_pessoas()}')

    print()
    print(f'2^2 = {Pessoa.potenciacao(base=2, expoente=2)}')

#     p3 = p1
#
#     print('p1')
#     my_print(p1)
#     print(p1)
#     print('p2')
#     my_print(p2)
#     print(p2)
#     print('p3')
#     my_print(p3)
#
#     print(p3.fazer_aniversario())
#     # print(f'Imprimindo P3: {p3}')
#     #
#     # print(f'Nome do objeto p1 {p1.meu_nome()}')
#     #
#     # print(p1.__doc__)
#     # print(print.__doc__)
#     # print(None)
