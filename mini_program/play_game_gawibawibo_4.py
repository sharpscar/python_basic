import random
'''
for문 2개로 가위바위보 만들어보자 - 실패 
반복문 2개로 9가지 경우의수가 나온다는건 확인했지만 
플레이어 컴퓨터 승패를 이프문 하나로 판별하는건 쉽지가 않다. 다른 방식으로 접근하는걸 생각해봐야겠다. 

'''

list_player = ["플가위","플바위","플보"]

list_computer = ["컴가위","컴바위","컴보"]
choice_com = random.choice(list_computer)
cnt =0
while cnt<2 :
    for i in list_player:
        for j in list_computer:
            if i=="플가위" and j=="컴보" or i=="플바위" and j=="컴가위" or i=="플보" and j=="컴바위" :
                print(f"플레이어의 승리 입니다.")
            elif i=="플가위" and j=="컴바위"or i=="플바위"and j=="컴보" or i=="플보" and j =="컴가위":
                print(f"컴퓨터의 승리입니다.")
            else :
                print(f"비긴겁니다.")
    cnt = cnt+1