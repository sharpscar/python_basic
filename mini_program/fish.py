

money = 100
end_money = input("목표금액을 입력하세요")
turn = 0

def get_current_money():
    if money == int(end_money):
        "게임 종료 {turn}째에 끝났습니다. "
    return money

def select_fish(money):
    fish = input("물고기를 선택하세요 1.고등어(10) 2. 도미(100) 3. 참치(1000) ")
    price = 0
    quantity = int(input("몇마리 살지 선택하세요"))
    if fish == '1':
        fish = '고등어'
        price =10
    elif fish == '2':
        fish = '도미'
        price =100
    elif fish == '3':
        fish = '참치'
        price = 1000
    else:
        input("입력을 잘못하셨습니다.")
        input()
    int(quantity)
    total =  price * quantity
    money= money - total
    return [fish,quantity, money]

'''
 물고기를 추가할때 {'sellable':'False','고등어 ': 1 , stat : 0} 이런식으로 추가  stat은 4이상 올라갈수 없다.'''
def buy_fish(f_fish, f_quantity):
    f_price = 0
    f_water_tank=[]
    if f_fish == '고등어':
        f_price=50
    elif f_fish == '도미':
        f_price = 300
    elif f_fish == '참치':
        f_price = 1800
    f_water_tank.append({'판매가능':False,'생선명':f_fish, '수량': f_quantity , '배부름상태' : 0, '판매가' : f_price})
    return f_water_tank

''' 물고기가 성체인지 아닌지 확인하고 성체이면 판매가능하도록 상태변경 '''
def check_fish_is_big(f_water_tank, fish):
    for i_ in f_water_tank:
        if i_['생선명'] == fish:
            if i_['배부름상태'] == 3:
                i_['판매가능'] = True
                i_['배부름상태'] = 0
    return f_water_tank

def check_sellable(f_water_tank):
    sellable_fish =[]
    for i_ in f_water_tank:
        if i_['판매가능'] :
            sellable_fish.append(i_)
            return sellable_fish
        else:
            return False
'''
water_tank 안에 sellable이 True 이고 생선명이 '고등어'인 요소들의 [quantity,가격] 합산 .
1. 해당 요소들을 가져와서 다른 dict로 만든다. 
2. 해당 요소들을 delete한다. 
3. 돈을 판매한 가격과 합산한다.  
'''
def sell_fish(f_water_tank, money):

    f_total = 0
    f_quantity = 0
    for i_,val in enumerate(f_water_tank):
        if val['판매가능'] ==True:
            # quantity 조회 합산 , price조회 합산

            f_quantity  = int(val['수량'])
            f_price = int(val['판매가'])
            f_water_tank.pop(i_) #안먹힌다. 해당하는 인덱스를 가져와서 지워야한다.
            money = f_quantity * f_price
    return [f_water_tank, money]



is_sellable = False
while turn <100:

    # 목표 금액에 도달하면 게임이 종료한다.
    get_current_money()

    if money > 10 :
        # 구매할 물고기, 수량을 받는다. 그리고 돈에 서 빼야한다.
        fish, quantity, money = select_fish(money)
        print(f"돈은 {money}")
        water_tank = buy_fish(fish, quantity)
        print(water_tank)
    # 스테이터스를 보고싶다면 스테이터스 안내

    # 고등어 수량을 체크한다.
    water_tank = check_fish_is_big(water_tank,'고등어')
    # 도미 수량을 체크한다.
    water_tank = check_fish_is_big(water_tank, '도미')
    # 참치 수량을 체크한다.
    water_tank = check_fish_is_big(water_tank, '참치')
    # 판매가 가능하다면 판매 가능한 요소들을 뿌려준다.

    sallable_list = check_sellable(water_tank)

    if sallable_list:
        # print(sallable_list)
        for i_sell in sallable_list:
            print(f"현재 판매 가능한 물고기 : {i_sell['생선명']} {i_sell['수량']}마리 가 있습니다.")
        answer = input("현재 판매 가능한 물고기가 있습니다. 판매하시겠습니까? y/n")
        if answer =="y":
            sell_list = sell_fish(water_tank)

        print(water_tank)
        print(money)
        #sell_list의 3번째 인덱스에 판매대금이 있으니 전역변수 돈에 추가한다.

        # 판매 안내를 한다.{'sellable':'True','생선명':f_fish 'quantity': 1 , stat : 0} 인 애들이 몇개인지 보여주고 생선명이 같은애들의 숫자를 합산한다.
    # 판매를 한다.
    '''
    water_tank 안에 sellable이 True 이고 생선명이 '고등어'인 요소들의 [quantity,가격] 합산 .
    1. 해당 요소들을 가져와서 다른 dict로 만든다. 
    2. 해당 요소들을 delete한다. 
    3. 돈을 판매한 가격과 합산한다.  
    '''
    input("enter를 누르시면 턴을 종료합니다.")
    # 구매가 가능하다면 구매 안내
    print(f"{turn}회 반복중입니다.")
    for i_turn in water_tank:
        i_turn['배부름상태'] +=1
    turn = turn + 1

