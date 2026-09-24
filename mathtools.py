import sys
from math import sqrt, isfinite

# ------ CONSTANTS ------

MAX_VALUE = 10000
MAX_COUNT = 20

# ------ HELPERS --------

def parseWithValidation(text):
    try:
        num = int(text)
    except:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)

    if abs(num) > MAX_VALUE:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)

    return num


def inputWithValidation(message):
    return parseWithValidation(input(message))


def parseFloatWithValidation(text):
    try:
        num = float(text)
    except ValueError:
        print("ОШИБКА: коэффициент не является числом", file=sys.stderr)
        sys.exit(1)

    if not isfinite(num) or abs(num) > MAX_VALUE:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)

    return num


def validateCount(count):
    if count < 0 or count > MAX_COUNT:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)


def formatRoot(x):
    if x == 0:
        x = 0.0

    return f"{x:.3f}"


def solve(a, b, c):
    if a == 0:
        if b != 0:
            print("Уравнение линейное")
            x = -c / b
            print(f"x = {formatRoot(x)}")
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
        print(f"x = {formatRoot(x)}")
    else:
        sqrtD = d ** 0.5
        x1 = (-b - sqrtD) / (2 * a)
        x2 = (-b + sqrtD) / (2 * a)

        print(f"x1 = {formatRoot(x1)}")
        print(f"x2 = {formatRoot(x2)}")


def readNumbers():
    count = inputWithValidation("Введите количество: ")
    validateCount(count)

    numbers = []

    for _ in range(count):
        numbers.append(parseFloatWithValidation(input()))

    return numbers


def readNumbersFromFile(path):
    try:
        with open(path) as f:
            text = f.read()
    except OSError:
        print("ОШИБКА: не удалось прочитать файл", file=sys.stderr)
        sys.exit(1)

    numbers = [parseFloatWithValidation(token) for token in text.split()]
    validateCount(len(numbers))

    return numbers


def calcStats(numbers):
    count = len(numbers)

    print(f"Количество: {count}")

    if count == 0:
        return

    total = sum(numbers)
    sqSum = sum(x * x for x in numbers)
    avg = total / count
    rms = sqrt(sqSum / count)
    variance = sqSum / count - avg ** 2
    sko = sqrt(variance)

    if count > 1:
        sampleStd = sqrt(sum((x - avg) ** 2 for x in numbers) / (count - 1))
    else:
        sampleStd = 0.0

    positives = sum(1 for x in numbers if x > 0)
    negatives = sum(1 for x in numbers if x < 0)

    print(f"Сумма: {total:.3f}")
    print(f"Ср. арифм.: {avg:.3f}")
    print(f"Сумма кв.: {sqSum:.3f}")
    print(f"Ср. кв.: {rms:.3f}")
    print(f"Дисперсия: {variance:.3f}")
    print(f"СКО: {sko:.3f}")
    print(f"Станд. откл.: {sampleStd:.3f}")
    print(f"Наименьшее: {min(numbers):.3f}")
    print(f"Наибольшее: {max(numbers):.3f}")
    print(f"Положительных: {positives}")
    print(f"Отрицательных: {negatives}")


# -------- MAIN ---------

if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print(
        """
Решение квадратного уравнения A*x^2 + B*x + C = 0
Статистика по последовательности чисел

Использование:
mathtools.py --help                       вывести эту справку
mathtools.py solve                        запросить коэффициенты у пользователя
mathtools.py solve -a A -b B -c C         взять коэффициенты из параметров
mathtools.py stats [--input FILE]         статистика по числам (ввод или файл)

Коэффициенты — целые числа по модулю не больше 10000.
Для stats: не более 20 вещественных чисел, |x| <= 10000, без NaN и бесконечностей.""")
    sys.exit(0)

if sys.argv[1] == "stats":
    if len(sys.argv) == 2:
        calcStats(readNumbers())
    elif len(sys.argv) == 4 and sys.argv[2] == "--input":
        calcStats(readNumbersFromFile(sys.argv[3]))
    else:
        print("ОШИБКА: неизвестный набор параметров", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if sys.argv[1] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

if len(sys.argv) - 1 == 1:
    a = inputWithValidation("Введите A: ")
    b = inputWithValidation("Введите B: ")
    c = inputWithValidation("Введите C: ")

elif len(sys.argv) - 1 == 7:
    if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)

    a = parseWithValidation(sys.argv[3])
    b = parseWithValidation(sys.argv[5])
    c = parseWithValidation(sys.argv[7])
else:
    print("ОШИБКА: неизвестный набор параметров", file=sys.stderr)
    sys.exit(1)

solve(a, b, c)
