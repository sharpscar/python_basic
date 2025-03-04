

money = 100
end_money = input("목표금액을 입력하세요")
turn = 0

def select_fish():
    fish = input("물고기를 선택하세요 1.고등어(10) 2. 도미(100) 3. 참치(1000) ")
    quantity = input("몇마리 살지 선택하세요")
    if fish == '1':
        fish = '고등어'
    elif fish == '2':
        fish = '도미'
    elif fish == '3':
        fish = '참치'
    else:
        input("입력을 잘못하셨습니다.")
        input()
    int(quantity)
    return [fish,quantity]

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
    f_water_tank.append({'sellable':False,'생선명':f_fish, '수량': f_quantity , 'stat' : 0, 'sale_price' : f_price})
    return f_water_tank

''' 물고기가 성체인지 아닌지 확인하고 성체이면 판매가능하도록 상태변경 '''
def check_fish_is_big(f_water_tank, fish):
    for i_ in f_water_tank:
        if i_['생선명'] == fish:
            if i_['stat'] == 3:
                i_['sellable'] = True
                i_['stat'] = 0
    return f_water_tank

def check_sellable(f_water_tank):
    sellable_fish =[]
    for i_ in f_water_tank:
        if i_['sellable'] :
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
def sell_fish(f_water_tank):
    sell_fishs = []
    f_total = 0
    f_quantity = 0
    for i_ in f_water_tank:
        if i_['sellable'] =='True':
            # quantity 조회 합산 , price조회 합산
            sell_fishs.append(i_)
            f_quantity  +=i_['quantity']
            f_total += i_['sale_price']
    f_water_tank.del
    return [sell_fishs, f_quantity, f_total]

# 구매할 물고기, 수량을 받는다.
fish,quantity = select_fish()
water_tank = buy_fish(fish, quantity)
is_sellable = False
while turn <4:
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
            money += sell_list[2]
        #sell_list의 3번째 인덱스에 판매대금이 있으니 전역변수 돈에 추가한다.

        # 판매 안내를 한다.{'sellable':'True','생선명':f_fish 'quantity': 1 , stat : 0} 인 애들이 몇개인지 보여주고 생선명이 같은애들의 숫자를 합산한다.
    # 판매를 한다.
    '''
    water_tank 안에 sellable이 True 이고 생선명이 '고등어'인 요소들의 [quantity,가격] 합산 .
    1. 해당 요소들을 가져와서 다른 dict로 만든다. 
    2. 해당 요소들을 delete한다. 
    3. 돈을 판매한 가격과 합산한다.  
    '''

    # 구매가 가능하다면 구매 안내

    for i_turn in water_tank:
        i_turn['stat'] +=1
    turn = turn + 1

