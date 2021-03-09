from time import sleep
import os


class clock (object):
    def __init__(self, hour=0, min=0, sec=0):
        self._hour = hour
        self._min = min
        self._sec = sec

    def run(self):
        self._sec += 1
        if(self._sec == 60):
            self._sec = 0
            self._min += 1
        if(self._min == 60):
            self._min = 0
            self._hour += 1
        if(self._hour == 24):
            self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._min, self._sec)


def main():
    watch = clock(10, 30, 1)
    while(1):
        os.system('clear')
        print(watch.show())
        sleep(1)
        watch.run()


if __name__ == '__main__':
    main()
