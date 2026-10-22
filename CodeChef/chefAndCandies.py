t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    if x > n:
        print(0)
    else:
        if (n-x) % 4 == 0:
            print((n-x)//4)
        else:
            print(((n-x)//4)+1)
