'''
최빈값 구하기
배열이 주어진다. 주어진 배열에서 제일 자주 나온 값을 출력하는 문제
최빈값이 2이상이면 -1을 리턴한다.
내가 직접 풀진 못했다.
https://jimmy-ai.tistory.com/217
이 자료를 참조했다. 여기선 x, new_a 두 배열을 사용해서
x에 최초 발견된 요소를 넣고 new_a에는 적어도 2번이산 만나게 되는 요소를 저장한다.
그럼 new_a의 크기만 가지고도 중복되는 값이 몇개인지 체크가 가능하다.
'''
#
# arr = [1,1,2,2]
# #v와 arr[i]는 같은 말이야.
#
# def solution(array):
#     x = [] # 처음 나온 요소
#     new_a = [] # 중복된 요소
#
#     for i in array:
#         if i not in x:
#             x.append(i)
#         else:
#             if i not in new_a:
#                 new_a.append(i)
#
#     if len(new_a)==0:
#         return x.pop()
#     if len(new_a)>=2:
#         return -1
#     return new_a.pop()

'''
n 매개변수 1부터 n까지 홀수만 출력해라
'''
# def solution(n):
#     hol = []
#     for i in range(n+1):
#         if i % 2 ==0:
#             pass
#         else:
#             hol.append(i)
#
#     return hol
#
# l = solution(15)

'''
OX퀴즈
'''
# def solution(quiz):
#     answer =[]
#     result = 0
#     for i,q in enumerate(quiz):
#         ex = q.split(" ")
#         print(ex)
#         if ex[1]== "-":
#             result = int(ex[0]) - int(ex[2])
#         if ex[1]== "+":
#             result = int(ex[0]) + int(ex[2])
#         if ex[1]== "*":
#             result = int(ex[0]) * int(ex[2])
#         if ex[1]== "/":
#             result = int(ex[0]) / int(ex[2])
#         if result != int(ex[4]):
#             answer.append("X")
#         if result == int(ex[4]):
#             answer.append("O")
#     return answer
# quiz = ["3 - 4 = -3", "5 + 6 = 11"]
# r = solution(quiz)
# print(r)












