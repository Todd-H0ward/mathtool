import argparse

from calc.series import FORMULAS, MAX_EPS, MAX_TERMS
from calc.integration import FORMULAS as INTEGRATION_FORMULAS, MAX_STEPS
from calc.sorting import METHODS
from calc.equation import MAX_COEFFICIENT
from calc.stats import MAX_COUNT, MAX_VALUE
from calc.arrays import (
    MAX_COUNT as MAX_ARRAY_COUNT,
    MIN_VALUE as MIN_ARRAY_VALUE,
    MAX_VALUE as MAX_ARRAY_VALUE,
    MAX_SEARCH,
)

# ------ PARSER --------

def build_parser():
    """Вернуть парсер математических команд с их параметрами."""
    parser = argparse.ArgumentParser(
        prog="mathtools.py",
        description="Математический инструмент: уравнение, статистика, ряд, интеграл, массивы.",
        allow_abbrev=False
    )
    sub = parser.add_subparsers(dest="command")

    # ------ SOLVE --------

    p_solve = sub.add_parser(
        "solve",
        help="решить уравнение A·x²+B·x+C=0",
        description="Решение квадратного или линейного уравнения A·x²+B·x+C=0. "
                    f"Коэффициенты — целые числа |x| <= {MAX_COEFFICIENT}.",
        allow_abbrev=False
    )

    p_solve.add_argument("-a", type=int, default=None, metavar="A", help=f"коэффициент A (целое, |A| <= {MAX_COEFFICIENT})")
    p_solve.add_argument("-b", type=int, default=None, metavar="B", help=f"коэффициент B (целое, |B| <= {MAX_COEFFICIENT})")
    p_solve.add_argument("-c", type=int, default=None, metavar="C", help=f"коэффициент C (целое, |C| <= {MAX_COEFFICIENT})")

    # ------ STATS --------

    p_stats = sub.add_parser(
        "stats",
        help="статистика по последовательности чисел",
        description="Вычисляет статистические показатели последовательности "
                    f"вещественных чисел (не более {MAX_COUNT}, |x| <= {MAX_VALUE}).",
        allow_abbrev=False
    )
    p_stats.add_argument("--input", metavar="FILE", default=None, help="прочитать числа из файла (по умолчанию — из стандартного ввода до конца потока)")

    # ------ SERIES --------

    p_series = sub.add_parser(
        "series",
        help="вычислить сумму ряда",
        description="Вычисляет сумму математического ряда.",
        allow_abbrev=False
    )

    p_series.add_argument("--func", required=True, choices=sorted(FORMULAS), help="формула ряда")
    series_mode = p_series.add_mutually_exclusive_group(required=True)
    series_mode.add_argument("--terms", type=int, metavar="N", help=f"число слагаемых (от 1 до {MAX_TERMS})")
    series_mode.add_argument("--eps", type=float, metavar="EPS", help=f"точность (0 < EPS <= {MAX_EPS})")

    # ------ INTEGRATE --------

    p_integrate = sub.add_parser(
        "integrate",
        help="численное интегрирование",
        description="Вычисляет определённый интеграл методом численного интегрирования.",
        allow_abbrev=False
    )
    p_integrate.add_argument("--func", required=True, choices=sorted(INTEGRATION_FORMULAS), help="подынтегральная функция")
    p_integrate.add_argument("--from", dest="a", required=True, type=float, metavar="A", help="нижний предел интегрирования")
    p_integrate.add_argument("--to", dest="b", required=True, type=float, metavar="B", help="верхний предел интегрирования")
    p_integrate.add_argument("--steps", required=True, type=int, metavar="N", help=f"число шагов (от 1 до {MAX_STEPS})")

    # ------ FILL --------

    p_fill = sub.add_parser(
        "fill",
        help="создать массив случайных целых чисел",
        description="Создаёт массив случайных целых чисел в заданных границах.",
        allow_abbrev=False
    )
    p_fill.add_argument("-c", "--count", required=True,
                        type=int, metavar="COUNT",
                        help=f"количество элементов (от 1 до {MAX_ARRAY_COUNT})")
    p_fill.add_argument("--min", type=int,
                        default=MIN_ARRAY_VALUE, metavar="MIN",
                        help=f"нижняя граница (по умолчанию {MIN_ARRAY_VALUE}; min <= max)")
    p_fill.add_argument("--max", type=int,
                        default=MAX_ARRAY_VALUE, metavar="MAX",
                        help=f"верхняя граница (по умолчанию {MAX_ARRAY_VALUE}; min <= max)")
    p_fill.add_argument("--seed", type=int, default=None, metavar="SEED",
                        help="начальное значение генератора (целое, по умолчанию не задано)")
    p_fill.add_argument("-o", "--output", default=None, metavar="FILE",
                        help="файл для массива (по умолчанию — вывод на экран)")

    # ------ SORT --------

    p_sort = sub.add_parser(
        "sort",
        help="сортировать массив",
        description="Сортирует массив выбранным методом.",
        allow_abbrev=False
    )
    p_sort.add_argument("-m", "--method", required=True,
                        choices=METHODS,
                        help="метод сортировки")
    p_sort.add_argument("--order", choices=("asc", "desc"), default="asc",
                        help="asc — по возрастанию, desc — по убыванию (по умолчанию asc)")
    p_sort.add_argument("-i", "--input", default=None, metavar="FILE",
                        help="файл с исходным массивом (по умолчанию — ввод с клавиатуры)")
    p_sort.add_argument("-o", "--output", default=None, metavar="FILE",
                        help="файл для результата (по умолчанию - вывод на экран)")

    # ------ SEARCH --------

    p_search = sub.add_parser(
        "search",
        help="найти целое число в массиве",
        description="Ищет целое число в массиве, отсортированном по возрастанию.",
        allow_abbrev=False
    )
    p_search.add_argument("-v", "--value", required=True,
                          type=int, metavar="VALUE",
                          help=f"искомое целое число (|value| <= {MAX_SEARCH})")
    p_search.add_argument("-i", "--input", default=None, metavar="FILE",
                          help="файл с массивом по возрастанию (по умолчанию - ввод с клавиатуры)")

    return parser


# ------ ARGUMENTS --------

def parse_args(argv=None):
    """Разобрать список argv (или sys.argv) и вернуть пространство параметров."""
    return build_parser().parse_args(argv)
