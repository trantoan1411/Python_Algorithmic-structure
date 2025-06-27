n = int(input())
m = int(n/2)
A= input()
dem=0
t1=0
t2=0
for i in range(m):
    t1 += int(A[i])
    if A[i] != "4" and A[i]!= "7":
        dem += 1
for i in range(m,n):
    t2 += int(A[i])
    if A[i] != "4" and A[i]!= "7":
        dem+=1
if dem > 0 or t1 != t2:
    print("NO")
else:
    print("YES")
