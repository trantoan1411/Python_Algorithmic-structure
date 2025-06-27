a = input().split(" ")
n=int(a[0])
m=int(a[1])
def KTSNT(n):
    dem=0
    for i in range(1,n+1):
        if n % i ==0:
            dem+=1
    if dem < 3:
        return True
    else:
        return False
d=0
for k in range(n,m+1):
    if KTSNT(k) == True:
        d+=1
if d <= 2 and KTSNT(m) == True and KTSNT(n)==True:
    print("YES")
else:
    print("NO")
