import re
dice={}
for _ in range(int(input())):
    i=re.split(r'[^a-zA-Z0-9]',input().strip())
    for x in i:
        if x.lower() not in dice and x!='':
            dice[x.lower()]=0
        if x!='': dice[x.lower()]+=1
kq=dict(sorted(dice.items(),key=lambda x:(-x[1],x[0])))
for i,k in kq.items():
    print(f'{i} {k}')