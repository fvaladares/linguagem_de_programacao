class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f'Saldo atual: R$ {self.saldo:.2f}'

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError(f'ERRO!: Valor decladarado para depósito é inválido: R$ {valor:.2f}')


if __name__ == '__main__':

    # c1.deposito(-1000.00)
    # print(c1)
    c1 = Conta(100)
    print(c1)
    c1.deposito(100)
    print(c1)
    try:
        c1.deposito(-1000.00)
        print(c1)
    except ValueError as ve:
        print(ve)

    print(c1)

    try:
        print(f'{10 / 0}')
    except ZeroDivisionError as zde:
        print(f'ERRO ({zde.__str__()}): Não é possível dividir por zero utilizando números naturais.')
