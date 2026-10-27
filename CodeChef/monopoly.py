t = int(input())
for _ in range(t):
    p,q,r,s = map(int,input().split())
    total = p+q+r+s 
    if p > total -p or q>total-q or r>total-r or s>total-s:
        print("YES")
    else:
        print("NO")
