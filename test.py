"""
# 參數前的*表示 num 是一個可變(動態)參數
def add(*num): 
    sum = 0
    for n in num:
        sum += n
    return sum

print(add(5))
print(add(5,2,7))
"""

"""
import from other file.py

from TempRadiusLeap import redius
redius(5)
"""
"""
f = [x for x in range(1, 10)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
"""




import os
import time
def main():
    content = 'teeeeeeeeeeeeeeeesting........'
    while True:
        # 清理畫面
        os.system('clear')  # os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
