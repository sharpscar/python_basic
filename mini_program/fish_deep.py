
account = 100
cnt =0
pollution=0
is_paid=None
is_cleaned=None
water_tank = []
limit_water_tank = 10

'''
## status 변수 

### 함수를 사용하면서 매개변수가 거의 2줄에 육박하기에 이르렀다. 그럼 변수 하나로 함수간 정보를 주고 받기 위해서 스테이터스 라는 변수를 만들게 되었다.

	water_tank   2 중 배열   수조   ['도미', 4, False]
	account        int     자산
	fish_info    [str,int] 구매시 물고기 정보
	wt_count     int       수조의 갯수
	pollution    int       오염도
	simple_wt_info dict.   water_tank의 물고기를 어종별로 마릿수를 정리한 변수-턴마다 동기화 

status = {
    'water_tank' : [],
    'account' : 0,
    'fish_info' : [],
    'wt_count':1,
    'pollution':100,
    'simple_wt_info':{
    '고등어':0,
    '도미':0,
    '참치':0
    }
    
}

'''
status = {
    'water_tank': [],
    'account': 0,
    'fish_info': [],
    'wt_count': 1,
    'pollution': 100,
    'simple_wt_info': {
        '고등어': 0,
        '도미': 0,
        '참치': 0
    }
}




# 현재 수조의 빈공간을 계산해서 정수로 반환  매개변수 limit는 현재 보유하는 수조 *10 , wt, 구매하려는 물고기숫자
def get_wt_empty_space(f_limit, wt ,quantity):
    # 구매하려는 물고기 숫자가 수조에 남은 공간보다 크면 구매할수 없다.
    if f_limit - len(wt) >= quantity:
        print(f"수조의 빈공간을 계산 { f_limit - len(wt)}")
        return f_limit - len(wt)


def buy_fish(water_tank,account):
    status['water_tank'] =  water_tank
    status['account'] = account
    print(f"현재 자산은 {status[account]} 입니다.")
    select_fish = input("구매할 물고기 선택 1.고등어(10), 2.도미(100), 3.참치(1000) 숫자만 입력하세요 ")
    if not select_fish.isdigit():
        print("숫자만 입력하세요")
        select_fish = input("구매할 물고기 선택 1.고등어(10), 2.도미(100), 3.참치(1000) 숫자만 입력하세요 ")
    try:
        status['fish_info'][1] = int(input("몇마리 구매?"))
    except:
        print("숫자입력")
        status['fish_info'][1] = int(input("몇마리 구매?"))
    if status['fish_info'][1] > 11:
        print("10마리 이상은 안됩니다.")
        status['fish_info'][1] = int(input("몇마리 구매?"))
    price = 0
    if select_fish == '1':
        # status['fish_info'] = [어종,마릿수,가격,총가격]
        status['fish_info'][0] = '고등어'
        status['fish_info'][2]  = 10
    elif select_fish == '2':
        status['fish_info'][0] = '도미'
        status['fish_info'][2] = 100
    elif select_fish == '3':
        status['fish_info'][0] = '참치'
        status['fish_info'][2] = 1000
    else:
        status['fish_info'][0] = '고등어'  # 디폴트값으로 이거라도 넣었다. 물고기가 아닌것이 들어가면 개발자가 몹시 불쾌해진다.
        status['fish_info'][2] = 10
    # 구매 조건에 부합하면 구매 처리 1.현재 자산, 2 수조 상태
    status['fish_info'][3] = status['fish_info'][2] * status['fish_info'][1]
    # 빈공간을 계산하는 함수를 구현해야함
    is_empty_space = get_wt_empty_space(status['wt_count']*10, status['water_tank'],status['fish_info'][1])

    # 기본 수조는 10 - 빈공간이 구매하려는 고기수보다 클때만 구매가능
    if is_empty_space :
        if status['fish_info'][3] <= status['accountunt']:
            for q in range(status['fish_info'][2]):
                # 수조에 들어가는 물고기 정보는 ['어종',포만도:int,'판매가능여부']이다. fish 정보 프로퍼티와 혼동되면 큰일남
                status['water_tank'].append([status['fish_info'][0], 0, False])
            print(f"어항상태 {len(status['water_tank'])} / {status['wt_count']*10} ")
            status['account'] = status['account'] - status['fish_info'][3]

    # 총 유저가 선택한 물고기종류*수량 = 지불하려는 비용

while cnt<100:

    user_input = input("입력 예시> 구매,상태, 먹이(주기), 수질(관리), 수조(구매) ) ")

    if status['account'] < -2000:
        print("돈이 부족하여 게임이 종료되었습니다. ")
        break

    if user_input == "구매":
        #구매
        status['water_tank'],status['account'] = buy_fish(status['water_tank'],status['account'])
    # if user_input == "먹이":
    #     #먹이주기
    #     pass
    #     # 돈이 0보다 많은가?
    #     is_bankrupt = is_money_zero() # True의 경우 파산이다.
    #     if not is_bankrupt:
    #         #돈을 차감 1.수조에 정보[fish, quentity] 리스트를 가져온다. 2. 총비용을 계산해서 유저주머니에서 뺀다.
    #         is_paid = pay_money() # return True or False
    #
    #     else:
    #         # 유저는 이미 파산된 상태이다 미이너스 계좌로 간다.
    #         is_paid =pay_money()
    #
    # if user_input == "수질":
    #     #수질관리
    #     is_bankrupt = is_money_zero()
    #     is_done = reset_environment() # T/F         pollution =100
    #     pass
    # if user_input == "수조":
    #     #수조구매
    #     pass
    #     buy_water_tank() # 물고기 제한량을 10씩 증가시킨다. limit_water_tank +10
    #
    # # 수질에 따른 처리
    # pollution = get_pollution()
    # if pollution>50:
    #     water_tank=kill_cham() #현재 수조의 모든 참치 20% 확률로 kill!
    #     if pollution>40:
    #         water_tank=kill_domi()
    #         if pollution>30:
    #             water_tank=kill_godu()

    if is_paid == "True" or is_cleaned == "True":
        print(f"{cnt} 회 턴 종료합니다.")
        pollution = pollution-10
        cnt += 1