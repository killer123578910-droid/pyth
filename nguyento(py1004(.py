def gcdc(a,b):
    return a if b==0 else gcdc(b,a/b)
print(gcdc(20,40))