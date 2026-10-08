import argparse

from calc.series import FORMULAS, MAX_EPS, MAX_TERMS

def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtools.py",
        description="Математический инструмент: уравнение, статистика, ряд, интеграл.",
        allow_abbrev=False
    )
    sub = parser.add_subparsers(dest="command")

    p_solve = sub.add_parser(
        "solve",
        help="решить уравнение A·x²+B·x+C=0",
        description="Решение квадратного или линейного уравнения A·x²+B·x+C=0. "
                    "Коэффициенты — целые числа |x| <= 10000.",
        allow_abbrev=False
    )

    p_solve.add_argument("-a", type=str, default=None, metavar="A", help="коэффициент A (целое, |A| <= 10000)")
    p_solve.add_argument("-b", type=str, default=None, metavar="B", help="коэффициент B (целое, |B| <= 10000)")
    p_solve.add_argument("-c", type=str, default=None, metavar="C", help="коэффициент C (целое, |C| <= 10000)")

    p_stats = sub.add_parser(
        "stats",
        help="статистика по последовательности чисел",
        description="Вычисляет статистические показатели последовательности "
                    "вещественных чисел (не более 20, |x| <= 10000).",
        allow_abbrev=False
    )
    p_stats.add_argument("--input", metavar="FILE", default=None, help="прочитать числа из файла (по умолчанию — с клавиатуры)")

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

    sub.add_parser(
        "integrate",
        help="численное интегрирование",
        description="Вычисляет определённый интеграл методом численного интегрирования.",
        allow_abbrev=False
    )

    return parser


def parse_args(argv=None):
    return build_parser().parse_args(argv)
