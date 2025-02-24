'''
2025년 2월 21일 (금)

팹시 콜라(800), 코카콜라(900), 포카리(700), 물(500)
사용자에게 돈, 뭐먹을지 물어보고
그것에 맞춰 제품과 잔돈을 출력

없는 메뉴일 시 해당메뉴가 존재하지 않습니다.
돈이 부족하면 돈이 부족합니다.
메뉴에 없는 것 우선 돈이 없으면

'''


drink = {
   "팹시콜라" : "800",
   "코카콜라":"900",
   "포카리":"700",
   "물":"500",
}
user_money = input("돈을 넣으세요  =>")
user_money = int(user_money)
user_select = input("메뉴를 고르세요 [팹시콜라(800), 코카콜라(900), 포카리(700), 물(500)]  => ")

print("주신돈은 {} 입니다. 선택하신 음료는 {}입니다. ".format(user_money,user_select))

# 1. 메뉴가 있나
if user_select in drink:
    # 유저가 선택한 음료의 가격
    user_select_price = int(drink[user_select])
    # 2. 돈은 있나
    if user_select_price < user_money :

        # 유저 주머니에서 선택한 음료 가격을뺀다.
        user_money = user_money - user_select_price
        # 여기서 만약 거스름돈이 메뉴에 있는 최소가격보다 높은경우 ? 또다른 주문을 받는다. : 선택한 음료와 거스름돈을 준다.
        print("선택하신 음료는 {}입니다. 가격은 {}원 입니다. 그리고 잔돈은 {}원 입니다. ".format(user_select, user_select_price, user_money))
    # 유저가 넣은 돈과 음료 가격이 같을때
    elif user_select_price == user_money:

        print("선택하신 음료는 {}입니다.가격은 {}원 입니다. 그리고 잔돈은 0입니다. ".format(user_select, user_select_price))
    # 유저가 넣은 돈이 부족할때
    else :

        print("돈이 부족합니다. {}원을 돌려드립니다.  ".format(user_money))


else:
    print("찾으시는 메뉴가 없습니다.{}원을 돌려드립니다. ".format(user_money))




