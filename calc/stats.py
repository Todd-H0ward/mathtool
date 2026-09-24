from math import sqrt


def calc_stats(numbers):
    count = len(numbers)

    if count == 0:
        return {"count": count}

    total = sum(numbers)
    sq_sum = sum(x * x for x in numbers)
    avg = total / count
    rms = sqrt(sq_sum / count)
    variance = sq_sum / count - avg ** 2
    sko = sqrt(variance)

    if count > 1:
        sample_std = sqrt(sum((x - avg) ** 2 for x in numbers) / (count - 1))
    else:
        sample_std = 0.0

    return {
        "count": count,
        "total": total,
        "avg": avg,
        "sq_sum": sq_sum,
        "rms": rms,
        "variance": variance,
        "sko": sko,
        "sample_std": sample_std,
        "minimum": min(numbers),
        "maximum": max(numbers),
        "positives": sum(1 for x in numbers if x > 0),
        "negatives": sum(1 for x in numbers if x < 0),
    }
