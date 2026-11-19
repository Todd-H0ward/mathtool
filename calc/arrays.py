import sys, random

# ------ CONSTANTS -------

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

# ------- HELPERS --------

def read_array(path):
    """Прочитать массив из файла или stdin и проверить числа и размер."""
    if path:
        with open(path, encoding="utf-8-sig") as file:
            text = file.read()
    else:
        lines = []
        for line in sys.stdin:
            if not line.strip():
                break
            lines.append(line)
        text = " ".join(lines)

    text = text.replace(",", " ").split()
    numbers = []
    for word in text:
        try:
            number = int(word)
        except ValueError:
            raise ValueError(f"{word} не является целым числом") from None
        numbers.append(number)

    if not 1 <= len(numbers) <= MAX_COUNT:
        raise ValueError(f"количество элементов должно быть от 1 до {MAX_COUNT}")
    for number in numbers:
        if not MIN_VALUE <= number <= MAX_VALUE:
            raise ValueError(f"значения должны быть от {MIN_VALUE} до {MAX_VALUE}")

    return numbers


def write_array(numbers, path):
    """Записать готовый массив одной строкой в файл UTF-8 или stdout."""
    text = " ".join(str(number) for number in numbers)
    if path:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text + "\n")
    else:
        print(text)

def fill(count, low = MIN_VALUE, high = MAX_VALUE, seed = ""):
    random.seed(seed)
    list = []

    for _ in range(count):
        list.append(random.randint(low, high))

    return list
