t=int(input())
m=[]
n=[]
for i in range(t):
    a=input().split(" ")
    m.append(int(a[0]))
    n.append(int(a[1]))
for k in range(t):
    if (m[k]+n[k])%3==0 and abs(m[k]-n[k])<= min(n[k],m[k]):
        print("YES")
    else:
        print("NO")
