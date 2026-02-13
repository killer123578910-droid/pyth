n=input()
m=input()
k=int(input())
temp1=n[:k-1]
temp2=n[k-1:]
ans=temp1+m+temp2
print(ans)