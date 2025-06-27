a=input()
A=[""]*len(a)

def VT(i):
    for j in a:
        A[i] = j
        if i == len(a) - 1:
            print(A)
        else:
            VT(i + 1)
VT(0)






























