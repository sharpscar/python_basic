'''

python function을 학습하고
자유자재로 function을 사용할수 있다.

InAndOut(햄버거아님) or InAndProcess or just doSomething


minus

multiple

division



'''
import math
def add(a,b):
    # 입력값 검증
    c = sum((a,b))
    ''''
    # sum(a, b) 하면 
    int' object is not iterable 
    오류가 발생하는데 왜일까? 
    '''
    return c


def minus(a,b):
    # 추후 둘중에 큰값을 판별하여 큰값에서 작은값을 빼게 만들수도
    c =a -b

    return c

def multiple(a,b):
    c = a*b
    return c

def division(a,b):
    if b < 1:
        print("0으로 나눌수 있는 수는 지구상에 존재하지 않습니다. \n두번째 값을 1로 변경합니다. ")
        b = 1
    c = a/b
    c = math.floor(c)
    return c

a = division(1,0)
print(a)