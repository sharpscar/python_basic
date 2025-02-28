'''선택구조_예제13'''
# number_ =input("정수 입력하세요 ")
# number = int(number_)
#
# if number % 2 ==0:
#     result = "짝수"
#     print(result)
# else:
#     result = "홀수"
#     print(result)

'''선택구조_예제13
    n의 배수 판별 
'''
# def is_multple_n(n):
#     if number % n ==0:
#         result = f"{n}의 배수"
#         print(result)
#     else:
#         result = f"not {n}의 배수."
#         print(result)
#
# '''선택구조_예제14'''
# number_ =input("정수 입력하세요 ")
# number = int(number_)
# is_multple_n(3)



'''선택구조_예제 15'''
# 나이에 따른 요금을 반환해줍니다.
# def calc_fee(age):
#     price = 5000
#     fee = 0
#     if age < 8:
#         fee = 0
#     if 8 <= age < 60:
#         fee = price
#     if age >= 60:
#         fee = int(price / 2)
#     return fee
#
# age =input("나이 입력하세요 ")
# age = int(age)
# fee = calc_fee(age)
# print (f"{fee}원 입니다.")

'''선택구조_예제 16'''
# def is_multple_n(n,input_number):
#     if input_number % n ==0:
#         # result = f"{n}의 배수"
#         print(input_number)
#         return True
#     else:
#         # result = f"not {n}의 배수."
#         return False

'''선택구조_예제14'''
# number_ =input("정수 입력하세요 ")
#
# input_number = int(number_)
#
# if is_multple_n(3,input_number) :
#     print(f"일단 3의 배수는 맞아요. ")
#     if is_multple_n(5,input_number):
#         print(f"3의 배수이며 5의 배수 입니다. ")
'''선택구조_예제 15'''
# 나이에 따른 요금을 반환해줍니다.
# def calc_fee(age):
#     price = 5000
#     fee = 0
#     if age < 8:
#         fee = 0
#     if 8 <= age < 60:
#         fee = price
#     if age >= 60:
#         fee = 0
#     return fee
#
# age =input("나이 입력하세요 ")
# age = int(age)
# fee = calc_fee(age)
# print (f"{fee}원 입니다.")
'''반복구조_예제 20'''

# iter_ = 10
# if iter_ <=1:
#     print (iter_)
# else:
#     for i in range(iter_):
#         print(iter_)
#         iter_ -=1
'''반복구조_예제 21'''
# sum = 0
# i = 1
# flag = True #깃발
# while flag :
#     if i <= 100:
#         sum = sum + i
#         i =  i + 1
#     else:
#         flag = False
#
# print(sum)
'''반복구조_예제 22'''
#
# i = 2
# sum = 0
# while(i<=100) :
#     sum = sum + i
#     # print(i, sum)
#     i = i + 2
# print(sum)
'''반복구조_예제 23'''
# i =2
# sum_ = 0
# while i<=100:
#     if i % 2 == 0:
#         sum_ = sum_ + i
#         print(f"i값은 {i}, sum값은 {sum_}")
#     # else:
#     #     pass # else pass 는 그저 아무것도 안하면 된다.
#     i +=1

# a = range(1,100)
#짝수가 아닌때는 그대로 리스트에 넣고 짝수인때는 *-1 해서 넣어라
# num_list = [ num if num % 2 !=0 else num * -1 for num in a ]
# print(num_list)

'''반복구조_예제 24'''
#
# sum_ = 0
# for i in range(1,101):
#
#     # 짝수인경우
#     if i % 2 == 0:
#         sum_ = sum_ - i
#     else:
#         sum_ = sum_ + i
#
# print(sum_)
'''반복구조_예제 25'''
# fact = 1
# i = 5
# for i in range(5 ,0 , -1):
#     fact = fact * i

# def facto(n):
#     if n ==1:
#         return 1
#     return n *facto(n-1)
# print(facto(5))