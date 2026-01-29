def sovle():
    n=input()
    dung=['0','1','2']
    for i in n:
        if i not in dung:
            return "NO"
    return "YES"
for t in range(int(input())):
    print(sovle())