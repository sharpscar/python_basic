'''
반복문 두개의 차이

    1. for   - 종료시점을 알때 길이가 고정적일때
    2. while - [종료시점을 모른다. ] 언제끝날지 모르는 구동간 멈출수 있는 그게 언제일지 모르는 작업을 할때 /

'''
'''0부터 99까지 출력하세요'''
# count = 0
# while count < 100:
#     print(count)
#     count+=1 # count = count+1

''' 1부터 100까지 출력하세요 홀수만 ver1 
문자 그대로 홀수만 출력해라  3번의 연산이 필요 3 * n
현실은 반복대상이 랜덤 (무작위)의 경우가 더 많다. 그래서  ver1의 사용빈도가 더 높을것이다. 
'''
# count = 0
# count2 = 0
# while count <100 :
#     count+=1
#     if count % 2 == 1:
#         print(count)
''' 1부터 100까지 출력하세요 짝수만 ver2  2씩증가하면 짝수가 나올수밖에 없다.  1번의 연산만으로 가능 1/2* n '''
# while count2 <100:
#     count2 += 2
#     print(count2)

# for i in range(1,11):
#     print(i)
# print(list(range(1,11)))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in my_list :
#     print(i)

# print(list(range(0,206,12)))
# for i in range(10):
#     print(i)
# print("===========")
# for i in range(0,10):
#     print(i)
# print("===========")
# for i in  range(0,10,1):
#     print(i)
# print("===========")
#
# total = 10
# ran = range(total)
# i =0
# while i< total:
#     print(ran[i])
#     i = i+1
#
# total =10
# set_ =set(range(total))
# i = 0
# while i< total:
#     print(set_[i])
#     i +=1

# '''반복문의 인덱스에 접근할수 있다. '''
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for idx in range(len(arr)):
#     print(idx, arr[idx])
#
# '''정확히 위 코드와 동일하게 동작한다. '''
# for idx, val in enumerate(arr):
#     print(idx, val)

'''
0 부터 100 까지 출력하는 3가지 버전
짝수만  
'''

#1
#
# for i in range(1,101,1):
#     if i % 2 == 0:
#         print(i)
# print("===============")
#
# #2
# for i in range(2, 101, 2):
#     print(i)

#3
# for i in range(0,101):
#     if i%2 !=0 :
#         continue
#         # break
#     print(i)

''' continue or break 를 활용해보아라 '''

'''
    만약 자판기의 경우 항상 켜져있어야 하니까 True 구문을 넣는다
        
        finish_purchase = 손님의 물건 구매가 끝났을 경우 continue 
        empty_drink 재고가 떨어졌을 경우 break

'''
