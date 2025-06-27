n = input().split(" ")
A = list(map(int, n))
print(A)
for i in range(len(A)):
    a = (A[1]*A[2]) // A[6]
    b =  A[3]*A[4]
    c =  A[5]*A[7]
if a < b:
    if  a < c:
        print(a//A[0])
    else:
        print(c//A[0])
else:
    if b < c:
        print(b//A[0])
    else:
        print(c//A[0])
print(f"{a},{b},{c}")



