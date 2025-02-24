''' 숫자형 , 부울린, 문자열과 같이 컴퓨터가 알고있는 이진법을 우리가 알고있는 형태로 정의 하는 방식입니다.

자료구조 = 자료형이 어떻게 배치되어있는가 ?

리스트 = 데이터를 나열 : int array[] = ["uno(un)","dos',"tres","cuatro"] ,

정수 3개
실수 4개
문자열 5개

정수 3개
실수4개
문자열 5개

'''

my_int = [1,2,3,4]

my_float1 = [0.11,0.25,0.45,0.77]

my_string = ["하나","둘","셋둘하나","넷","다섯"]

my_int_t = (1,2,3,4)

my_float_t = (0.11,0.25,0.45,0.77)

my_string_t= ("하나","둘","셋둘하나","넷","다섯")



def test_my_value(value):
    print(type(value))


value_list = [my_int_t,my_float_t,my_string_t]

# print(value_list[2][0:3])

for i in value_list:
    # test_my_value(i[0])
    for j in i:
        pass
        # test_my_value(j)


# print(my_string[4][0])
'''dictionary  {} 중괄호로 표현  key, value  키값 쌍으로 자료를 저장할때 사용하는 자료형 '''
dict_ = {
    "안녕": "이것은 이사입니다.",
    "잘가": "이것은 헤어질때 인사입니다.",
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}
new_dict = {
    "Test":["안녕", "하이","구텐탁","곤니찌와"]
}
# print(new_dict)
# print(dict_["안녕"][1])
pick_one_character_from_dict = new_dict["Test"][2][1]
# print(pick_one_character_from_dict)

'''  File "/home/scar/PycharmProjects/PythonProject/main_2021.py", line 65, in <module>
    print(new_dict[i][j])
          ~~~~~~~~~~~^^^
TypeError: list indices must be integers or slices, not str
리스트의 지수는 숫자 또는 슬라이스, 여야 합니다. 문자가 들어가면안된다.  j로 
'''
''' set은 중복을 허용치 않는다. 중복없는 자료를 원할땐 set을 사용해라 
    set은 인덱스를 제공하지 않는다. ["중복없음", "자주탐색해야할때"]
'''
set_ = {1,2,3,4,5}
print(set_.pop())


# print(dir(dict_))
# test_my_value(dict_)

'''조건문 
drink = {
   "물" : "500",
   "솔의눈","700"
   "포카리","800"
   "카스제로":"1000"
}
그럼 딕트에서 해당하는 것이 있는지 없는지 찾는 함수를 이용한다. 
    def find_product() return Bool  

찾았다면 유저가 낸 돈에서 물품금액을 뺀 금액을 구하고 거스름돈을 반환한다. 
    def serv_product() return ""
    def change_money() return user_money - product_price   
'''

user_money = int(input("돈내놔 =>"))
user_select = input("뭐먹을래?")

if user_money >= 500 and user_select =='물':
    print("물")
    user_money = user_money - 500
    # print("거스름돈 {} 입니다.", user_money)

elif user_money >=400 and user_select == '껌':
    print("껌")
    user_money = user_money - 400
    # print("거스름돈 {} 입니다.", user_money)
else:
    print("아무것도 구매하지 못했습니다.")

print(user_money)