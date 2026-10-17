t = int(input())
for _ in range(t):
    a,b,x,y = map(int,input().split())
    cr = a*b 
    mh = x*y 
    if mh >= cr:
        print("Yes")
    else:
        print("No")
