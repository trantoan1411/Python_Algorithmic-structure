n=int(input())
B=[]
for i in range(n):
    k = input()
    A = k.split(" ")
    B.append(A)
m = (n+1)/2
C = 0
for a in range(n):
    for b in range(n):
        if a == m-1 or b == m-1 or a+b == n-1 or a==b:
            c = B[a][b]
            C += int(c)
print(C)