n = int(input())
a = input().split(" ")
A = list(map(int,a))
B=[1] * n
for i in range(len(A)):
    B[A[i]-1] = i+1
C=list(map(str,B))
print(" ".join(C))

