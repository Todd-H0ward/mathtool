import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtools.py",
        description="Математический инструмент: уравнение, статистика, ряд, интеграл.",
    )
    sub = parser.add_subparsers(dest="command")

    p_solve = sub.add_parser(
        "solve",
        help="решить уравнение A·x²+B·x+C=0",
        description="Решение квадратного или линейного уравнения A·x²+B·x+C=0. "
                    "Коэффициенты — целые числа |x| <= 10000.",
    )
    p_solve.add_argument("-a", type=str, default=None, metavar="A",
                         help="коэффициент A (целое, |A| <= 10000)")
    p_solve.add_argument("-b", type=str, default=None, metavar="B",
                         help="коэффициент B (целое, |B| <= 10000)")
    p_solve.add_argument("-c", type=str, default=None, metavar="C",
                         help="коэффициент C (целое, |C| <= 10000)")

    p_stats = sub.add_parser(
        "stats",
        help="статистика по последовательности чисел",
        description="Вычисляет статистические показатели последовательности "
                    "вещественных чисел (не более 20, |x| <= 10000).",
    )
    p_stats.add_argument("--input", metavar="FILE", default=None,
                         help="прочитать числа из файла (по умолчанию — с клавиатуры)")

    sub.add_parser(
        "series",
        help="вычислить сумму ряда",
        description="Вычисляет сумму математического ряда.",
    )

    sub.add_parser(
        "integrate",
        help="численное интегрирование",
        description="Вычисляет определённый интеграл методом численного интегрирования.",
    )

    return parser


def parse_args(argv=None):
    return build_parser().parse_args(argv)

