t = int(input())
for _ in range(t):
    n,s = map(int,input().split())
    ans = -1
    for c in range(n+1):
        w=4*c-s
        if 0<= w<=n-c:
            ans = c+w
            break
    print(ans)
