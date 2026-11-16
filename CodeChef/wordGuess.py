
T = int(input())

for _ in range(T):
    S = input()
    R = input()

    M = ""

    for i in range(5):
        if S[i] == R[i]:
            M += "G"
        else:
            M += "B"

    print(M)
