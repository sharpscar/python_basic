import random
ran_list = []
# 랜덤 정수 3개 리스트 생성
num = set()
# 3개의 숫자가 중복되지 않도록 생성
while len(num)<3:
    num.add(random.randint(1,9))
ran_list = list(num)

def get_input():
    user_input = input("3개의 숫자를 ,로 띄어서 입력해줘요>>  ")
    user_input_list = user_input.split(",")
    if len(user_input_list) > 4:
        print("사용자의 입력이 4개 이상입니다. ")
    for i in range(len(user_input_list)) :
        user_input_list[i] = int(user_input_list[i])
    return user_input_list

print(ran_list)

# 사용자 입력을 10회 받는다 입력은 정수 정수 정수 형식
for i in range(10):
    user_input_list = get_input()
# 각 입력받은 값들을 생성한 랜덤생성한 숫자배열 과  비교
    strike = 0
    ball = 0
    # 해당 위치와 해당 값이 일치하면 스트라이크  #다른위치에 값이 일치하면 볼
    # 랜덤 0번째와 유저인풋 0번째가 같으면 스트라이크 +1
    for i in range(len(ran_list)):
        for j in range(len(user_input_list)):

            # i 와 j 가 인덱스가 같고 값이 같은경우 스트라이크 +1  i 와 j의 인덱스가 다르고 값이 같은경우는 볼 +1
            if i == j:
                if ran_list[i] == user_input_list[j]:
                    strike = strike + 1
            else:
                if ran_list[i] == user_input_list[j]:
                    ball = ball + 1


    #만약 스트라이크가 3이상인경우 게임 중지
    if strike ==3:
        print("3진아웃 입니다. You win")
        break

    print("strike는 {},ball은 {} ".format(strike, ball))




get_input()


