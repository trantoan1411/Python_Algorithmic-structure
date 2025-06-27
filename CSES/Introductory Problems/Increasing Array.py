a = int(input())
b = input().split(" ")
c = list(map(int,b))
i=0
dem=0
k=1
while i+k < a:
    if c[i] > c[i+k]:
        dem +=c[i]-c[i+k]
        k+=1


    else:
        i += k
        k = 1
print(dem)


