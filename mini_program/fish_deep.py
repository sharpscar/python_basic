
account = 100
cnt =0
pollution=0
is_paid=None
is_cleaned=None
water_tank = []
limit_water_tank = 10

def buy_fish(f_water_tank,f_account):
    print(f"현재 자산은 {account} 입니다.")
    select_fish = input("구매할 물고기 선택 1.고등어(10), 2.도미(100), 3.참치(1000) 숫자만 입력하세요 ")
    if not select_fish.isdigit():
        print("숫자만 입력하세요")
        select_fish = input("구매할 물고기 선택 1.고등어(10), 2.도미(100), 3.참치(1000) 숫자만 입력하세요 ")
    try:
        select_quantity = int(input("몇마리 구매?"))
    except:
        print("숫자입력")
        select_quantity = int(input("몇마리 구매?"))
    if select_quantity > 11:
        print("10마리 이상은 안됩니다.")
        select_quantity = int(input("몇마리 구매?"))
    price = 0
    if select_fish == '1':
        fish = '고등어'
        price = 10
    elif select_fish == '2':
        fish = '도미'
        price = 100
    elif select_fish == '3':
        fish = '참치'
        price = 1000
    else:
        fish = '고등어'  # 디폴트값으로 이거라도 넣었다. 물고기가 아닌것이 들어가면 개발자가 몹시 불쾌해진다.
        price = 10
    # 구매 조건에 부합하면 구매 처리 1.현재 자산, 2 수조 상태
    f_total_price = price * select_quantity

    # 기본 수조는 10 - 빈공간이 구매하려는 고기수보다 클때만 구매가능
    if limit_water_tank - wt_room >= select_quantity:
        



    for q in range(select_quantity):
        f_water_tank.append([fish, 0, False])
    print(f"어항상태 {len(f_water_tank)} /10")
    f_account = f_account - f_total_price
    return [f_water_tank, f_account]
    # 총 유저가 선택한 물고기종류*수량 = 지불하려는 비용

while cnt<100:

    user_input = input("입력 예시> 구매,상태, 먹이(주기), 수질(관리), 수조(구매) ) ")

    if account < -2000:
        print("돈이 부족하여 게임이 종료되었습니다. ")
        break

    if user_input == "구매":
        #구매
        water_tank,account =buy_fish(water_tank,account)
    if user_input == "먹이":
        #먹이주기
        pass
        # 돈이 0보다 많은가?
        is_bankrupt = is_money_zero() # True의 경우 파산이다.
        if not is_bankrupt:
            #돈을 차감 1.수조에 정보[fish, quentity] 리스트를 가져온다. 2. 총비용을 계산해서 유저주머니에서 뺀다.
            is_paid = pay_money() # return True or False

        else:
            # 유저는 이미 파산된 상태이다 미이너스 계좌로 간다.
            is_paid =pay_money()

    if user_input == "수질":
        #수질관리
        is_bankrupt = is_money_zero()
        is_done = reset_environment() # T/F         pollution =100
        pass
    if user_input == "수조":
        #수조구매
        pass
        buy_water_tank() # 물고기 제한량을 10씩 증가시킨다. limit_water_tank +10

    # 수질에 따른 처리
    pollution = get_pollution()
    if pollution>50:
        water_tank=kill_cham() #현재 수조의 모든 참치 20% 확률로 kill!
        if pollution>40:
            water_tank=kill_domi()
            if pollution>30:
                water_tank=kill_godu()

    if is_paid == "True" or is_cleaned == "True":
        print(f"{cnt} 회 턴 종료합니다.")
        pollution = pollution-10
        cnt += 1