t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    li = list(map(int,input().split()))
    i = 0
    handShakeCount = 0
    count = 0
    people = 0
    li.sort()
    for i in li:
        newPeople = people+i
        handShakeCount = (newPeople*(newPeople-1))//2
        if handShakeCount<=m:
            people = newPeople
            count += 1
    print(count)
        
        
