# ------ HELPERS --------

def _format_root(x):
    if x == 0:
        x = 0.0
    return f"{x:.3f}"


# ------ VALIDATE -------

def validate(a, b, c):
    if a == 0 and b == 0:
        raise ValueError("это не уравнение, неизвестное отсутствует")


# ------- SOLVE ---------

def solve(a, b, c):
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
