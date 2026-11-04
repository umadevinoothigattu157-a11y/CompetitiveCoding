t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    grid =[input()for i in range(n)]
    minr = n 
    maxr = -1
    minc = m 
    maxc = -1 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                minr = min(minr,i)
                maxr = max(maxr,i)
                minc = min(minc,j)
                maxc=max(maxc,j)
    area = (maxr-minr+1)*(maxc-minc+1)
    print(area)
