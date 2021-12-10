def sub(a,b,*c):
    d=0
    for i in c:
        d-=i
    return a-b-abs(d)

print(sub(13122,13,121,6,534,4536,78,3201,2653,1,7,54,667))