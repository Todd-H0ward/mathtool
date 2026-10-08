# ------ CONSTANTS --------

MAX_COEFFICIENT = 10_000

# ------ HELPERS --------

def format_root(x):
    """Вернуть строку корня x с тремя знаками после запятой."""
    if x == 0:
        x = 0.0
    return f"{x:.3f}"


# ------ VALIDATE -------

def validate(a, b, c):
    """Проверить диапазон коэффициентов a, b, c и наличие неизвестного."""
    for name, value in (("A", a), ("B", b), ("C", c)):
        if abs(value) > MAX_COEFFICIENT:
            raise ValueError(f"ОШИБКА: коэффициент {name} вне допустимого диапазона")
    if a == 0 and b == 0:
        raise ValueError("ОШИБКА: это не уравнение, неизвестное отсутствует")


# ------- SOLVE ---------

def solve(a, b, c):
    """Вернуть вид уравнения, дискриминант и список корней для a, b, c."""
    if a == 0:
        x = -c / b
        return "линейное", None, [x]

    d = b ** 2 - 4 * a * c

    if d < 0:
        return "квадратное", d, []
    elif d == 0:
        x = -b / (2 * a)
        return "квадратное", d, [x]
    else:
        sqrt_d = d ** 0.5
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return "квадратное", d, [x1, x2]

