for _ in range(int(input())):
    st=[]
    cnt=1
    dictt={}
    ar=input()
    kq=[]
    for i in range(len(ar)):
        if ar[i]=='(':
            st.append(i)
            dictt[i]=cnt
            kq.append(cnt)
            cnt+=1
        elif ar[i]==')':
            k=st.pop()
            kq.append(dictt[k])
    for i in kq: print(i,end=' ')
    print()