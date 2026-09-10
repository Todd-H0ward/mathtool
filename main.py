import sys

# ------ HELPERS --------

def inputWithValidation(message):
    try:
        num = int(input(message))
    except:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)

    return num


def solve(a, b, c):
    if a != 0:
        return

    if b != 0:
        print("Уравнение линейное")
        x = -c / b
        print("x = {:.3f}".format(x))
    else:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)
    return

# -------- MAIN ---------

if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print("Справка") #TODO
    sys.exit(0)

if sys.argv[1] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

if len(sys.argv) - 1 == 1:
    a = inputWithValidation("Введите A: ")
    b = inputWithValidation("Введите B: ")
    c = inputWithValidation("Введите C: ")

    if abs(a) > 10000 or abs(b) > 10000 or abs(c) > 10000:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)


elif len(sys.argv) - 1 == 7:
    if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)

    a = sys.argv[3]
    b = sys.argv[5]
    c = sys.argv[7]
else:
    print("ОШИБКА: неизвестный набор параметров", file=sys.stderr)
    sys.exit(1)

solve(a, b, c)
