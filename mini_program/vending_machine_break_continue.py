'''
2025년 2월 21일 (금)

팹시 콜라(800), 코카콜라(900), 포카리(700), 물(500)
사용자에게 돈, 뭐먹을지 물어보고
그것에 맞춰 제품과 잔돈을 출력

없는 메뉴일 시 해당메뉴가 존재하지 않습니다.
돈이 부족하면 돈이 부족합니다.
메뉴에 없는 것 우선 돈이 없으면

'''


drinks = {
   "팹시콜라" : "800",
   "코카콜라":"900",
   "포카리":"700",
   "물":"500",
}
switch = True  # 추후 물품이 없는경우 switch를 false
change_money =0 #거스름돈

while switch:

    user_money = input("돈을 넣으세요  =>")
    #숫자가 아닐경우 무시하는 코드를 넣자
    change_money = change_money+int(user_money)

    user_select = input("메뉴를 고르세요 [팹시콜라(800), 코카콜라(900), 포카리(700), 물(500)]  => ")

    # 유저의 입력을 받아서 drink딕셔너리에 키를 검색 해당하는 문자열 하나라도 있으면 해당 키의 값을 가져온다.
    for drink in drinks :
        if drink.startswith(user_select):
            user_select = drink

    print("잔액은 {} 입니다. 선택하신 음료는 {}입니다. ".format(change_money, user_select))


    # 1. 메뉴가 있나
    if user_select in drinks:
        # 유저가 선택한 음료의 가격
        user_select_price = int(drinks[user_select])
        # 2. 돈은 있나
        if user_select_price < change_money :

            # 유저 주머니에서 선택한 음료 가격을뺀다.
            change_money = change_money - user_select_price
            # 여기서 만약 거스름돈이 메뉴에 있는 최소가격보다 높은경우 ? 또다른 주문을 받는다. : 선택한 음료와 거스름돈을 준다.
            print("선택하신 음료는 {}입니다. 가격은 {}원 입니다. 그리고 잔액은 {}원 입니다. ".format(user_select, user_select_price, change_money))

        # 유저가 넣은 돈과 음료 가격이 같을때
        elif user_select_price == change_money:

            print("선택하신 음료는 {}입니다.가격은 {}원 입니다. 그리고 잔액은 0입니다. ".format(user_select, user_select_price))
            continue
        # 유저가 넣은 돈이 부족할때
        else :

            print("돈이 부족합니다. {}원을 돌려드립니다.  ".format(change_money))
            continue


    else:

        print("찾으시는 메뉴가 없습니다.{}원을 돌려드립니다. ".format(change_money))
        continue





# switch = True
# while True:
#     for menu in drinks:
#         #유저가 입력한 음료가 메뉴에 없을때
#         if user_input in drinks:
#             print(user_input)
#             #스위치를 끄고 continue문으로 다시 입력을 받는다.
#             switch = False
#             continue
#     user_input = input("메뉴를 입력하세요")