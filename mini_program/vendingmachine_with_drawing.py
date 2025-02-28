inserted_money=input("돈입력")
inserted_money = int(inserted_money)

#자판기 재고 확인 - quantity가 1이상인경우

#사용자가 메뉴를 선택
menu = [
{'p_name':'포카리','p_price':1500,'quantity':100 },
{'p_name':'환타','p_price':1300,'quantity':100 },
{'p_name':'사이다','p_price':1400,'quantity':100 },
{'p_name':'코카콜라','p_price':2000,'quantity':100 },
{'p_name':'파워에이드','p_price':1600,'quantity':100 },
{'p_name':'밀키스','p_price':900,'quantity':100 }
]
str_=''
for idx, val in enumerate(menu):
    str_ +=val['p_name'] + "   "+str(val['p_price'])+"(₩)\n"

print(str_)