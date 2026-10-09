# cook your dish here
t = int(input())
for _ in range(t):
    li = list(map(int,input().split()))
    if li.count(0) >= 2:
        print("Water filling time")
    else:
        print("Not now")
