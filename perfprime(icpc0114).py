def snt(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
            
def solve():
    n=input()
    temp=0
    for i in n:
        if not snt(int(i)):
            return "No"
        temp+=int(i)
    return "Yes" if snt(int(n)) and snt(int(n[::-1])) and snt(temp) else "No"
for t in range(int(input())):
    print(solve())

