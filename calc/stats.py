import math

# ------ CONSTANTS --------

MAX_VALUE = 10_000
MAX_COUNT = 20

# ------ BASIC STATISTICS --------

def total(numbers):
    """Вернуть сумму чисел из последовательности numbers."""
    result = 0
    for value in numbers:
        result += value
    return result


def mean(numbers):
    """Вернуть среднее арифметическое непустой последовательности numbers."""
    return total(numbers) / len(numbers)


def minimum(numbers):
    """Вернуть наименьшее число непустой последовательности numbers."""
    result = numbers[0]
    for value in numbers:
        if value < result:
            result = value
    return result


def maximum(numbers):
    """Вернуть наибольшее число непустой последовательности numbers."""
    result = numbers[0]
    for value in numbers:
        if value > result:
            result = value
    return result


def count_positive(numbers):
    """Вернуть количество положительных чисел в numbers."""
    result = 0
    for value in numbers:
        if value > 0:
            result += 1
    return result


def count_negative(numbers):
    """Вернуть количество отрицательных чисел в numbers."""
    result = 0
    for value in numbers:
        if value < 0:
            result += 1
    return result


# ------ SQUARES AND DEVIATIONS --------

def sum_sq(numbers):
    """Вернуть сумму квадратов чисел из numbers."""
    result = 0
    for value in numbers:
        result += value ** 2
    return result


def sum_sq_dev(numbers):
    """Вернуть сумму квадратов отклонений numbers от их среднего."""
    m = mean(numbers)
    result = 0

    for value in numbers:
        result += (value - m) ** 2

    return result


def variance(numbers):
    """Вернуть дисперсию непустой последовательности numbers."""
    return sum_sq_dev(numbers) / len(numbers)


def sko(numbers):
    """Вернуть среднее квадратичное отклонение чисел из numbers."""
    return math.sqrt(variance(numbers))


def sample_std(numbers):
    """Вернуть выборочное стандартное отклонение numbers или None при n < 2."""
    if len(numbers) < 2:
        return None
    return math.sqrt(sum_sq_dev(numbers) / (len(numbers) - 1))


def rms(numbers):
    """Вернуть среднее квадратичное непустой последовательности numbers."""
    return math.sqrt(sum_sq(numbers) / len(numbers))


# ------ SUMMARY --------

def calc_stats(numbers):
    """Вернуть словарь статистических показателей последовательности numbers."""
    count = len(numbers)

    if count == 0:
        return {"count": count}

    std = sample_std(numbers)

    return {
        "count": count,
        "total": total(numbers),
        "avg": mean(numbers),
        "sq_sum": sum_sq(numbers),
        "rms": rms(numbers),
        "variance": variance(numbers),
        "sko": sko(numbers),
        "sample_std": std,
        "minimum": minimum(numbers),
        "maximum": maximum(numbers),
        "positives": count_positive(numbers),
        "negatives": count_negative(numbers),
    }
