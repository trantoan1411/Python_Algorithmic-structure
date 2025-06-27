n = int(input())
k = str(n)
while n != 1:
    if n % 2==0:
        n = n/2
        k = k + " " + str(int(n))
    else:
        n= n*3+1
        k= k+" "+str(int(n))
print(k)

