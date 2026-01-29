def sovle():
    n=input().strip()
    freq={"4":0,"7":0}
    for x in n:
        if x == '4' or x=='7':
            freq[x]+=1
    return "YES" if freq['4']+freq['7']==4 or freq['4']+freq['7']==7 else "NO"
print(sovle())