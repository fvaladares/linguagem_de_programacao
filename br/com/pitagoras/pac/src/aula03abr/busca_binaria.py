import random


def binary_search(list_fun, key):
    start = 0
    finish = len(list_fun) - 1
    while start < finish:
        middle = (start + finish) // 2
        if key < list_fun[middle]:
            finish = middle - 1
        elif key > list_fun[middle]:
            start = middle + 1
        else:
            return True

    return False


if __name__ == '__main__':
    key_main = 109388
    list_main = random.sample(range(100_000_000), 10_000_000)
    # list_main = list(range(100_000_000))
    # print(f'Before: {list_main}')
    list_main.sort()
    # print(f'After: {list_main}')
    answer = binary_search(key=key_main, list_fun=list_main)

    if answer:
        # index + 1 -> because data sets in python start with index 0
        print(f'{key_main} is preset in your data set')
        print(f'Index of key :{list_main.index(key_main)}')
    else:
        print(f'{key_main} is not preset in your data set')
