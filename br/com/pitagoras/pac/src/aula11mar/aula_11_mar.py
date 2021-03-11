# Criando uma função


def print_msg(name, message='Live Long and Prosper'):
    """Imprime uma mensagem de boas vindas."""
    print(name, message)
    print(f'{name} {message}')


#  Criar uma função para calcular a exponenciação, o usuário deve informar
#  Base e o expoente.
def add(parcel_a, parcel_b):
    return parcel_a + parcel_b


def exemplo_nome():
    name = input('Your name: ')
    print_msg('Fabricio', 'Seja bem vindo!!')
    print_msg(name=name)

    print_msg(message='Bem vindo ao maravilhoso mundo Pythonico :)',
              name='Gabriel')


if __name__ == '__main__':
    # exemplo_nome()
    a = 10
    b = 5
    print(f'{a} + {b} = {add(a, b)}')
