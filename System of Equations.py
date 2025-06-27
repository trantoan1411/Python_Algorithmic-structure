m= input()
n= m.split(" ")
k = list(map(int,n))
dem=0
for a in range(100):
    for b in range(100):
        if a**2 + b == k[0] and b**2 + a ==k[1]:
            dem+=1
print(dem)