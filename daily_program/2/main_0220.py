#
#
#
# wierdstring = "쀍쀩뽥뽉"
#
# print(wierdstring *10)
# print("my programmmmm")
# print(wierdstring*10)
#
# #문자열과 숫자 형변환이 되는가의 차이를 알자
# print( "1" + "1")
#
# print( 1 + "1")
# print( 1 * "1")
# print( 1 * "1")
#
#
#
from math import isnan

exam1 = "Life is too shorts, you need python!"
# 1. " "을 기준으로 스플릿 [1,2,3,4,5 ]
# a = exam1.split(" ")
# print(a)

# 2. 나눈 1을 다시 join을 이용해서 합친것
# print("".join(a))

# print("".join(exam1.split(" ")))
#
# exam2 = "오늘의 숫자는 입니다.{abc} ".format(abc="wow")
# print("we are saying {0} who say{1}".format('hi','hello'))
#
#
#
# sub1 = "python string!"
# sub2 = "an arg"
# a = "i am a %s" % sub1 #변수를 문자열로 바꾸는 포매팅 연산자
# b = "i am a {0}".format(sub1)
# print(b )    # "i am a python string!"
#
# # 필드명을 기준으로 한 포메팅
# print("Age of student {name} is {age}".format(age=43, name="경태"))
# # 오브젝트의 인덱스 혹은 키를 사용하여 포맷팅
# position = [12.5,35,90]
# print("A의 좌표는 x = {p[0]}, y={p[1]}, z={p[2]} ".format(p=position))
#
# number = 10
# day ="three"
#
# print("I ate %d apples, so I was sick for %s days." %(number, day))
#
# print("Error is %d%%." % 98)
#
# # print("%50s" % "hi")
# print("%-10sjane. " % "hi") # hi를 왼쪽정렬 하고 나머지는 공백으로 채웠다.
# print("이것은 소숫점 자리수 입니다. ")
# print("%0.4f" % 3.42134234)   #전체길이 상관없이 좌측정렬 소수점4째자리
# print("%10.4f" % 3.42134234)  #전체길이가 10개이며 오른쪽정렬 소수점네째자리
#
# print("{0:<10}".format("hi")) #왼쪽정렬
# print("{0:>10}".format("hi")) #오른쪽정렬
# print("{0:^10}".format("hi")) #가운데정렬
#
# print("{0:=^10}".format("hi"))
# print("{0:!<10}".format("hi"))
#
# y=3.42134234
# print("{0:0.4f}".format(y))
# print("{0:10.4f}".format(y))
# print("".join("abcd"))

# print("A의 좌표는 x = {p[0]}, y={p[1]}, z={p[2]} ".format(p=position))
# result = [0,1]
# print("결과는 {result[0]} , {result[1]}".format(result))


# 프로그램이 돌때 인사하고싶다.
# name = input("please typing your name ?")
# greetingMessage = f"welcome, {name} ?"

# print("A의 좌표는 x = {p[0]}, y={p[1]}, z={p[2]} ".format(p=position))

# first_value = int(input("숫자를 입력해주세요 "))
# second_value = int(input("숫자를 입력해주세요 "))

class Calc:


    def __init__(self,fir,sec):
        self.fir = fir
        self.sec = sec
        self.result = 0

    def add(self):
        print("덧셈입니다. ")
        self.result =  self.fir+self.sec
        print(self.result)

    def sub(self):
        self.result =  self.fir-self.sec

    def mul(self):
        self.result =  self.fir*self.sec

    def div(self):
        self.result = self.fir / self.sec


numbers = input("두 숫자를 입력하세요 ")
#받은 문자를 인트로 형변환 하고 그것들을 리스트에 넣는다.
my_num = numbers.split(" ")
first = int(my_num[0])
second = int(my_num[1])

print(first, type(first))

mycal = Calc(first,second)

mycal.add()
