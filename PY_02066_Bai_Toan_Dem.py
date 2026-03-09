n=int(input())
ar=[]
while len(ar)<n:
    ar.extend(list(map(int,input().split())))
lene=max(ar)
dic={}
for i in range(1,lene+1):
    if i not in dic:
        dic[i]=0
for i in ar:
    dic[i]+=1
flag=1
for i in dic.keys():
    if dic[i]==0:
        print(i)
        flag=0
if flag:
    print("Excellent!")