n = int(input())
arr = list(map(int,input().split()))
seen = set()
for x in arr:
    if x not in seen:
        print(x,end=" ")
        seen.add(x)
