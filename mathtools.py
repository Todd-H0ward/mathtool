import sys

# ------ CONSTANTS ------

MAX_VALUE = 10000

# ------ HELPERS --------

def inputWithValidation(message):
    try:
        num = int(input(message))
    except:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)

    return num


def solve(a, b, c):
    if a == 0:
        if b != 0:
            print("Уравнение линейное")
            x = -c / b
            print(f"x = {x:.3f}")
        else:
            print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
            sys.exit(1)
        return

    print("Уравнение квадратное")

    d = b ** 2 - 4 * a * c

    print(f"D = {d}")

    if d < 0:
        print("Действительных корней нет")
    elif d == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        sqrtD = d ** 0.5
        x1 = (-b - sqrtD) / (2 * a)
        x2 = (-b + sqrtD) / (2 * a)
        
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")

# -------- MAIN ---------

if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print(
        """
Решение квадратного уравнения A*x^2 + B*x + C = 0

Использование:
main.py --help                       вывести эту справку
main.py solve                        запросить коэффициенты у пользователя
main.py solve -a A -b B -c C         взять коэффициенты из параметров

Коэффициенты — целые числа по модулю не больше 10000.""")
    sys.exit(0)

if sys.argv[1] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

if len(sys.argv) - 1 == 1:
    a = inputWithValidation("Введите A: ")
    b = inputWithValidation("Введите B: ")
    c = inputWithValidation("Введите C: ")

    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
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
