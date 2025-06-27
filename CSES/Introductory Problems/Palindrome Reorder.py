def reverse(string):
    string = "".join(reversed(string))
    return string
A=input()
p={}
B=""
for i in A:
    if i in p:
        p[i]+=1
    else:
        p[i]=1
for j in p:
    if p[j]%2==0:
        B+= j* (p[j]//2)
d=0
c=""
for k in p:
    if p[k]%2!=0:
        c=k*p[k]
        d+=1
if d > 1:
    print("NO SOLUTION")
else:
    print(B+c+reverse(B))

