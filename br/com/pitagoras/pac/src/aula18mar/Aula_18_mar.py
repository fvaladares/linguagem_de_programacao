class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'
    #     # return 'Name ' + self.name + ' ' + 'age: ' + str(self.age)


def part_one():
    # Tuple created.
    tupla = (3, 5, 7, 9)
    print('Tupla:', tupla)
    print('Tupla tipo de dado:', type(tupla))

    my_list = [2, 4, 6]
    my_tuple = tuple(my_list)

    print('My list: ', my_list)
    print('Type of my_list: ', type(my_list))
    print('My tuple: ', my_tuple)
    print('Type of my_tuple: ', type(my_tuple))

    p1 = Person('Fabricio', 39)
    print(p1)
    tp3 = (p1, 5, 2.2, 'Fome', 'Python', True)
    print(f'TP3 content: {tp3}')
    print(f'typeof(TP3 content): {type(tp3)}')

    print('-' * 25)
    print('My fruits are: ')
    fruits = ('apple', 'pear', 'orange', 'plum', 'apple')
    for i, fruit in enumerate(fruits):
        print(f'\t{i + 1} : {fruit}')
    print('-' * 25)

    # print(f'Name: {p1.name}, age: {p1.age}')
    age = 39
    print(type(age))
    print(age)


def part_two():
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ('Marcos', 'Túlio', 'Carlos')
    tuple3 = (42, tuple1, tuple2, 5.5)

    print(tuple3)

    beatles = ['John', 'Paul', 'George', 'Ringo', 'Paul']
    print(beatles)
    print(f'type(beatles): {type(beatles)}')
    for b in beatles:
        print(b)

    vowelTuple = ('a', 'e', 'i', 'o', 'u')
    print(list(vowelTuple)[4])
    print(beatles[2])
    print(f'Last element of the beatles list: {beatles[len(beatles) - 1]}')
    print(f'Last element of the beatles list: {beatles[-1]}')

    for i, b in enumerate(beatles):
        if 'Paul' == b:
            print(f'Paul is in position {i}')

    beatles.sort()
    print(beatles)
    my_num = [5, 2, 34, 4444, -1]
    my_num.sort()
    print(my_num)


if __name__ == '__main__':
    # part_one()
    # part_two()
    basket = {'apple', 'pear', 'orange', 'plum', 'apple'}
    print(basket)
    basket.add('peach')
    print(basket)
    basket.update(['mango', 'grapefruit'])
    print(basket)
    print(len(basket))
    print(max(basket))
    print(min(basket))
    ordered_list = list(basket)
    ordered_list.sort()
    print(ordered_list)

    numbers = {1, 3, 4, 50, -1, 10}
    print(max(numbers))
    print(min(numbers))
    basket.clear()
    print(f'empty basket: {basket}')

    import os

    os.system('cls' if os.name == 'nt' else 'clear')
