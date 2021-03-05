import string

if __name__ == '__main__':
    first_name = 'Fabricio'
    last_name = 'Valadares'

    print('Concatenando strings: ', first_name + ' ' + last_name)
    # Size of a string
    print('The {} has {} characters'.format(first_name, len(first_name)))

    print('A posição 3 da palavra {} possui o caractere: {}'.format(first_name, first_name[2]))
    print('Substring example: ', first_name[1:4])
    print('-' * 25)
    print()
    print('Hi\n' * 10)
    print("Hello world")

    text = 'This is a long string. It is OK.'
    split_text = text.split(' ')
    print('Original String: ', text)
    print('String after split: ', split_text)
    print(type(split_text))
    print(split_text[0])

    print('Count example: ', end='')
    print(text.count('long'))
    year = 2021
    print('A new year ' + str(year))

    print("Comparing Strings: ")
    print("'Name' == 'name':", 'Name' == 'name')
    print("'Name' != 'name':", 'Name' != 'name')

    print('fabricio GERALDO valadares'.title())

    print(f'{first_name:>25}')
    print('|{:>25}|'.format(first_name))

    message = string.Template('$artist sang $song in $year')
    data = dict(artist='Freddie Mercury', song='The Great Pretender', year=1987)
    print(message.substitute(data))
    integer_number = 1
    print(type(integer_number))
    # integer_number = int(input('Please, inform a number: '))
    print(type(integer_number))
    floating_point_number = 10.5
    print(f'Floating point number: {floating_point_number}')
    print(f'Floating point number converted to integer: {int(floating_point_number)}')
    num_a = 10
    num_b = 2
    print(f'Integer division? {num_a / num_b}')
    print(f'Type: {type(num_a / num_b)}')

    num_a = 10
    num_b = 2
    print(f'Division using // {num_a // num_b}')
    print(f'Type: {type(num_a // num_b)}')

    print(f'3//2 = {3 // 2}')
    print(f'-3//2 = {-3 // 2}')

    num_a = 1.5

    print(num_a is not None)
    print('-' * 80)
    num_a = 0
    if num_a > 0:
        print('This is a positive number!!')
    elif num_a == 0:
        print('This is a neutral number!!')
    else:
        print('This is a negative number!!')

    print('Finish!!')

    age = 20
    if 12 < age < 20:
        status = 'teenager'
    else:
        status = 'not teenager'

    status = ('teenager' if 12 < age < 20 else 'not teenager')

    print(status)
    for i in range(0, 10):
        print(i)
