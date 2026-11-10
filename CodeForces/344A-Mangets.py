
n = int(input())

prev = input()
count = 1

for i in range(n - 1):
    curr = input()

    if curr != prev:
        count += 1

    prev = curr

print(count)
