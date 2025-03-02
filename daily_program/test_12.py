

#함수
def input_(max_):
    a = int(input("첫번째 값을 입력하세요 (정수)"))

    if a > max_:
        max_ = a
    return max_


f = int(input("첫번째 값을 입력하세요 (정수)"))

max_1 = f

max_1 = input_(max_1)
max_1 = input_(max_1)


# a = int(input("첫번째 값을 입력하세요 (정수)"))
#
# if a>max :
#     max = a

# a = int(input("첫번째 값을 입력하세요 (정수)"))
#
# if a>max :
#     max = a


print(max)

