def UC(n,m):
    ucnn=1
    for i in range(min(m,n),1,-1):
        if m%i==0 and n%i==0:
            ucnn = i
            break
    return ucnn
a = input().split(" ")
A=list(map(int,a))
while A[2]!=0:
    A[2]= A[2] - UC(A[0],A[2])
    if A[2]==0:
        print("0")
    A[2] = A[2] - UC(A[1], A[2])
    if A[2] == 0:
        print("1")