# Criando uma função


def print_msg(name, message='Live Long and Prosper'):
    """Imprime uma mensagem de boas vindas."""
    print(name, message)
    print(f'{name} {message}')


#  Criar uma função para calcular a exponenciação, o usuário deve informar
#  Base e o expoente.
def add(parcel_a, parcel_b):
    return parcel_a + parcel_b


def my_power(base, power=2):
    return base ** power


def swap(a, b):
    return b, a


def exemplo_nome():
    name = input('Your name: ')
    print_msg('Fabricio', 'Seja bem vindo!!')
    print_msg(name=name)

    print_msg(message='Bem vindo ao maravilhoso mundo Pythonico :)',
              name='Gabriel')


def funcao_com_retorno():
    a = 2
    b = 3
    print(f'{a} + {b} = {add(a, b)}')
    print(f'{a} ^ {b} = {my_power(a, b)}')
    print(f'{a} ^ {2} = {my_power(a)}')
    x = '11,3,2021'
    y = x.replace(',', '/')
    print(y)
    x = swap(a, b)
    print(f'x = {x} y = {y}')
    print(type(x))


def print_names(*args):
    for i, name in enumerate(args):
        print(f'{i} - Welcome {name}')


def print_family(*args, **kwargs):
    print('Parents:')
    for i in args:
        print('\t', i)
    print('Family members')
    for key in kwargs:
        print(f'\t{key}: Name = {kwargs[key]}')


def funcao_parametros_arbitrarios_e_keyword():
    print_names('Samuel', 'Arthur', 'Carlos', 'Dalmo', 'Davi', 'Leandro', 'Marco', 'Marcus', 'Samuel', 'Stanley')
    print('-' * 25)
    print_family('Fabricio', 'Pollyanna', first_sun='Gabriel', second_sun='Miguel')


def my_function(n):
    return lambda a: a * n


if __name__ == '__main__':
    # exemplo_nome()
    # funcao_com_retorno
    double = lambda i: i * i
    multiplication = lambda i, j: i * j

    print(double(2))
    print(multiplication(2, 10))

    my_doubler = my_function(2)
    triple = my_function(3)

    print('Exemplo: Dobro de um número =  ', my_doubler(365))
    print('Exemplo: Dobro de um número =  ', triple(3))
