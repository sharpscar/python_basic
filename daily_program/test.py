'''
class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |

'''
from curses.ascii import isdigit

#
# def my_num(num):
#
#     for i in range(num) :
#         if i % 2 == 0 :
#
#
#     return r

a = [1,2,3]
b = 0
c = 0
d = 0



a = input("첫번째 변수를 입력하세요")
# b = input("두번째 변수를 입력하세요")

if not a.isdigit :
    print("재입력하세요 숫자를 넣어야 합니다.")
    input()
elif int(a) < 0:
    print("재입력하세요 양수를 넣어야 합니다.")
    input()
else:
    a = int(a)
    c = a*a*3.14

print(f"원의 면적은  {c} 입니다.")

