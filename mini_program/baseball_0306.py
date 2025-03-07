import random
difficulty = {'상':9, '중':12, '하':15}
# turn_limit =0
# 배열엔 승패포 이렇게 기록한다.
record = {
        #승패포
    '상':[0,0,0],
    '중':[0,0,0],
    '하':[0,0,0]
}
def select_difficulty():
    game_info= {}
    turn_limit = 0
    user_select_2 = input("1.상 2.중 3.하  | 난이도를 선택하세요 ")

    if user_select_2 == "1":
        turn_limit = difficulty['상']
    if user_select_2 == "2":
        turn_limit = difficulty['중']
    if user_select_2 == "3":
        turn_limit = difficulty['하']

    game_info['difficulty'] =user_select_2
    game_info['record'] = ''
    game_info['turn_limit'] = turn_limit

    #난이도 선택시 pc의 랜덤번호를 생성해 받아서 넣어준다.
    ran_list = get_random_number()
    game_info['ran_list'] =ran_list

    return game_info
    # 게임을 시작하는곳

def main_scene(rec_result='None'):
    main_select = input("1.플레이하기 2. 전적보기 3. 종료 | 숫자를 선택하세요 ")

    if main_select == "1":
        game_info = select_difficulty()
        start_game(game_info)

    if main_select == "2":
        # 전적보기 rec_result
        difficulty_1_total = rec_result['상'][0] +rec_result['상'][1]
        if difficulty_1_total == 0:
            difficulty_1_total = 1
        difficulty_2_total = rec_result['중'][0] + rec_result['중'][1]
        if difficulty_2_total == 0:
            difficulty_2_total =1
        difficulty_3_total = rec_result['하'][0] +rec_result['하'][1]
        if difficulty_3_total == 0:
            difficulty_3_total =1
        print(rec_result) # 승패포판
        print(f"난이도 상 \n 승\t{rec_result['상'][0]},\t패\t{rec_result['상'][1]},\t포기\t{rec_result['상'][2]} \n난이도 중 \n 승\t{rec_result['중'][0]},\t패\t{rec_result['중'][1]},\t포기\t{rec_result['중'][2]}, \n"
              f"난이도 하 \n 승\t{rec_result['하'][0]},\t패\t{rec_result['하'][1]},\t포기\t{rec_result['하'][2]} \n\t\t".rjust(1, " "))


        print(f"상 {rec_result['상'][0] / difficulty_1_total * 100} \t\t"
              f"중 {rec_result['중'][0] / difficulty_2_total * 100} \t\t"
              f"하 {rec_result['하'][0] / difficulty_3_total * 100}")
        main_scene()

    if main_select == "3":
        # 종료 게임의 난이도/ 승패를 기록하고 게임을 종료한다.
        quit()

def get_random_number():
    num = set()
    while len(num) < 3:
        num.add(random.randint(1, 9))
    ran_list = list(num)
    return ran_list


def giveup_game(game_info):

    game_info['record'] = '포기'
    record = set_record(game_info)
    return record


def get_input(game_info=None):
    user_input = input("3개의 숫자를 ,로 띄어서 입력해줘요>> 포기하기는 '포기'입력 ")
    if user_input == '포기':
        result = giveup_game(game_info)
        if result :
            # 왜 매개변수로 result가 필요한가. 만약 없애고 포기를 2번 할경우 전적 보기를 했을때 터진다. . 43라인 string indices must be integers, not 'str'
            main_scene(result)#result

    user_input_list = user_input.split(",")
    if len(user_input_list) > 4:
        print("사용자의 입력이 4개 이상입니다. ")

    for i in range(len(user_input_list)):
        user_input_list[i] = int(user_input_list[i])
    return user_input_list


        # 난이도를 선택해서 제한 턴을 설정했다.
'''
game_info = {
                'difficulty': f_difficulty,
                record: [1, 0, 0]
            }
'''
def set_record(game_info):
    #게임의 승패를 record 변수에 기록한다. 승, 패, 포기, 판
    # record = {'상': [0, 0, 0,0], '중': [0, 0, 0,0], '하': [0, 0, 0,0]}


    if game_info['difficulty']=="1" and game_info['record'] == '승':
        record['상'][0] = record['상'][0] + 1
    if game_info['difficulty']=="1" and game_info['record'] == '패':
        record['상'][1] = record['상'][1] + 1
    if game_info['difficulty']=="상" and game_info['record'] == '포기':
        record['상'][2] = record['상'][2] + 1
    if game_info['difficulty']=="2" and game_info['record'] == '승':
        record['중'][0] = record['중'][0] + 1
    if game_info['difficulty']=="2" and game_info['record'] == '패':
        record['중'][1] = record['중'][1] + 1
    if game_info['difficulty']=="2" and game_info['record'] == '포기':
        record['중'][2] = record['중'][2] + 1
    if game_info['difficulty']=="3" and game_info['record'] == '승':
        record['하'][0] = record['하'][0] + 1
    if game_info['difficulty']=="3" and game_info['record'] == '패':
        record['하'][1] = record['하'][1] + 1
    if game_info['difficulty']=="3" and game_info['record'] == '포기':
        record['하'][2] = record['하'][2] + 1
    return record


def game_over(record):
    # 끝나기전 기록을 한다.
    rec_result = set_record(record)

    #기록을 하고나면 뭘 반환해야할까? 기록 정보를 반환해보자 다시하기 ->reset_game() : pc의 랜덤 리스트를 갱신
    is_continue = input("게임이 종료되었습니다. 게임을 계속 하시겠습니까? y/n")

    if is_continue =="y" or is_continue =="Y" :
        # pc번호를 갱신

        game_info = select_difficulty()
        start_game(game_info)
    else:
        main_scene(rec_result)

    return rec_result


def start_game(game_info):
    pnl = game_info['ran_list']

    # print(pnl)
    cnt = 0

    while(game_info['turn_limit']):

        uil = get_input(game_info)
        strike = 0
        ball = 0

        for i in range(len(pnl)):
            for j in range(len(uil)):

                # i 와 j 가 인덱스가 같고 값이 같은경우 스트라이크 +1  i 와 j의 인덱스가 다르고 값이 같은경우는 볼 +1
                if i == j:
                    if pnl[i] == uil[j]:
                        strike = strike + 1
                else:
                    if pnl[i] == uil[j]:
                        ball = ball + 1

        print("strike는 {},ball은 {} {}턴째입니다.".format(strike, ball,cnt+1))

        # 만약 스트라이크가 3이상인경우 게임 중지
        if strike == 3:
            # 유저가 선택한 난이도를 가져온다. 게
            print("3진아웃 입니다. You win")
            game_info['record'] = '승'
            record_result = game_over(game_info)

        # 턴이 늘어날수록 난이도에 따라 턴이 줄어든다.
        game_info['turn_limit']= game_info['turn_limit']-1

        #턴  계산
        cnt+=1

        # 기회가 다 소모되어 게임이 종료
        if game_info['turn_limit']==0:
            # 유저가 선택한 난이도를 가져온다.
            print("아쉽게 됐네요 좀더 연습을 하셔야겠네요.")

            # game_info['difficulty'] = game_info['difficulty']
            game_info['record'] = '패'
            record_result = game_over(game_info)
            print(f"게임이 패배로 끝남 {record_result}")

main_scene()