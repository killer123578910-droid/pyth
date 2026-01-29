def solve():
    n=input()
    sumn=0
    for i in n:
        sumn+=int(i)
    if sumn<10:
        return "NO"
    summ=str(sumn)
    for i in range(int(len(summ)/2)+1):
        if summ[i]!=summ[len(summ)-1-i]:
            return "NO"
    return "YES"
for t in range(int(input())):
    print(solve())