'''
dict를 사용해보자
'''
from main import solution

#
# data = {
#     "main":[10,3,5,5,5,5,10,5,2,100],
#     "goblin":[3,0,1,1,1,1,2,1,0,5]
# }
# status = {
#     "mp":0,
#     "str":0,
# "dex":0,
# "int":0,
# "luk":0,
# "damage":0,"magic_damage":0,"protext":0
#
# }
# char_ ={}
#
# for k, v in data.items():
#     tmp_dict = status.copy()
#
#     for idx, k_ in enumerate(status.keys()):
#         tmp_dict[k_] = v[idx]
#
#     char_[k] = tmp_dict
# print(char_)


# 목표 = [1,2,3,4,5,6,7,8,9,10]

'''예제 37'''
# range를 대신할 함수 증감까지 구현하면 참좋겠다.
def my_r(init,n):
    l = []
    i = init
    while(i<n+1):
        l.append(i)
        i= i+1
    return l
'''
예제 44
10진수를 2진수로 변환하기 

2진수 : binary number
8진수 :octal number
10진수 :decimal number
16진수 :hexadecimal

'''








'''
예제 43 에라토스테네스의 체 (선택 문제)
'''
# def remove_from_list(start, list_):
#     answer = []
#     for i in list_:
#         if i % start != 0:
#             answer.append(i)
#     return answer
#
#
# def solution():
#     hundred = my_r(2,100)
#     answer = []
#     answer_2 = remove_from_list(2,hundred)
#     answer_3 = remove_from_list(3, answer_2)
#     answer_5 = remove_from_list(5, answer_3)
#     # 에라토스테네스의 체는 2,3,5는 체로 걸르는 알고리즘이다. 그러므로 이런 편법은 봐주자
#     pre = [2,3,5]
#     return pre+answer_5
#
# r = solution()
# print(r)



'''
예제 42 리스트 요소중 최댓값 구하기 
'''
# def solution(arr):
#     max_ = arr[0]
#
#     for i in arr:
#
#         if max_ < i :
#             max_ = i
#
#
#     return max_
#
# l = [91,90,78,35,65,9,97,54,62,90]
# r = solution(l)
# print(r)
'''
예제 41

'''
# def solution():
#     a = my_r(1,10)
#     # t = [0 for i_ in a]
#
#     t = a[0]
#     for i in range(9):
#         a[i]= a[i+1]
#     a[9] = t
#     return a
# r = solution()
# print(r)

'''
예제 40
리스트를 뒤집은 내용을 출력하라 .
'''
# def solution(init, n):
#     l = []
#     a = my_r(init, n)
#     b = [0 for i_ in a]
#     # print(b)
#     for i in range(len(a)):
#         b[i] = a[9-i]
#     return b
# r = solution(1,10)
# print(r)

'''
예제 39
리스트 요소 거꾸로 뒤집기 
'''
#
# def solution(init, n):
#     l = []
#     l = my_r(init,n)
#     a = my_r(1,10)
#
#     t = [0 for i_ in a] # out of range 오류 방지 초기화
#
#     for i  in l:
#         t[i] = a[9-i]
#         a[9-i] = a[i]
#         a[i] = t[i]
#     print(a)

# r = solution(0,4)

#
# ten = my_r(1,10)
# a =[i for i in (ten)]
#
# print(a)
'''
예제 38
init 부터 n까지 증가하는 리스트를 반환한다는 .. my_r
'''
# def solution(init,n):
#     l=[]
#     l_=[]
#     r_l=[]
#     l = my_r(init,n)
#
#     for i in l:
#         # l_[i].append(i*10)  리스트의 i로 접근하면 index out of range라는 에러를 만날 확률이 굉장히 높다.
#         l_.append(i*10)
#     print(l_)
#     # l_가 [10,20,30,40,50,60,70,80,90,100]
#     # 배열을 역순으로 바꾼다.
#     r = reversed(l)
#     for j in r:
#         r_l.append(j*10)
#     # r_l이  [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]
#     print(r_l)
#
# my_l = solution(1,10)
