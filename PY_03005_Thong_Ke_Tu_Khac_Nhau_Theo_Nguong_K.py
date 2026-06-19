import re
n,k=map(int,input().split())
dect={}
for i in range(n):
    l=re.split(r'[^a-zA-Z0-9]',input().strip())
    for ko in l:
        if ko.lower() not in dect and ko!='':
            dect[ko.lower()]=0
        if ko!='':dect[ko.lower()]+=1 

kq=dict(sorted(dect.items(),key=lambda x:(-x[1],x[0])))
for i,z in kq.items():
    if z>=k:
        print(f'{i} {z}')
    