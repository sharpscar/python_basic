'''
실업급여를 받는 간단한 프로그램입니다.
2월 현재까지 받은 금액은 aready_paid_money
총할당된 급여액은 total
아직 지급받지 못한  급여액 remain_money
'''

day_won = 60000

min_month = 4

remain_money = 0



aready_paid_money = 900000

def calc_total_pay():
    total = day_won * 4 *30
    print(f"총 할당된 실업급여액은  {total}, 그리고 이미 받은 실업급여액은 {aready_paid_money}")
    return total
def remain_pay(val):
    print("남은 실업급여 액은 ?")
    remain_money = val - aready_paid_money
    print(remain_money)

total = calc_total_pay()
remain_pay(total)
