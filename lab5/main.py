import sys
import math


def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Обрабатываем неправильный ввод
    while True:
        try:
            coef = float(coef_str)
        except:
            print("Введены неправильные данные.", prompt)
            coef_str = input()
        else:
            return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root >= 0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        if root1 >= 0:
            if root1 == 0:
                result.append(root1)
            else:
                result.append(math.sqrt(root1))
                result.append(-math.sqrt(root1))
        root2 = (-b - sqD) / (2.0 * a)
        if root2 >= 0:
            if root2 == 0.0:
                result.append(root2)
            else:
                result.append(math.sqrt(root2))
                result.append(-math.sqrt(root2))
        result = set(result)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней', end=" ")
        return
    elif len_roots == 1:
        print('Один корень:', end=" ")
    elif len_roots == 2:
        print('Два корня:', end=" ")
    elif len_roots == 3:
        print('Три корня:', end=" ")
    else:
        print('Четыре корня:')
    print(*roots, sep=", ")


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()