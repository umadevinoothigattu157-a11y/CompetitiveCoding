for i in range(5):
    a = list(map(int,input().split()))
    if 1 in a:
        row = i+1
        col = a.index(1)+1
print(abs(row-3)+abs(col-3))
