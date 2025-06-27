n = int(input())
A = [0] * n


def TT (i, s):
    for j in range(1, n + 1):
        A[i] = j
        if s + j == n:
            print(A)
            A[i] = 0
            return
        else:
            TT(i + 1, s + j)

TT(0, 0)
