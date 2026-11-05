t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    ages = list(map(int,input().split()))
    count = 0
    for age in ages:
        if age>=x:
            count+=1
    print(count)
