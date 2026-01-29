def sovle():
    x=int(input())
    if x%2==0:
        summ=0
        for i in range(2,x+1,2):
            summ+=float(1/i)
        print("{:.6f}".format(summ))
    else:
        summ=0
        for i in range(1,x+1,2):
            summ+=float(1/i)
        print("{:.6f}".format(summ))
for t in range(int(input())):
    sovle()