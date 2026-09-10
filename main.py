import sys

if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print("Справка") #TODO
    sys.exit(0)

if sys.argv[1] != "solve":
    print("Ошибка: неизвестная команда")
    sys.exit(1)

if len(sys.argv) - 1 == 1:
    a = input("Введите A: ")
    b = input("Введите B: ")
    c = input("Введите C: ")
elif len(sys.argv) - 1 == 7:
    if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
        print("Ошибка: неизвестный параметр")
        sys.exit(1)

    a = sys.argv[3]
    b = sys.argv[5]
    c = sys.argv[7]
else:
    print("Ошибка: неизвестный набор параметров")
    sys.exit(1)
