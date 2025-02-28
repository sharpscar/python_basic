a = input("a의 값을 입력하세요 (정수 )")
b = input("b의 값을 입력하세요 (정수 )")
c = input("c의 값을 입력하세요 (정수 )")

if a.isdigit() !=False and b.isdigit()!=False and c.isdigit() !=False:
    a = int(a)
    b = int(b)
    c = int(c)
else:
    input("숫자로 재입력하세요 ")

if a > b :
    if a > c :
        print("a가 최대값")
    else:
        print("c가 최대값")
else:
    # a < b
    if b > c:
        print("b가 최대값")
    else:
        print("c가 최대값")