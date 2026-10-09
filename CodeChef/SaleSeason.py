# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    if n <=100:
        print(n)
    elif n <= 1000:
        print(n-25)
    elif n <= 5000:
        print(n-100)
    else:
        print(n-500)
    
