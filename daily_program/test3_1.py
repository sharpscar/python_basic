#
# def solution(arr):
#     print(arr)
#     arr.sort()
#     half = len(arr)/2
#     half = str(half)
#     half = int(half.split(".")[0])
#
#     answer = arr[half]
#     return answer
#
# print(solution([1,2,7,10,11]))

'''
연속된 수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/120923

 '''
# def solution(num, total):
#     answer=[0 for i in range(num)]
#
#     total_ = 0
#     for i in range(-100,200):
#
#         # num의 크기만큼  돌아라
#         for j in range(num): # j는 0 1 2
#
#             answer[j]=(i+j)
#         # list의 크기가 3이상이면 넘겨라
#         total_ = sum(answer)
#         if total_ == total :
#             return answer
#
#
#     return answer
#
# r = solution(5,5)
#
# print(r)

def solution(numlist, n):
    answer = []
    # 만약 주어진 배열의 갯수가 짝수개일땐 0요소를 추가해준다. 그리고 모든 작업이 끝나면 제거한다.
    if len(numlist) % 2 == 0:
        numlist.append(0)
    n_index = numlist.index(n)
    increase_index = [i for i in range(1,len(numlist)-n_index)]
    max_increase=len(numlist)-n_index-1

    for i in range(max_increase):
        # print(f"i값은         {i}")
        #기준이 되는 인덱스 보다 +1 인 인덱스의 값을 가져온다
        index_=n_index + increase_index[i]
        n1 = numlist[index_]
        index_ = n_index - increase_index[i]
        n2 = numlist[index_]
        print(n1,n2)
        #n과 n1 과의 차이와 n과 n2와의 차이를 비교하여 작은 값을 먼저 넣는다 만약 차이가 없다면 큰숫자가 먼저들어간다.
        r1 = n1 - n
        # print(f"r1값은 {r1}")
        r2 = n - n2
        # print(f"r2값은 {r2}")
        if r1<= r2 :
            answer.append(n1)
            answer.append(n2)
        else:
            answer.append(n2)
            answer.append(n1)

        # 2가지 작업을 해줘야한다. 1. 4를 앞에 넣는다. 2. 0을 제거한다.
    answer.insert(0,n)
    answer.remove(0)
    return answer


r = solution([10000,20,36,47,40,6,10,7000],30)
print(r)