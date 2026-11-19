import sys
from math import isfinite

from cli import build_parser
from calc import equation, sorting, stats, series, integration, arrays

# ------ HELPERS ------

def parse_int(text):
    """Преобразовать text в целый коэффициент или вызвать ValueError."""
    try:
        return int(text)
    except (ValueError, TypeError):
        raise ValueError("коэффициент не является целым числом")


def parse_float(text):
    """Преобразовать text в конечное число в допустимом для stats диапазоне."""
    try:
        num = float(text)
    except (ValueError, TypeError):
        raise ValueError(f"{text} не является числом")
    if not isfinite(num) or abs(num) > stats.MAX_VALUE:
        raise ValueError(f"{text} не является допустимым числом")
    return num


def read_numbers(source):
    """Вернуть проверенный список чисел из строки source или потока строк."""
    numbers = []

    if isinstance(source, str):
        for word in source.split():
            numbers.append(parse_float(word))
    else:
        for line in source:
            for word in line.split():
                numbers.append(parse_float(word))

    if len(numbers) == 0:
        raise ValueError("последовательность пуста")
    if len(numbers) > stats.MAX_COUNT:
        raise ValueError(f"чисел больше {stats.MAX_COUNT}")
    return numbers


def format_root(x):
    """Вернуть строку корня x с тремя знаками, исключая отрицательный ноль."""
    if x == 0:
        x = 0.0
    return f"{x:.3f}"


# ------ COMMAND HANDLERS --------

def handle_solve(args):
    """Прочитать коэффициенты из args или stdin, вывести корни и вернуть код 0."""
    if args.a is None and args.b is None and args.c is None:
        a = parse_int(input("Введите A: "))
        b = parse_int(input("Введите B: "))
        c = parse_int(input("Введите C: "))
    elif args.a is not None and args.b is not None and args.c is not None:
        a = args.a
        b = args.b
        c = args.c
    else:
        raise ValueError("укажите все три коэффициента либо ни одного")

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
    """Прочитать числа из args.input или stdin, вывести статистику и вернуть 0."""
    if args.input is None:
        numbers = read_numbers(sys.stdin)
    else:
        try:
            with open(args.input, encoding="utf-8-sig") as f:
                numbers = read_numbers(f)
        except OSError as exc:
            raise ValueError("файл не открывается") from exc

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
    """Вычислить ряд по параметрам args, вывести сумму и вернуть код 0."""
    series.validate(args.terms, args.eps)
    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        result = series.sum_by_count(term, args.terms)
        count = args.terms
    else:
        result, count = series.sum_by_eps(term, args.eps)

    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")

    return 0


def handle_integrate(args):
    """Вычислить интеграл по параметрам args, вывести результат и вернуть код 0."""
    function, formula, low, high, inclusive = integration.FORMULAS[args.func]
    integration.validate(args.a, args.b, args.steps, low, high, inclusive)

    result = integration.integrate(function, args.a, args.b, args.steps)

    print(formula)
    print(f"Значение интеграла: {result:.{integration.DIGITS}f}")
    print(f"Количество шагов: {args.steps}")

    return 0

def handle_fill(args):
    """Заполнить массив рандомными числами"""

    if args.min < arrays.MIN_VALUE:
        raise ValueError("Минимальная граница меньше чем ограничение")

    if args.max > arrays.MAX_VALUE:
        raise ValueError("Максимальная граница превышает ограничение")

    result = arrays.fill(args.count, args.min, args.max, args.seed)

    print(result)
    arrays.write_array(result, args.output)

    return 0


def handle_sort(args):
    """Прочитать массив, отсортировать и вывести или записать результат."""
    array = arrays.read_array(args.input)
    method = sorting.METHODS[args.method]
    descending = args.order == "desc"
    method(array, descending)

    arrays.write_array(array, args.output)
    if args.output:
        print(f"Записано элементов: {len(array)}; файл: {args.output}")
    print("Сортировка прошла успешно")
    return 0


def handle_search(args):
    return 1


# ------ COMMAND TABLE --------

HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
    "fill": handle_fill,
    "sort": handle_sort,
    "search": handle_search,
}


# ------ ENTRY POINT --------

def main(argv=None):
    """Разобрать argv, выполнить команду и вернуть код 0 или 1 при ошибке данных."""
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
