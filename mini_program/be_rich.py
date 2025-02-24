import math
'''
10만 달러 만들기
20250225 기준
143,713,000원
1억 4,371만 3,000원
만약 월 700000원 씩 적금을 한다고 상정해보자
'''

my_objective = 143713000

monthly_savings = 700000

how_long_month = my_objective / monthly_savings

#올림한다.
how_long_month = math.ceil(how_long_month)

# 몇년이나 걸릴까
how_long_year = how_long_month /12

print(how_long_month)
