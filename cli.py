import argparse

from calc.series import FORMULAS, MAX_EPS, MAX_TERMS
from calc.integration import FORMULAS as INTEGRATION_FORMULAS, MAX_STEPS
from calc.equation import MAX_COEFFICIENT
from calc.stats import MAX_COUNT, MAX_VALUE

# ------ PARSER --------

def build_parser():
    """Вернуть парсер команд solve, stats, series и integrate с их параметрами."""
    parser = argparse.ArgumentParser(
        prog="mathtools.py",
        description="Математический инструмент: уравнение, статистика, ряд, интеграл.",
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

    p_solve.add_argument("-a", type=str, default=None, metavar="A", help=f"коэффициент A (целое, |A| <= {MAX_COEFFICIENT})")
    p_solve.add_argument("-b", type=str, default=None, metavar="B", help=f"коэффициент B (целое, |B| <= {MAX_COEFFICIENT})")
    p_solve.add_argument("-c", type=str, default=None, metavar="C", help=f"коэффициент C (целое, |C| <= {MAX_COEFFICIENT})")

    # ------ STATS --------

    p_stats = sub.add_parser(
        "stats",
        help="статистика по последовательности чисел",
        description="Вычисляет статистические показатели последовательности "
                    f"вещественных чисел (не более {MAX_COUNT}, |x| <= {MAX_VALUE}).",
        allow_abbrev=False
    )
    p_stats.add_argument("--input", metavar="FILE", default=None, help="прочитать числа из файла (по умолчанию — с клавиатуры)")

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

    return parser


# ------ ARGUMENTS --------

def parse_args(argv=None):
    """Разобрать список argv (или sys.argv) и вернуть пространство параметров."""
    return build_parser().parse_args(argv)
