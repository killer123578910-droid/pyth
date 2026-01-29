t = int(input())
while t>0:
    s = input()

    minnum = 1000000
    temp = ""

    for ch in s:
        if ch.isdigit():
            temp += ch
        else:
            if temp:
                minnum = min(minnum, int(temp))
                temp = ""

    # xử lý số ở cuối chuỗi
    if temp:
        minnum = min(minnum, int(temp))

    print(minnum)
    t-=1
