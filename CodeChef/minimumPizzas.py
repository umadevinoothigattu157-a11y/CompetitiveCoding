from math import ceil
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    val = n*x 
    ans = ceil(val /4)
    print(ans)
