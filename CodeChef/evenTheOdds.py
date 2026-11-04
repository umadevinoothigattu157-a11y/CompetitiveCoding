t = int(input())
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    max_len = 0
    for i in range(n):
        count = 0
        for j in range(i,n):
            if a[j]%2 != 0:
                count+=1
            if count % 2 == 0:
                max_len = max(max_len,j-i+1)
    print(max_len)
