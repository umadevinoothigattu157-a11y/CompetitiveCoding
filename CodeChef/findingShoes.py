# cook your dish here
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print((n*2)-min(m,n))
