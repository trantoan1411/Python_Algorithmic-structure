n= int(input())
A= []
for i in range(n):
    a = input().split(" ")
    for k in a:
        A.append(k)
dem = 0
max = int(A[len(A)-2])
for j in range(1,len(A)-3,2):
    dem += int(A[j])
    if dem > max:
        max = dem
    dem-=int(A[j+1])
print(max)

