c = int(input())
m = [0]*(c+1)
n = [0]*(c+1)
for k in range(1,c+1):
    a=input().split(" ")
    m[k]=int(a[0])
    n[k]=int(a[1])
for i in range(1,c+1):
    if m[i] > n[i]:
        if m[i] % 2 ==0:
            print(m[i]*m[i]-n[i]+1)
        else:
            print((m[i]-1)*(m[i]-1)+n[i])
    else:
        if n[i] % 2 ==0:
            print((n[i]-1)*(n[i]-1)+m[i])
        else:
            print(n[i]*n[i]-m[i]+1)





