import datetime
import time
import os
import random

list_ = []
print()

for i in range(6) :
    number = random.randint(1, 46)
    list_.append(number)

random.shuffle(list_)
print(list_)

lotto = random.sample(list_,6)
print(sorted(lotto))


while False:
    str_ =''
    now = datetime.datetime.now()
    str_ = f"{now.year}년{now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초 {now.microsecond}밀리초"
    print(str_)

    time.sleep(0.1)