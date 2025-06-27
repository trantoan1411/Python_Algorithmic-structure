n = int(input())
a=input().split(" ")
A=list(map(int,a))
for i in range(n):
    if A[i] == max(A):
        break
for j in range(len(A)-1,0,-1):
    if A[j] == min(A):
        break
if i > j:
    print(i + n - j - 2 )
else:
    print(i + n - j - 1)




