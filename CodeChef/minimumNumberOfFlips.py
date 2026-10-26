t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if s % 2!= 0:
        print(-1)
    else:
        print(abs(s)//2)
