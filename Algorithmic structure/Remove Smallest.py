n = int(input())
A = []
for i in range(n):
    a = int(input())
    b = input().split(" ")
    c = list(map(int, b))
    A.append(c)
#hàm sắp xếp
def sapxep(D):
    for d1 in range(len(D)):
        for d2 in range(d1 , len(D)):
            if D[d1] < D[d2]:
                tg = D[d2]
                D[d2] = D[d1]
                D[d1] = tg
    return D
for j in range(len(A)):
    sapxep(A[j])
    dem = 0
    for k in range(len(A[j])-1):
        if abs(A[j][k] - A[j][k+1]) > 1:
            dem += 1
    if dem > 0:
        print("NO")
    else:
        print("YES")

