a = input().split(" ")
n=int(a[0])
m=int(a[1])
i=1

while m > i-1:
    m -=  i
    if i < n:
        i += 1
    else:
        i = 1

print(m)




