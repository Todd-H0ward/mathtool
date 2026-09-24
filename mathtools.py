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
        num = int(text)
    except (ValueError, TypeError):
        raise ValueError("коэффициент не является целым числом")
    if abs(num) > MAX_VALUE:
        raise ValueError("значение вне допустимого диапазона")
    return num


def parse_float(text):
    try:
        num = float(text)
    except (ValueError, TypeError):
        raise ValueError("коэффициент не является числом")
    if not isfinite(num) or abs(num) > MAX_VALUE:
        raise ValueError("значение вне допустимого диапазона")
    return num


def validate_count(count):
    if count < 0 or count > MAX_COUNT:
        raise ValueError("количество чисел вне допустимого диапазона")


def _read_numbers_stdin():
    count = parse_int(input("Введите количество: "))
    validate_count(count)
    numbers = [parse_float(input()) for _ in range(count)]
    return numbers


def _read_numbers_file(path):
    try:
        with open(path) as f:
            text = f.read()
    except OSError:
        raise ValueError(f"не удалось прочитать файл: {path}")
    numbers = [parse_float(token) for token in text.split()]
    validate_count(len(numbers))

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
    elif args.a is not None and args.b is not None and args.c is not None:
        a = parse_int(args.a)
        b = parse_int(args.b)
        c = parse_int(args.c)
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
        numbers = _read_numbers_stdin()
    else:
        numbers = _read_numbers_file(args.input)

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
    print(f"Станд. откл.: {s['sample_std']:.3f}")
    print(f"Наименьшее: {s['minimum']:.3f}")
    print(f"Наибольшее: {s['maximum']:.3f}")
    print(f"Положительных: {s['positives']}")
    print(f"Отрицательных: {s['negatives']}")
    return 0


def handle_series(args):
    print(series.calc_series())
    return 0


def handle_integrate(args):
    print(integration.calc_integrate())
    return 0

HANDLERS = {
    "solve":     handle_solve,
    "stats":     handle_stats,
    "series":    handle_series,
    "integrate": handle_integrate,
}

HELP_TEXT = """\
Математический инструмент

Использование:
  mathtools.py --help                        вывести эту справку
  mathtools.py solve                         запросить коэффициенты у пользователя
  mathtools.py solve -a A -b B -c C         взять коэффициенты из параметров
  mathtools.py stats [--input FILE]          статистика по числам (ввод или файл)
  mathtools.py series                        сумма ряда
  mathtools.py integrate                     численное интегрирование

Коэффициенты — целые числа |x| <= 10000.
Для stats: не более 20 вещественных чисел, |x| <= 10000, без NaN и бесконечностей."""


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        print(HELP_TEXT)
        return 0

    handler = HANDLERS[args.command]
    try:
        return handler(args)
    except ValueError as exc:
        print(f"ОШИБКА: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
