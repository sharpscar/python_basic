'''addition of fractions
분수의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/120808

입출력 두개는 통과하지만 문제는 틀렸다 추후 다시 풀어보는걸로
'''
#
# # 9,2,1,3
#
# def solution(numer1, denom1, numer2, denom2):
#     #분모끼리 같지 않으면 곱
#     if denom1 != denom2 :
#        denom = denom1 * denom2 # 분모를 곱하여 통분
#        numer1 = numer1 * denom2 # 분자1의 값을 구함 1 * 4
#        numer2 = numer2 * denom1 # 분자 2의 값을 구함 2 * 3
#     else:
#         denom = denom1
#
#     numer = numer1 + numer2
#     # 원래 약분할 약수를 먼저 구하는게 아니라 소수인지 아닌지 판별이 우선이지만 약수가 있는지 체크하려면 먼저 약수들을 구해봐야 아니까..
#     denom_list = get_div(denom) #분모의 약수를 구함
#     numer_list = get_div(numer) #분자의 약수를 구함
#     '''
#      약분하는 부분
#      분모나 분자가 소수인경우 약분할 필요 없다. 소수 구하는 방법? 만약 get_div()함수를 거쳤으나 빈 리스트가 나온경우
#     분기문  - 분모가 소수거나 분자가 소수이면 약분을 할수가 없으니 그냥 대답에 리스트형식으로 넣음
#             분모와 분자 둘중에 하나라도 소수가 아니면
#     '''
#     if len(denom_list) != 2 and len(numer_list) != 2:
#         # 소수인경우에 이쪽분기로 오면 에러를 뱉을수밖에 없다 0으로 나눌거거든
#         measure = 0
#         del denom_list[-1]
#         del denom_list[0]
#         del numer_list[-1]
#         del numer_list[0]
#
#         for i in denom_list:
#             if i in numer_list:
#                 measure = i
#
#         answer = [int(numer / measure), int(denom / measure)]
#     else:
#         answer = [int(numer), int(denom)]
#     return answer
#
#
#
#
# #약수 구하는 함수
# def get_div(n):
#     divi = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             divi.append(i)
#
#     return divi

# r = solution(7,5,2,3)
# print(r)
#
# def solution(numbers):
#     answer =[i *2 for i in numbers]
#     print(answer)
#     answer = []
#     return answer
#
# solution([1,2,3,4,5,6])
#
# def my_def(n1,n2):
#     my_list=[]
#     for i in range(n1,0,-1):
#         if n1 % i ==0 and n2 % i ==0:
#             my_list.append(i)
#     result = max(my_list)
#     return result
#
# r = my_def(12,16)
# print(r)
# def my_fun(n):
#     # my_dick = {}
#
#     for i in range(2,n-1):
#         if n % i == 0:
#             str_ = f'{n}는 소수가 아닙니다.'
#
#         else:
#             str_ = f'{n}는 소수 입니다.'
#
#     return str_
#
# a = my_fun(7)
# print(a)
#
# def pivonachi():
#
#     a = 1
#     b= 1
#     m_l = [a,b]
#     for i in range(100):
#         c=a+b
#         a=b
#         b=c
#         # c = a + b
#
#         m_l.append(c)
#     return m_l
# l = pivonachi()
# print(l)
#
# def find_max(l):
#     max_ = 0
#     for i, val in enumerate(l):
#         print(f"정수 : {val}")
#
#         if max_ < val:      # 내가 근데 이상하게  max_ > val면  max_ = val 하라 라고 써놓고 왜안되지? 하며 고뇌했다.
#             max_ = val
#     return max_
#
# r = find_max([5,7,30,9,8,0])
# print(f"최대값 {r}")

# def my_func(n):
#     m_l=""
#     for i in range(1,n):
#         m_l += str(i)
#         print(m_l)
#
# my_func(6)

'''
임의의 수를 나누었을 때 나누어떨어지게 하는 수를 약수라 한다.
즉, n의 약수는 1부터 n까지의 수로 n을 나누어떨어지게 하는 수가 된다.
예를 들면, 10의 약수는 1부터 10까지 수들로 나누었을 때 나머지가 0이 되게 하는 수, 즉 1, 2, 5, 10이 된다.
'''
# 약수
# def means(n):
#     mean_list=[]
#     for i in range(1,n+1):
#         if n % i ==0 :
#             mean_list.append(i)
#     return mean_list
#
# for i in range(1,11):
#     m = means(i)
#     print(f"{i}의 약수{m}.")

# 예제 29 ->34
# def my_fun(n):
#     measure_list = []
#     for i in range(2,n):
#         if n % i == 0:
#             #나누어 떨어지기때문에 소수가 아님 (약수
#             measure_list.append(i)
#     if len(measure_list) == 0:
#         return n
#
# for i in range(2,101):
#     answer = my_fun(i)
#     if answer is not None:
#         print (answer, end=" ")

def my_sol():
    s = 1
    n = 1

    for i in range (1,11):
        if i == 1:
            pass
        else:
            n = n+i
            s = s+n
        #만약에 숫자를 저장하지 않고 문자열로 수식을 저장한다면?
        # n = str(i) + "+"+ n
        # s = n + "+" + s
        # print(" i는 ",i ,"       ", end="")
        # print(n, end="")
        # print("     "+s)


    print(s)


my_sol()
#
# def my_sol():
#
#     for i in range(2,10):
#         # 다다단!
#
#         print("# ",end="")
#         for j in range(1,10):
#             print(f"{i} x {j} = {i*j}", end="\t")
#         print()
#
# my_sol()