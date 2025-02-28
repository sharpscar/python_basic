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

a = ""
b = ""
c =[]
d={}
cnt = 0

def get_input():
    while cnt < 2:
        input_text = input("날라리 아무거나 입력해 ")
        if cnt == 0 :
            a = input_text
        elif cnt == 1:
            b = input_text
        cnt= cnt+1

# 만약 초기화 번호를 인수로 넣어보면
get_input()
print(a,b)
