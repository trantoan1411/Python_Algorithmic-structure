A = []
for i in range(5):
    a = int(input())
    A.append(a)
dem=0
for i in range(A[4]):
    k = 0
    while k < (5):
        if i % A[k] ==0:
            dem+=1
            break
        else:
            k+=1
print(dem)