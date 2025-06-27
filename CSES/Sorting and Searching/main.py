A = []
for i in range(8):
    a = list(input())
    A.append(a)
def KT(a, b):
    d = 0
    for c in range(len(X)):
        if a == X[c] or b == Y[c] or a - b == (X[c] - Y[c]) or a + b == (X[c] + Y[c]):
            d += 1
    if d > 0:
        return False
    else:
        return True
X=[]
Y=[]
dem=0
def gen(i):
    if len(X) == 8:
        print(Y)

    t=0
    for j in range(8):
        if KT(i, j) == True and A[i][j]==".":
            t+=1
            X.append(i)
            Y.append(j)
            gen(i+1)
            t=0
    if t == 0:
        if len(X)>0:
            X.pop(len(X)-1)
            Y.pop(len(Y)-1)

gen(0)


