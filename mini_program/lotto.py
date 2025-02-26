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

'''

lotto_num_dict = {}
cnt = 1
buyer_num_dict = {}
str_ =""
switch = 1
user_list = [0,0,0,0,0,0]
auto=True
'''
    buyer_number = input("로또번호를 6개 입력하세요 , 형식 자동은 '자동' 입력 >>")
    buyer_number = [int(i) for i in buyer_number.split(",")]
    입력을 하나씩 받고 총 6개의 숫자를 리스트에 넣는다. 
'''

for i in range(6):
    input_str = input("로또번호 하나씩 입력해주세요 ")
    # if type(input_str) !="int":
    #     # int가 아니니 다시 받아야한다.

    input_int = int(input_str)
    user_list[i] = input_int

# 중복체크
for idx,val  in enumerate(user_list):
    number_cnt = user_list.count(val)
    if number_cnt > 1:
        print("중복된값이 있습니다 다시입력하세요")

print(f"넣은 번호는 {user_list}입니다.")
auto_ = input("자동을 돌리시겠습니까? y/n")

while auto :
    # 컴퓨터 랜덤 넘버 생성 6+1
    lotto = (list(range(1,46)))

    random.shuffle(lotto)
    lotto_num = lotto[0:6]
    lotto_bonus = lotto[-1]
    lotto_num.sort()
    lotto_num_dict[cnt] = [lotto_num , lotto_bonus]

    buyer_number = user_list

    buyer_num_dict[cnt] = buyer_number
    # 유저번호가 6개 일치 1등, 보너스 1개가 일치하고 유저 번호 5개가 동일하다면 2등  유저번호 5개만 동일하다면 3등
    if len(set(lotto_num_dict[cnt][0]).intersection(buyer_number)) == 6 :
        str_ ="ㅊㅋㅊㅋ 1등 20억"
    elif len(set(lotto_num_dict[cnt][0]).intersection(buyer_number))  == 5 and len(set([lotto_num_dict[cnt][1]]).intersection(buyer_number)) == 1:
        str_ = "2등입니다."
    elif len(set(lotto_num_dict[cnt][0]).intersection(buyer_number))  == 5 :
        str_ = "3등입니다."
    else :
        print("다음기회에")

    str_ += f"{cnt} 회차 당첨번호 {lotto_num_dict[cnt][0]} 입니다.// 보너스번호는 {lotto_num_dict[cnt][1]}입니다. "


    print(str_)
    str_ =""
    if auto_ == "y":
        auto = True
        time.sleep(2)
    elif auto_ == "q":
        break
    else:
        auto = False

    cnt += 1

