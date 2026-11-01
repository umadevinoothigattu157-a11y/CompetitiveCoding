t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a * 2> b:
        print("FIRST")
    elif a*2<b:
        print("SECOND")
    else:
        print("ANY")
