fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']

# for flavor in flavor_list:
#     print(f'{flavor} 맛있어요.')
#range 를 사용하는 방법
#
# for i in range(len(flavor_list)): #range(4)
#     flavor = flavor_list[i]
#     print(f'{i+1} : {flavor}')
#
# for i, flavor in enumerate(flavor_list):
#     print(f'{i+1}: {flavor}')
#


# for index, value in list(enumerate(fruits)):
#     print(index, value)


# start = 0
# for _ in fruits:
#     print(start, _)
#     start +=1

'''
index메서드는 중복값이 있는 경우에 첫번재 값만 반환하는 특성이있다.  
'''
#
# for i in fruits:
#   print("{0} {1}".format(fruits.index(i),i), end = " ")

names = ['Cecilia', '남궁민수', '毛泽东']
counts = [len(n) for n in names] #각 요소의 크기를 리스트에 넣는다.
print(counts)
