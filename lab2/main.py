from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import sys

def get_side_rad(prompt="Введите значение стороны"):
    print(prompt)
    side_str = input()
    while True:
        try:
            side = float(side_str)
        except:
            print("Введены неправильные данные.")
            side_str = input()
        else:
            return side


def get_color(termpt):
    print("Введите цвет будущего", termpt)
    return str(input())


def main():
    print("Выберете тип ввода:\n1 - с клавиатуры \n2 - по умолчанию")
    while True:
        choise = int(input())
        if choise == 1 or choise == 2:
            break
        else:
            print("Введено неверное значение. Введите 1 или 2")

    if choise == 1:
        r = Rectangle(get_color("прямоугольника"), get_side_rad(), get_side_rad())
        c = Circle(get_color("круга"), get_side_rad("Введите радиус"))
        s = Square(get_color("квадрата"), get_side_rad())
        print(r, c, s, sep="\n")
    else:
        print(Rectangle("синего", 3, 3))
        print(Circle("зеленого", 3))
        print(Square("красного", 3))


if __name__ == "__main__":
    main()