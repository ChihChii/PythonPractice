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
