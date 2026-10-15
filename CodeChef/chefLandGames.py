# cook your dish here
t = int(input())
for _ in range(t):
    li = list(map(int,input().split()))
    for i in li:
        if i == 1:
            print("OUT")
            break
    else:
        print("IN")
    
