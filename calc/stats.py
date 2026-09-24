import math


def total(numbers):
    result = 0
    for value in numbers:
        result += value
    return result


def mean(numbers):
    return total(numbers) / len(numbers)


def minimum(numbers):
    result = numbers[0]
    for value in numbers:
        if value < result:
            result = value
    return result


def maximum(numbers):
    result = numbers[0]
    for value in numbers:
        if value > result:
            result = value
    return result


def count_positive(numbers):
    result = 0
    for value in numbers:
        if value > 0:
            result += 1
    return result


def count_negative(numbers):
    result = 0
    for value in numbers:
        if value < 0:
            result += 1
    return result


def sum_sq(numbers):
    result = 0
    for value in numbers:
        result += value ** 2
    return result


def sum_sq_dev(numbers):
    mean = mean(numbers)
    result = 0
    for value in numbers:
        result += (value - mean) ** 2
    return result


def variance(numbers):
    return sum_sq_dev(numbers) / len(numbers)


def sko(numbers):
    return math.sqrt(variance(numbers))


def sample_std(numbers):
    if len(numbers) < 2:
        return None
    return math.sqrt(sum_sq_dev(numbers) / (len(numbers) - 1))


def rms(numbers):
    return math.sqrt(sum_sq(numbers) / len(numbers))


def calc_stats(numbers):
    count = len(numbers)

    if count == 0:
        return {"count": count}

    sample_std = sample_std(numbers)

    return {
        "count": count,
        "total": total(numbers),
        "avg": mean(numbers),
        "sq_sum": sum_sq(numbers),
        "rms": rms(numbers),
        "variance": variance(numbers),
        "sko": sko(numbers),
        "sample_std": sample_std,
        "minimum": minimum(numbers),
        "maximum": maximum(numbers),
        "positives": count_positive(numbers),
        "negatives": count_negative(numbers),
    }
