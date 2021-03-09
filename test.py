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
"""#跑馬燈
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
"""

"""
class Student (object):

    # __init__是一個特殊方法用於在創建對象時進行初始化操作
    # 通過這個方法我們可以為學生對象綁定name和age兩個屬性
    def __init__(self, name, age):
        self . name = name
        self . age = age

    def study(self, course_name):
        print('%s正在學習%s.' % (self . name, course_name))

    # PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
    # 但是部分程序員和公司更傾向於使用駝峰命名法(駝峰標識)
    def watch_movie(self):
        if self . age < 18:
            print('%s只能觀看《熊出沒》.' % self . name)
        else:
            print('%s正在觀看島國愛情大電影.' % self . name)


def main():
    # 創建學生對象並指定姓名和年齡
    stu1 = Student('駱昊', 38)
    # 給對象發study消息
    stu1 . study('Python程序設計')
    # 給對象發watch_av消息
    stu1 . watch_movie()
    stu2 = Student('王大錘', 15)
    stu2 . study('思想品德')
    stu2 . watch_movie()


if __name__ == '__main__':
    main()
"""




from  time  import  sleep
class  Clock (object ):
     """數字時鐘"""

    def  __init__ ( self , hour = 0 , minute = 0 , second = 0 ):
        self._hour  =  hour 
        self . _minute  =  minute 
        self . _second  =  second

    def  run ( self ):
         """走字""" 
        self . _second  +=  1 
        if  self . _second  ==  60 :
            self . _second  =  0 
            self . _minute  +=  1 
        if  self . _minute  ==  60 :
            self . _minute  =  0 
            self . _hour  +=  1 
        if  self . _hour  ==  24:
            self . _hour  =  0

    def  show ( self ):
         """顯示時間""" 
        return  '%02d:%02d:%02d'  % \
               ( self . _hour , self . _minute , self . _second )


def  main ():
     clock  =  Clock ( 23 , 59 , 58 )
     while  True :
         print ( clock . show ())
         sleep ( 1 )
         clock . run ()


if  __name__  ==  '__main__' :
     main ()
