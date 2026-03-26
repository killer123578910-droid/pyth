f=open("CONTACT.in",'r')
dic=set()
for line in f:
    str=(line.strip()).lower()
    if str not in dic:
        dic.add(str)
for k in sorted(dic):
    print(k)