def recursive_function(count):
    print(f'calling recursive_function({count}) ')
    if count > 0:
        recursive_function(count - 1)


def factorial(n):
    if n == 1:
        print(f'1 ')
        return 1  # caso base
    else:
        res = n * factorial(n - 1)  # chamada recursiva
        print(f'{res} ')
        return res


def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        print(f'{acc} ')
        return tail_factorial(n - 1, acc * n)


if __name__ == '__main__':
    # recursive_function(100)
    tail_factorial(996)
    factorial(996)
