import math

# ------ CONSTANTS --------

MAX_STEPS = 100_000
DIGITS = 4

# ------ HELPERS --------

def F_ratio(x):
    return x / (x + 1)


def F_root(x):
    return math.sqrt(x * x + 1)

# ------ FORMULAS --------

FORMULAS = {
    "ratio": (F_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (F_root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}

# ------ VALIDATE --------

def validate(a, b, steps, low, high, inclusive):
    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("ОШИБКА: пределы интегрирования должны быть конечными числами")
    if a >= b:
        raise ValueError("ОШИБКА: нижний предел должен быть меньше верхнего")

    for value in (a, b):
        if inclusive:
            outside = value < low or value > high
        else:
            outside = value <= low or value >= high
        if outside:
            interval = f"[{low}; {high}]" if inclusive else f"({low}; {high})"
            raise ValueError(f"ОШИБКА: пределы интегрирования должны принадлежать промежутку {interval}")

    if not 1 <= steps <= MAX_STEPS:
        raise ValueError(f"ОШИБКА: число шагов должно быть от 1 до {MAX_STEPS}")

# ------ INTEGRATION --------

def integrate(function, a, b, steps):
    dx = (b - a) / steps
    result = 0

    for i in range(steps):
        x = a + i * dx
        result += function(x) * dx
        
    return result
