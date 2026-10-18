
t = int(input())

for _ in range(t):
    n = int(input())
    income = n * 50
    expenses = income * 70 // 100
    profit = income - expenses
    print(profit)
