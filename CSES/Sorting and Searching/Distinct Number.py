n = int(input())
A = input().split(" ")
p={}
dem=0
for i in A:
    if i not in p:
        dem+=1
        p[i]=1
print(dem)
