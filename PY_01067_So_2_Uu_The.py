from collections import deque
def check(k):
    cnt=0
    moc=len(k)//2+1
    for i in k:
        if i=='2':
            cnt+=1
        if cnt>=moc:
            return True
    return False
    
for i in range(int(input())):
    n=int(input())
    ar=deque()
    them=['0','1','2']
    ar.append('1')
    ar.append('2')
    i=0
    while i<n and ar:
        top=ar.popleft()
        if check(top):
            print(top,end=" ")
            i+=1
        for j in them:
            ar.append(top+j)
    print()
        