t = int(input())
count = 0
for _ in range(t):
    li = list(map(int,input().split()))
    if li.count(1)>= 2:
        count += 1
print(count)
