import math

# ------ CONSTANTS --------

MAX_TERMS = 10_000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100_000
DIGITS = math.ceil(-math.log10(MAX_EPS))

# ------ HELPERS --------

def sign(n):
    """Вернуть -1 для чётного номера n и 1 для нечётного."""
    if n % 2 == 0:
        return -1

    return 1

# ------ ADDENDS --------

def addend_sqplus(n):
    """Вернуть слагаемое ряда sqplus с номером n, включая знак."""
    return sign(n) / (n * n + 1)

def addend_third(n):
    """Вернуть слагаемое ряда third с номером n, включая знак."""
    return sign(n) / (3 * n)

# ------ FORMULAS --------

FORMULAS = {
    "sqplus": (addend_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + ..."),
    "third": (addend_third, "S = 1/3 - 1/6 + 1/9 - ..."),
}

# ------ VALIDATE --------

def validate(terms, eps):
    """Проверить пределы terms и eps; неиспользуемый параметр равен None."""
    if terms is not None and not 1 <= terms <= MAX_TERMS:
        raise ValueError(f"ОШИБКА: число слагаемых должно быть от 1 до {MAX_TERMS}")
    if eps is not None and not (math.isfinite(eps) and 0 < eps <= MAX_EPS):
        raise ValueError(f"ОШИБКА: точность должна быть конечным числом: 0 < eps <= {MAX_EPS}")

# ------ SUMMATION --------

def sum_by_count(term, count):
    """Вернуть сумму count слагаемых, вычисленных функцией term(n)."""
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result

def sum_by_eps(term, eps):
    """Вернуть сумму и число слагаемых до |term(n)| < eps или вызвать ошибку."""
    result = 0
    n = 0

    while True:
        n += 1
        value = term(n)
        result += value
        
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError(f"ОШИБКА: точность не достигнута за {MAX_ITERATIONS} слагаемых")
