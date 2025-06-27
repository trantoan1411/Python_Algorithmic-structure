A=input().strip()
B=input().strip()
C=input().strip()
D=A+B
p1={}
p2={}
dem=0
for t in C:
    if t not in D:
        dem+=1
for i in D:
    if i in p1:
        p1[i]+=1
    else:
        p1[i]=1
for j in C:
    if j in p2:
        p2[j]+=1
    else:
        p2[j]=1
for k1 in p1:
    if k1 in p2:
        if p1[k1] != p2[k1]:
            dem+=1
if dem !=0 or len(D) != len(C):
    print("NO")
else:
    print("YES")
