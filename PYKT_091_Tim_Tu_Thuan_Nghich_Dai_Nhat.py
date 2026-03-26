def thuannghich(n):
    return n == n[::-1]

f = open("VANBAN.in",'r')

dic = {}
maxlen = 0
chose = ''

for i in f:
    for e in i.split():
        if thuannghich(e):   # ❗ bỏ điều kiện maxlen
            if len(e) > maxlen:
                dic.clear()
                dic[e] = 1
                chose = e
                maxlen = len(e)
            elif len(e) == maxlen:
                if e not in dic:
                    dic[e] = 0
                dic[e] += 1

for i in dic:
    print(i,dic[i])