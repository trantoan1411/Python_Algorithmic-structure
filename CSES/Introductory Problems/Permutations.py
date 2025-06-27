n=int(input())
a=""
b=""
if n > 3 or n==1:
    for i in range(1,n+1):
        if i % 2 == 0:
            a += str(i)+" "
        else:
            b+= str(i)+" "


    print(a+b)
else:
    print("NO SOLUTION")


