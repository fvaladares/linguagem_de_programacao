import random


def selection_sort(list_func):
    n = len(list_func)

    for i in range(0, n):
        index_min = i
        for j in range(i + 1, n):
            if list_func[j] < list_func[index_min]:
                index_min = j
        list_func[i], list_func[index_min] = list_func[index_min], list_func[i]
        # temp = list_func[index_min]
        # list_func[index_min] = list_func[i]
        # list_func[i] = temp

    return list_func


def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        insert_value = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > insert_value:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = insert_value
    return lista


if __name__ == '__main__':
    # lista = [10, 9, 5, 8, 11, -1, 3]

    lista = random.sample(range(100_000), 10_000)
    print(f'Unordered: {lista}')

    ordered_list3 = insertion_sort(lista)
    print(f'Insertion sort:   {ordered_list3}')

    ordered_list = selection_sort(lista)
    print(f'Selection Sort:   {ordered_list}')

    ordered_list2 = bubble_sort(lista)
    print(f'Bubble sort:   {ordered_list2}')
