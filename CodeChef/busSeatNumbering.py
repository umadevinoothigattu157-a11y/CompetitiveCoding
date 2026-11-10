# cook your dish here

T = int(input())

for _ in range(T):
    N = int(input())

    if N <= 15:
        deck = "Lower"
        if N <= 10:
            seat = "Double"
        else:
            seat = "Single"
    else:
        deck = "Upper"
        if N <= 25:
            seat = "Double"
        else:
            seat = "Single"

    print(deck, seat)
