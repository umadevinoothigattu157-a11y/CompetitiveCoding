n,k = map(int,input().split())
scores = list(map(int,input().split()))
threshold = scores[k-1]
count = 0
for x in scores:
   if x >= threshold and x > 0:
        count += 1
print(count)
