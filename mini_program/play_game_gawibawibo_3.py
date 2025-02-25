import random
'''
가위바위보 게임
1번플레이어가 "가위바위보" 중 하나를 입력
2번플레이어가 "가위바위보" 중 하나를 입력
최종적으로 1번과 2번 플레이어가 각 각 무엇을 냈는지 보여주고
어떤 플레이어가 이겼느지 알려주는 프로그램

컴퓨터가 랜던값을 낸다.
random.randint(1, 4) 1가위 ,2바위 3,보

'''
cnt = 0
while cnt < 10 :

    player1 = input("컴퓨터와 가위바위보를 합시다. >> [가위, 바위, 보 ]중 하나만 냅니다. ")
    # player2 = input("플레이어 2의 선택 예시 >> [가위, 바위, 보 ]중 하나만 냅니다. ")
    dict_com ={
        1:"가위",
        2:"바위",
        3:"보"
    }
    r_com = random.randint(1,3)

    computer = dict_com[r_com]


    # 사용자가 낸 값 검증
    if player1 not in ["가위", "바위", "보"] :
        print("올바른 값을 내세요")

    else :
        # 사용자들이 올바른 값을 냈을경우
        if player1 =="가위" and computer =="가위":
            print("플레이어 1,컴퓨터 둘 다 가위를 내어 비겼습니다.")
        elif player1 =="바위" and computer =="바위":
            print("플레이어 1,컴퓨터 둘 다 바위를 내어 비겼습니다.")
        elif player1 =="보" and computer =="보":
            print("플레이어 1,컴퓨터 둘 다  보를 내어 비겼습니다.")

        elif player1 =="가위" and computer =="바위":
            print("플레이어1은 가위, 컴퓨터는  바위를 냈습니다.  컴퓨터가 이겼습니다. ")
        elif player1 == "가위" and computer == "보":
            print("플레이어1은 가위 ,컴퓨터는 보를 냈습니다.  플레이어 1이 이겼습니다. ")

        elif player1 == "바위" and computer == "보":
            print("플레이어1은 바위 ,컴퓨터는 보를 냈습니다.  컴퓨터는가 이겼습니다. ")
        elif player1 == "바위" and computer == "가위":
            print("플레이어1은 바위 ,컴퓨터는 가위를 냈습니다.  플레이어1이 이겼습니다. ")

        elif player1 == "보" and computer == "가위":
            print("플레이어1은 보 ,컴퓨터는 가위를 냈습니다.  컴퓨터가 이겼습니다. ")
        elif player1 == "보" and computer == "바위":
            print("플레이어1은 보 ,컴퓨터는 바위를 냈습니다.  플레이어1 가 이겼습니다. ")


    cnt= cnt+1




