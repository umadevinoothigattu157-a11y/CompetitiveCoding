t = int(input())
for _ in range(t):
    n = int(input())
    arr =  list(map(int,input().split()))
    count = 0
    for x in arr:
        if x >= 1000:
            count+=1
    print(count)
