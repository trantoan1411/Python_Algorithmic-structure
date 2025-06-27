n = int(input())
a = 0
b = 0
A=""
B=""
d1=0
d2=0
if n ==1:
    print("NO")
if n % 2 == 1 :
    for i in range(1,n,4):
        a+= i + i +1
        A += " "+str(i)
        A+=" "+str(i+1)
        d1 += 2
    for j in range(3,n+1,4):
        if j<n-1:
            b += j + j + 1
            B += " " + str(j)
            B += " "+ str(j + 1)
            d2 += 2
        else:
            b += j
            B += " " + str(j)
            d2 += 1

else:
    a=1+n
    d1=2
    for i in range(4,n,4):
        a += i + i +1
        A += " "+str(i)
        A+=" "+str(i+1)
        d1 += 2
    for j in range(2,n,4):
        b += j + j + 1
        B += " "+str(j)
        B += " " +str(j + 1)
        d2 += 2
    A="1"+A+" "+str(n)
if a !=b:
    print("NO")
else:
    print("YES")
    print(d1)
    print(A.strip())
    print(d2)
    print(B.strip())