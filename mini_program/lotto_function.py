import random
import time
'''
로또 자동 만들기

1. 로또기본기능 그대로 유지
=> 번호 개수 , 등수, 당첨금은 동일


2. 회차별 컴퓨터가 로또 당첨번호를 자동으로 생성

3 번호 6개 선택 [사용자 입력 ]

4 당첨금 보여준다.
    1등은 20억
    2등 5천마원
    3등 150만원

6  1회차 게임이 끝나면 게임이 끝난다.

7 자동이라는 선택지가 있는데 (엔터?)
누르면 다음회차 진행한다. <1등 당첨직전까지 >

8 사용자가 입력한 로또번호를 기록하여 남긴다.

9 랜덤 쓰되 sample쓰지마라 .

10 로또 번호 출력시 오름차순
# 중복체크

리팩터링에 삭제한 프로퍼티
str_

'''

lotto_num_dict = {}
buyer_num_dict = {}
cnt = 1                                     #로또의 회차 번호
auto_generate_random_number=True
duplication_cnt = 0                         #사용자 입력검증 입력된숫자가 중복되었다면 +1
                     # 유효성 검증이 통과되었다면 기대값  [int,int,int,int,int,int]


'''
일단 입력을 계속 받아 until user_list의 크기가 6이 될때까지
false 일때 벗어난다 - 받은 입력이  list [int,int, int,int,int, int] 을 만족하면 조건 변수에 false를 입력하겠다. validation_list
각 검증에 실패했을땐 user_list를 초기화한다.  
'''
def get_input():
    validation_list = True
    user_input_list = []

    while validation_list:
        input_str = input("로또번호 하나씩 입력해주세요 ")

        # 입력값이 숫자가 가능한지?
        if input_str.isdigit():
            input_int = int(input_str)

            # 입력값의 범위가 0 <값 <46
            if 0 < input_int < 46:
                user_input_list.append(input_int)
                print(f"입력하신 번호는 {user_input_list}입니다.")
            else:
                print("1~45까지의 숫자만 입력 해야합니다 다시입력하세요 ")
                user_input_list = []
        else:
            print("입력형식을 확인하세요  다시 입력 하세요")
            user_input_list = []

        # 입력받은 값 중복 체크
        if len(user_input_list) < 6:
            for i in user_input_list:
                # print(f"유저 입력의 갯수는 {len(user_input_list)}",type(i))
                duplication_cnt = user_input_list.count(i)
                if duplication_cnt > 1:
                    print("중복된값이 있습니다 다시입력하세요")
                    user_input_list = []

        else:
            # 인트로 배열을 6개 채웠을때
            validation_list = False
        # 값의 범위
    return user_input_list



user_input_list = get_input()

#입력 값 검증 입력값이 1~45까지만 가능하다 음수 안되고 소수점 안되고

print(f"넣은 번호는 {user_input_list}입니다.")
auto_ = input("자동을 돌리시겠습니까? y/n")
auto_ = auto_.lower()

if auto_ =="y":
    auto_ = True
else:
    auto_ = False

# 자동적으로 난수를 생성할지 :auto_generate_random_number
def print_out(lotto_num_dict,atari_num):
    print(f"{cnt}회차 번호{lotto_num_dict[cnt][0]} 입니다.|보너스번호는 {lotto_num_dict[cnt][1]}입니다. ")
    print(f"구매하신 번호는 {user_input_list} / 같은 숫자 번호 {atari_num}개 입니다,  ")


while auto_generate_random_number :
    # 컴퓨터 랜덤 넘버 생성 6+1
    lotto = (list(range(1,46)))
    random.shuffle(lotto)
    lotto_num = lotto[0:6]
    lotto_bonus = lotto[-1]
    lotto_num.sort()
    lotto_num_dict[cnt] = [lotto_num , lotto_bonus]
    buyer_number = user_input_list
    atari_num = [6,5,4,3]
    #구매자 번호를 딕션에 넣는다.
    buyer_num_dict[cnt] = buyer_number

    if auto_:

        # 유저번호가 6개 일치 1등, 보너스 1개가 일치하고 유저 번호 5개가 동일하다면 2등  유저번호 5개만 동일하다면 3등
        if len(set(lotto_num_dict[cnt][0]).intersection(buyer_number)) == atari_num[0] :
            print_out(lotto_num_dict,atari_num[0])
            str_ ="로또  1등 20억당첨입니다."
            print(str_)
            exit()
        elif len(set(lotto_num_dict[cnt][0]).intersection(buyer_number))  == atari_num[1] and len(set([lotto_num_dict[cnt][1]]).intersection(buyer_number)) == 1:
            print_out(lotto_num_dict,atari_num[1])
            str_ = "2등입니다. 당첨금은 5천만원입니다. "
            print(str_)
        elif len(set(lotto_num_dict[cnt][0]).intersection(buyer_number))  == atari_num[1] :
            print_out(lotto_num_dict,atari_num[1])
            str_ = "3등입니다. 당첨금은 150만원 입니다.   "
            print(str_)
        elif len(set(lotto_num_dict[cnt][0]).intersection(buyer_number))  == atari_num[2] :
            print_out(lotto_num_dict,atari_num[2])
            str_ = "4등입니다. 당첨금은 5만원 입니다."
            print(str_)
        elif len(set(lotto_num_dict[cnt][0]).intersection(buyer_number))  == atari_num[3] :
            print_out(lotto_num_dict,atari_num[3])

            str_ = "5등입니다. 당첨금은 5천원 입니다."
            print(str_)

        else :
            print(f"{cnt}회차 번호{lotto_num_dict[cnt][0]} 입니다.|보너스번호는 {lotto_num_dict[cnt][1]}입니다. ")
            print(f"구매하신 번호는 {user_input_list} / 같은 숫자 번호 0개 입니다.  ")
            print("꽝입니다. 다음기회에...")
            # time.sleep(1)

    else:
        #로또 담첨번호 출력
        print(f"{cnt} 회차 당첨번호 {lotto_num_dict[cnt][0]} 입니다.// 보너스번호는 {lotto_num_dict[cnt][1]}입니다.")
        # time.sleep(1)

    str_ =""
    cnt += 1

