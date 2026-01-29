for t in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    m1=m2=m3=100000000
    for x in a:
        if x<m1:
            m3=m2
            m2=m1
            m1=x
        elif x<m2:
            m3=m2
            m2=x
        elif x<m3:
            m3=x
    print(m1+m2+m3)