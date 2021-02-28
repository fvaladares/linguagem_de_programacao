# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# ClassPerson -> class_person
# firstName -> first_name
#

def test_one():
    print("Programa de teste")
    name = input('Por favor, informe seu nome: ')
    print(name)


def manipulandoDados():
    z = """
           Olá, boa noite.
           Sou o professor Fabrício Valadares
           Curso de Linguagem de programação.
       """
    print(__name__)
    print("Calculadora: ")
    parcela1 = input('Por favor, informe o primeiro número:')
    parcela2 = input('Por favor, informe o segundo número: ')
    print(f"Tipo da parcela1 {type(parcela1)}")

    parcela1 = float(parcela1)
    print(f"Tipo da parcela1 {type(parcela1)}")
    parcela2 = float(parcela2)
    print(f"O resultado da operação de {parcela1} + {parcela2} é {parcela1 + parcela2}")

    print(z)


def manipulandoStrings():
    senha = 'minhaSenha'
    senha2 = input("Informe a senha: ")

    print(senha.upper())
    print(senha.lower())
    print(senha.title())
    print(senha2.title())
    print(senha)
    print(senha.upper() == senha2.upper())


def print_hello():
    format_string = 'Olá {}, seja bem vindo!!{}'
    print(format_string.format('Fabricio', ':)'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hello()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
