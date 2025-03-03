# 9,2,1,3

def solution(numer1, denom1, numer2, denom2):
    #분모끼리 같지 않으면 곱
    if denom1 != denom2 :
       denom = denom1 * denom2 # 분모를 같게해줌
       numer1 = numer1 * denom2 # 분자1의 값을 구함 1 * 4
       numer2 = numer2 * denom1 # 분자 2의 값을 구함 2 * 3
    else:
        denom = denom1

    numer = numer1 + numer2
    # 원래 약분할 약수를 먼저 구하는게 아니라 소수인지 아닌지 판별이 우선이지만 약수가 있는지 체크하려면 먼저 약수들을 구해봐야 아니까..
    denom_list = get_div(denom)
    numer_list = get_div(numer)

    # 분모나 분자가 소수인경우 약분할 필요 없다. 소수 구하는 방법? 만약 get_div()함수를 거쳤으나 빈 리스트가 나온경우
    if len(denom_list) == 2 or len(numer_list) == 2:
        answer = [int(numer), int(denom)]
    else:

        measure = 0
        del denom_list[-1]
        del denom_list[0]
        del numer_list[-1]
        del numer_list[0]

        for i in denom_list:
            if i in numer_list:
                measure = i
        answer = [int(numer / measure), int(denom / measure)]
    return answer




#약수 구하는 함수
def get_div(n):
    divi = []
    for i in range(1, n+1):
        if n % i == 0:
            divi.append(i)

    return divi
'''
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/sharpscar/python_basic.git/'
'''