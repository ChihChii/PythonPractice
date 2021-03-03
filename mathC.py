def times(t):
    sum = 1
    for i in range(1, t+1):
        sum *= i
    return sum


def main():
    m = int(input('m : '))
    n = int(input('n : '))
    res = times(m) / (times(n)*times(m-n))
    print('Res : ', res)


if __name__ == '__main__':
    main()
