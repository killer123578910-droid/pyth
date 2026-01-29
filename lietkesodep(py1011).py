def solve():
    n=int(input())
    queue=[]
    queue.append('2')
    queue.append('4')
    queue.append('6')
    queue.append('8')
    while bool(queue):
        front=queue[0]
        queue.pop(0)
        if 22 <= int(front+front[::-1]) < n:
            print(int(front+front[::-1]),end=" ")
        newfront0=front+'0'
        newfront1=front+'2'
        newfront2=front+'4'
        newfront3=front+'6'
        newfront4=front+'8'
        if int(newfront0+newfront0[::-1])<n:
            queue.append(newfront0)
        if int(newfront1+newfront1[::-1])<n:
            queue.append(newfront1)
        if int(newfront2+newfront2[::-1])<n:
            queue.append(newfront2)
        if int(newfront3+newfront3[::-1])<n:
            queue.append(newfront3)
        if int(newfront4+newfront4[::-1])<n:
            queue.append(newfront4)
    print()
for t in range(int(input())):
    solve()     
    