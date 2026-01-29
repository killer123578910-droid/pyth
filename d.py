def isnum(st):
 return st>="0" and st<="9"
t=int(input())
while t>0:
 str=input()
 maxnum=1000000
 for i in range(0,len(str)):
  if isnum(st[i]):
   while isnum(st[i]):
    