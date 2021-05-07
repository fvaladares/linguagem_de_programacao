# import functools
from functools import reduce

from Person import Person


def primeira_parte():
    # As chaves não strings"
    dict_01 = dict(MG='BH', MT='CB', MS='CG')
    print(f'dict_01 {dict_01}')

    # Os pares chave valor são tuplas
    dict_02 = dict([('MG', 'BH'), ('MT', 'CB'), ('MS', 'CG')])
    print(f'dict_02 {dict_02}')

    # par chave valor são listas
    dict_03 = dict((['MG', 'BH'], ['MT', 'CB'], ['MS', 'CG']))
    print(f'dict_03 {dict_03}')

    print(f'dict_03[MG] "teste"= {dict_03["MG"]}')
    print(f'dict_03.get(MG) = {dict_03.get("MG")}')

    dict_03['SC'] = 'FS'
    print(f'dict_03 {dict_03}')

    dict_03['SC'] = 'BL'
    print(f'dict_03 {dict_03}')

    print(dict_03)
    print(dict_03.popitem())
    print(f'popitem: {dict_03}')
    print(dict_03.pop('MG'))
    print(f'pop("MG"): {dict_03}')
    del dict_03['MT']
    print(f'del: {dict_03}')


def segunda_parte():
    estados_capitais = {'Maranhão': 'São Luís',
                        'Mato Grosso': 'Cuiabá',
                        'Mato Grosso do Sul': 'Campo Grande',
                        'Minas Gerais': 'Belo Horizonte'
                        }

    print(estados_capitais)
    print('-' * 25)
    for key in estados_capitais:
        print(f'\t{key}', end=', ')
        print(estados_capitais[key])

    print('-' * 25)
    for capital in estados_capitais.values():
        print(f'\t{capital}')

    print(list(estados_capitais.values())[0])
    print(estados_capitais.keys())
    print(estados_capitais.items())

    print('Verifica se o valor está presente nas chaves: ')
    print(f"\t{'Belo Horizonte' in estados_capitais}")

    print('Verifica se o valor está presente nos valores')
    print(f"\t{'Belo Horizonte' in estados_capitais.values()}")

    print(f'Tamanho do dicionário: {len(estados_capitais)}')


def terceira_parte():
    set_a = {'apple', 'orange', 'banana', 'lime'}
    set_b = {'grapefruit', 'lime', 'banana'}

    print(f'set_a {set_a}')
    print(f'set_b {set_b}')
    print(f'Union: {set_a | set_b}')
    print(f'Intersection: {set_a & set_b}')
    print(f'Difference (set_a - set_b): {set_a - set_b}')
    print(f'Difference (set_b - set_a): {set_b - set_a}')
    print(f'Symetric Diference: {set_a ^ set_b}')


def quarta_parte():
    data = [1, 3, 5, 2, 7, 4, 10]
    print(type(data))
    print(f'list data: {data}')

    data_filtered = list(filter(lambda i: i % 2 == 0, data))
    print(f'data_filtered(even numbers) = {data_filtered}')

    def is_even(i):
        return i % 2 == 0

    data_filtered = list(filter(is_even, data))
    print(f'data_filtered(even numbers)(função de baixa ordem) = {data_filtered}')

    person_data = [Person('Fabricio', 39), Person('Pollyanna', 39), Person('Gabriel', 17), Person('Miguel', 7)]
    print(f'person_data: {person_data}')
    print('-' * 80)
    for person in person_data:
        print(person, end=', ')
    print()
    print('-' * 80)

    person_filtered = list(
        filter(
            lambda p: p.age >= 18,
            person_data
        )
    )

    print('-' * 80)
    for person in person_filtered:
        print(person, end=', ')
    print()
    print('-' * 80)

    print(type(data))
    print(f'list data: {data}')
    data_transformed = list(
        map(
            lambda i: i ** 2,
            data
        )
    )
    print(f'data_transformed: {data_transformed}')

    print('-' * 80)
    for person in person_data:
        print(person, end=', ')
    print()
    print('-' * 80)
    ages = list(
        map(
            lambda a: a.age,
            person_data
        )
    )
    print(f'ages: {ages}')

    print(type(data))
    print(f'list data: {data}')
    result = reduce(
        lambda total, value: total + value,
        data,
        0
    )
    print(result)

    print('-' * 80)
    for person in person_data:
        print(person, end=', ')
    print()
    print('-' * 80)

    total_age = reduce(
        lambda total_age, p: total_age + p.age,
        person_data,
        0
    )
    average_age = total_age // len(person_data)
    print(f'Average age: {average_age}')


def quinta_parte():
    person = Person(nome='Fabricio Valadares', idade=39)
    print(person)
    print(f'Salario de {person.name}: R$ {person.calcular_pagamento(10)}')
    if person.eh_adolescente():
        print(f'{person.name} eh adolescente')
    else:
        print(f'{person.name} está velho')


if __name__ == '__main__':
    # primeira_parte()
    # segunda_parte()
    # terceira_parte()
    # quarta_parte()
    quinta_parte()
#     CRIAR UM DICIONARIO ANINHADO, ONDE A CHAVE É A REGIÃO, E OS VALORES, OS ESTADOS PERTENCENTES À REGIÃO.
