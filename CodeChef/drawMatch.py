t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    if x>0 and y > 0 and x== y:
        print("YES")
    else:
        print("NO")
