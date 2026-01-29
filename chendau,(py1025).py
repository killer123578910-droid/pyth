def solve():
    x=input()
    cnt=0
    ans=''
    for i in range(len(x)-1,-1,-1):
        if cnt<3:
            ans=x[i]+ans
            cnt+=1
        else:
            ans=x[i]+','+ans
            cnt=1
    return ans
print(solve())