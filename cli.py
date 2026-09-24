import argparse


def build_parser():
    parser = argparse.ArgumentParser(prog="mathtools.py", add_help=True)
    sub = parser.add_subparsers(dest="command")

    p_solve = sub.add_parser("solve")
    p_solve.add_argument("-a", type=str, default=None, metavar="A")
    p_solve.add_argument("-b", type=str, default=None, metavar="B")
    p_solve.add_argument("-c", type=str, default=None, metavar="C")

    p_stats = sub.add_parser("stats")
    p_stats.add_argument("--input", metavar="FILE", default=None)

    sub.add_parser("series")
    sub.add_parser("integrate")

    return parser


def parse_args(argv=None):
    return build_parser().parse_args(argv)
