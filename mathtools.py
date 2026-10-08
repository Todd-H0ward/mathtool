import sys
from math import isfinite

from cli import build_parser
from calc import equation, stats, series, integration

# ------ CONSTANTS ------

MAX_VALUE = 10000
MAX_COUNT = 20

# ------ HELPERS ------

def parse_int(text):
    try:
        return int(text)
    except (ValueError, TypeError):
        raise ValueError("ОШИБКА: коэффициент не является целым числом")


def check_coefficients(coefficients):
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"ОШИБКА: коэффициент {name} вне допустимого диапазона")


def parse_float(text):
    try:
        num = float(text)
    except (ValueError, TypeError):
        raise ValueError(f"ОШИБКА: {text!r} не является числом")
    if not isfinite(num) or abs(num) > MAX_VALUE:
        raise ValueError(f"ОШИБКА: {text!r} не является допустимым числом")
    return num


def read_numbers(source):
    numbers = []

    if type(source) == str:
        for word in source.split(" "):
            numbers.append(parse_float(word))
    else:
        for line in source:
            for word in line.split(" "):
                numbers.append(parse_float(word))

    if len(numbers) == 0:
        raise ValueError("ОШИБКА: список чисел пуст")
    if len(numbers) > MAX_COUNT:
        raise ValueError(f"ОШИБКА: чисел больше {MAX_COUNT}")
    return numbers


def format_root(x):
    if x == 0:
        x = 0.0
    return f"{x:.3f}"


def handle_solve(args):
    if args.a is None and args.b is None and args.c is None:
        a = parse_int(input("Введите A: "))
        b = parse_int(input("Введите B: "))
        c = parse_int(input("Введите C: "))
        check_coefficients({"A": a, "B": b, "C": c})
    elif args.a is not None and args.b is not None and args.c is not None:
        a = parse_int(args.a)
        b = parse_int(args.b)
        c = parse_int(args.c)
        check_coefficients({"A": a, "B": b, "C": c})
    else:
        raise ValueError("укажите все три коэффициента (-a, -b, -c) или ни одного")

    equation.validate(a, b, c)
    kind, d, roots = equation.solve(a, b, c)

    if kind == "линейное":
        print("Уравнение линейное")
        print(f"x = {format_root(roots[0])}")
    else:
        print("Уравнение квадратное")
        print(f"D = {d}")
        if len(roots) == 0:
            print("Действительных корней нет")
        elif len(roots) == 1:
            print(f"x = {format_root(roots[0])}")
        else:
            print(f"x1 = {format_root(roots[0])}")
            print(f"x2 = {format_root(roots[1])}")

    return 0

def handle_stats(args):
    if args.input is None:
        nums_input = input("Введите числа: ");
        numbers = read_numbers(nums_input)
    else:
        with open(args.input, encoding="utf-8-sig") as f:
            numbers = read_numbers(f)

    s = stats.calc_stats(numbers)

    print(f"Количество: {s['count']}")

    if s['count'] == 0:
        return 0

    print(f"Сумма: {s['total']:.3f}")
    print(f"Ср. арифм.: {s['avg']:.3f}")
    print(f"Сумма кв.: {s['sq_sum']:.3f}")
    print(f"Ср. кв.: {s['rms']:.3f}")
    print(f"Дисперсия: {s['variance']:.3f}")
    print(f"СКО: {s['sko']:.3f}")
    print(f"Станд. откл.: {s['sample_std']:.3f}" if s['sample_std'] is not None else "Станд. откл.: НЕ СУЩЕСТВУЕТ")
    print(f"Наименьшее: {s['minimum']:.3f}")
    print(f"Наибольшее: {s['maximum']:.3f}")
    print(f"Положительных: {s['positives']}")
    print(f"Отрицательных: {s['negatives']}")

    return 0


def handle_series(args):
    series.validate(args.terms, args.eps)
    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        result = series.sum_by_count(term, args.terms)
        count = args.terms
    else:
        result, count = series.sum_by_eps(term, args.eps)

    print(formula)
    print(f"Сумма: {result:.{series.DIGITS}f}")
    print(f"Количество слагаемых: {count}")

    return 0


def handle_integrate(args):
    function, formula, low, high, inclusive = integration.FORMULAS[args.func]
    integration.validate(args.a, args.b, args.steps, low, high, inclusive)

    result = integration.integrate(function, args.a, args.b, args.steps)

    print(formula)
    print(f"Интеграл: {result:.{integration.DIGITS}f}")
    print(f"Количество шагов: {args.steps}")

    return 0

HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = HANDLERS[args.command]

    try:
        return handler(args)
    except (ValueError, OSError) as exc:
        print(f"ОШИБКА: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
