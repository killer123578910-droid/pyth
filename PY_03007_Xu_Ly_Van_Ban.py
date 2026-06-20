import re
import sys
kq = sys.stdin.read()
kq=re.split(r'[.!?]',kq)
for i in kq:
    l=i.lower().split()
    if not l: continue
   
    l[0]=l[0].title()
    ke=" ".join(l)
    print(ke)