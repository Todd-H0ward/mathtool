import math

# ------ CONSTANTS --------

MAX_STEPS = 100_000
DIGITS = 4
RATIO_LOW = 0
RATIO_HIGH = 20
ROOT_LOW = -5
ROOT_HIGH = 5

# ------ HELPERS --------

def F_ratio(x):
    """Вернуть значение подынтегральной функции x / (x + 1) в точке x."""
    return x / (x + 1)


def F_root(x):
    """Вернуть значение подынтегральной функции sqrt(x² + 1) в точке x."""
    return math.sqrt(x * x + 1)

# ------ FORMULAS --------

FORMULAS = {
    "ratio": (F_ratio, "F(x) = x / (x + 1)", RATIO_LOW, RATIO_HIGH, True),
    "root": (F_root, "F(x) = sqrt(x^2 + 1)", ROOT_LOW, ROOT_HIGH, False),
}

# ------ VALIDATE --------

def validate(a, b, steps, low, high, inclusive):
    """Проверить a < b и steps; inclusive разрешает границы low и high."""
    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("пределы интегрирования должны быть конечными числами")
    if a >= b:
        raise ValueError("начальный предел не меньше конечного")

    for value in (a, b):
        if inclusive:
            outside = value < low or value > high
        else:
            outside = value <= low or value >= high
        if outside:
            raise ValueError("предел вне промежутка")

    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")

# ------ INTEGRATION --------

def integrate(function, a, b, steps):
    """Вернуть интеграл function на [a; b] по steps левым прямоугольникам."""
    dx = (b - a) / steps
    result = 0

    for i in range(steps):
        x = a + i * dx
        result += function(x) * dx
        
    return result
