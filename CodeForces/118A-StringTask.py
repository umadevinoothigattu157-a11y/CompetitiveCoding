s = input().lower()
res=""
for ch in s:
    if ch not in "aeioyu":
        res +="."+ch
print(res)
