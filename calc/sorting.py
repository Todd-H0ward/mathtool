from .arrays import MIN_VALUE, MAX_VALUE

# ------ HELPERS --------

def not_in_order(a, b, descending):
    if descending:
        return a < b
    else:
        return a > b

# ------ SORTING METHODS --------

def bubble_sort(array, descending=False):
    """Отсортировать список на месте пузырьком; вернуть None."""
    n = len(array)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if not_in_order(array[j], array[j + 1], descending):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break


def selection_sort(array, descending=False):
    """Отсортировать список на месте выбором; вернуть None."""
    n = len(array)

    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if not_in_order(array[best], array[j], descending):
                best = j
        array[i], array[best] = array[best], array[i]


def insertion_sort(array, descending=False):
    """Отсортировать список на месте вставками; вернуть None."""
    n = len(array)

    for i in range(1, n):
        current = array[i]
        j = i
        while j > 0 and not_in_order(array[j - 1], current, descending):
            array[j] = array[j - 1]
            j -= 1
        array[j] = current


def counting_sort(array, descending=False):
    """Отсортировать список на месте подсчётом; вернуть None."""
    counts = [0] * (MAX_VALUE - MIN_VALUE + 1)
    for value in array:
        counts[value - MIN_VALUE] += 1

    k = 0
    indices = range(len(counts))
    if descending:
        indices = reversed(indices)
    for index in indices:
        for _ in range(counts[index]):
            array[k] = index + MIN_VALUE
            k += 1


# ------ METHODS --------

METHODS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "counting": counting_sort,
}   
