import math


def FtoC(f):
    c = (f - 32) / 1.8
    print('Du F = %.1f' % int(c))


def redius(r):
    perimeter = 2 * r * math.pi
    area = (r**2) * math.pi
    print('perimeter: %.1f' % perimeter)
    print('area: %.1f' % area)


def isLeap(y):
    is_leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    print(is_leap)


def main():
    option = int(
        input('1. FtoC\n2. radius\n3. IsLeap\nPlease choose the option !\nOption : '))

    if (option == 1):
        c = float(input('Du C = '))
        FtoC(c)
    elif (option == 2):
        r = float(input('radius = '))
        redius(r)
    elif (option == 3):
        year = int(input('year = '))
        isLeap(year)
    else:
        print('no this option la !')


if __name__ == '__main__':
    main()
