from mini_program.fish import water_tank

money =  100
cnt = 0
water_tank = [] # 구입시 마릿수만큼 배열을 증가시킨다.[['고등어':0], ['도미':0],['참치':0]]


def buy(f_water_tank,f_select_fish,f_total_price,f_money,f_select_quantity):
    f_price = 0
    for q in range(len(f_select_quantity)):
        f_water_tank.append([f_select_fish,0,False])

    f_money = f_money- f_total_price
    return [f_water_tank, f_money]


while cnt<100:
    user_input = input("입력 예시> 사기, 상태, 엔터")

    #유저의 선택이 사기
    if user_input == "사기":

        print(f"현재 자산은 {money} 입니다.")

        select_fish  = input("구매할 물고기 선택 1.고등어(10), 2.도미(100), 3.참치(1000)")
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
        #총 유저가 선택한 물고기종류*수량 = 지불하려는 비용

        #구매 조건에 부합하면 구매 처리 1.현재 자산, 2 수조 상태
        total_price = price * select_quantity

        if total_price <= money:
            # 수조의 물고기가 10마리 이하이다.
            if len(water_tank) < 10 :
                # 조건을 만족하면 구매!
                buy(water_tank,select_fish,total_price,money, select_quantity)
        else:
            print("돈이 부족합니다.")

    #턴마다 수조를 체크해서 판매 가능한 고기는 마지막에 True 넣어준다.
    for w in water_tank:
        if w[0]=="고등어":
            limit = 4
            if w[1] == limit :
                w[2] = True
        if w[0] == "도미":
            limit = 8
            if w[1] == limit:
                w[2] = True
        if w[0] == "참치":
            limit = 12
            if w[1] == limit:
                w[2] = True
    # 판매 가능한 고기가 있으면 물고기종류와 갯수를 표시하고 판매의사를 묻는다.
    for w_ in water_tank:
        if w_[2]== True:


    if user_input =="상태":
        print(f"현재 수조 상태입니다.")
        for w in water_tank:
            print(water_tank)

    if user_input == "":
        print(f"턴을 종료합니다.")

        for w in water_tank:
            w[1] = w[1] + 1


    cnt+=1
