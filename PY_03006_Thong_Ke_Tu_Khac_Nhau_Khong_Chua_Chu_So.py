import re
import re
n=int(input())
dect={}
for i in range(n):
    l=re.split(r'[^a-z]',input().lower())
    for ko in l:
        if ko not in dect and ko!='' and ko.isalpha():
            dect[ko]=0
        if ko!='' and ko.isalpha():dect[ko]+=1 

kq=dict(sorted(dect.items(),key=lambda x:(-x[1],x[0])))
for i,z in kq.items():
    print(f'{i} {z}')
    