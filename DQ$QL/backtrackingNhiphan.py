n = int(input())
A = [0] * n

def VT(i):
    for j in range(2):
        A[i] = j
        if i == n - 1:
            print(''.join(map(str, A)))
        else:
            VT(i + 1)
VT(0)
