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


# ------ METHODS --------

METHODS = {
    "bubble": bubble_sort
}   
