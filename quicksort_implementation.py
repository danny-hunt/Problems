import random

array = list(range(10))
random.shuffle(array)


def quicksort(array, first, last):

    if first >= last:
        return

    i, j = first, last
    pivot = array[random.randint(first, last)]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    quicksort(array, first, j)
    quicksort(array, i, last)



print(array)
print(quicksort(array, 0, len(array)- 1))
print(array)

