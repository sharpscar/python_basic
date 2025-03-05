

money =  100
cnt = 0
water_tank = [] # 구입시 마릿수만큼 배열을 증가시킨다.[['고등어':0], ['도미':0],['참치':0]]
goal = int(input("목표금액을 입력하세요"))
turn = True

def buy(f_water_tank,f_fish,f_total_price,f_money,f_select_quantity):
    f_price = 0
    global money
    for q in range(f_select_quantity):
        f_water_tank.append([f_fish,0,False])
    print(f"어항상태 {f_water_tank}")
    money = f_money- f_total_price
    return [f_water_tank, money]


while cnt<100:

    user_input = input("입력 예시> 구매, 상태, 엔터 ) ")

    #유저의 선택이 사기
    if user_input == "구매":
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
        else:
            fish = '물고기가 아닌것'
            price = 0
        #총 유저가 선택한 물고기종류*수량 = 지불하려는 비용

        #구매 조건에 부합하면 구매 처리 1.현재 자산, 2 수조 상태
        total_price = price * select_quantity

        if total_price <= money:
            # 수조의 물고기가 10마리 이하이다.
            if len(water_tank) == 9:
                print("경고경고 수조가 비좁아요 10마리 이상은 구매 불가 현재 9마리입니다.")
            if len(water_tank) == 10:
                print("경고경고 수조가 비좁아요 10마리 이상은 구매 불가 더이상 구매불가합니다.")
            if len(water_tank) < 10 :
                # 조건을 만족하면 구매!
                water_tank, money = buy(water_tank,fish,total_price,money, select_quantity)
        else:
            print("돈이 부족합니다.")



    #턴마다 판매 가능 체크
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
    sallable_list = []
    total = 0 #판매대금이 될것이다. 반복할때마다 리셋되는게 맞겠지
    for w_ in water_tank:
        if w_[2]== True:
            sallable_list.append(w_)
            w_[1] = 0
    if sallable_list:
        # 표시
        for s in sallable_list:
            print(s[0])
            #sallable_list에 있는 모든 물고기의 값을 계산해야한다.
        '''
        이걸 보고 고등어 , 도미, 참치 로시작하는 리스트가 몇개인지 세고 
        가격에 곱하면 유저에게 얼마를 줘야하는지 파악이 된다. 
        '''
        god_cnt,domi_cnt,cham_cnt,price=[0,0,0,0]
        god_price = 50
        domi_price =300
        cham_price =1800
        for w in water_tank:
            if w[0] == "고등어":
                god_cnt = water_tank.count(['고등어', 0, True])
                total += god_cnt * price
            if w[0] == "도미":
                domi_cnt = water_tank.count(['도미', 0, True])
                total += domi_cnt * price
            if w[0] == "참치":
                cham_cnt = water_tank.count(['참치', 0, True])
        total = (god_cnt * god_price)+(domi_cnt*domi_price)+(cham_cnt*cham_price)

        print("========================")
        decision = input(f"위의 물고기를 판매하시겠습니까? 판매 예상금액 {total} y/n")
        if decision == "y":
            # 워터탱크에 3번째 배열에 True가 있는 리스트의 수를 구한다. (제거 해야할 요소)
            cnt_full_index = []
            for w in range(len(water_tank)):
                if water_tank[w][2]:
                    cnt_full_index.append(w)

            print(f"cnt_full_index{cnt_full_index} ")

            # 삭제를 위해 역순으로 뒤집는다.
            cnt_full_index.reverse()
            for idx in cnt_full_index:
                del water_tank[idx]
            # 수조에서 물고기를 뺏으니까 유저주머니를 두둑하게 해줄 차례다.
            money = money+total
    # 판매 완료



    if user_input =="상태":
        print(f"현재 수조 상태입니다.")
        for w in water_tank:
            print(f"물고기 종류:{w[0]}, 물고기의 성장상태 :{w[1]}")

    if user_input == "":
        print(f"턴을 종료합니다. 현재 돈은 {money}원이 있습니다.")

        for w in water_tank:
            w[1] = w[1] + 1


        print(f"{cnt} 회 턴 종료합니다.")
        cnt+=1
