def check(a):
    for i in range(len(a)-1):
        if int(a[i])>int(a[i+1]):
            return "NO"
    return "YES"
for t in range(int(input())):
    n=input()
    print(check(n))
