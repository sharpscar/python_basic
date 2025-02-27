'''
동행복권 사이트로부터 로또 1회차부터 최신회차까지
번호를 가져와서 csv 파일에 저장하는 기능
- 본인이 직접 작성한 프로그램이 아님을 밝힙니다.

'''

from datetime import datetime
import requests

from bs4 import BeautifulSoup
import pandas as pd

# 10회차 데이터 크롤링
count  =10

url = f'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}'
html = requests.get(url).text
soup= BeautifulSoup(html,'lxml')


# <p class="desc">(2003년 02월 08일 추첨)</p>
date = datetime.strptime(soup.find('p',class_='desc').text,'(%Y년 %m월 %d일 추첨)')

numbers = soup.find('div', attrs={'class':'num win'}).find('p').text.strip().split('\n')
# 배열안의 요소들 인트형으로 변경
numbers = [int(i) for i in numbers]

bonus_number = soup.find('div', attrs ={'class':'num bonus'}).find('p').text.strip()

# 1~5등 정보 추출
winer_5 = soup.find('table', attrs ={'class':'tbl_data'})
# df = pd.read_html(str(winer_5))[0]

def crawling_lotto(count):
    url= f'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    date = datetime.strptime(soup.find('p', class_='desc').text, '(%Y년 %m월 %d일 추첨)')
    win_number =[ int(i) for i in soup.find('div', attrs={'class':'num win'}).find('p').text.strip().split('\n')]
    bonus_number = soup.find('div', attrs ={'class':'num bonus'}).find('p').text.strip()

    return {
        'date' : date,
        'win_number': win_number,
        'bonus_number': bonus_number
    }

result = crawling_lotto(2)
print(result)