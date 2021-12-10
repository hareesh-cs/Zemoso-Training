def add(a,b,*c):
    s=0
    for i in c:
        s+=i
    return a+b+s

print(add(2,3,5,6,7))