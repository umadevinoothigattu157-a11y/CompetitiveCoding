s = input()
lower = 0
upper = 0
for ch in s:
    if ch.isupper():
        upper+=1
    else:
        lower+=1
if upper > lower:
    print(s.upper())
else:
    print(s.lower())
