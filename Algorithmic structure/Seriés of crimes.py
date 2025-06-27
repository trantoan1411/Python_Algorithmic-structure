m = input().split(" ")
A = []
for i in range(int(m[0])):
    k = input()
    A.append(k)
p = {}
p2 = {}
for a in range(int(m[0])):
    for b in range(int(m[1])):
        if A[a][b] == "*":
            if a in p:
                p[a] += 1
            else:
                p[a] = 1
            if b in p2:
                p2[b] += 1
            else:
                p2[b] = 1
for k in p:
    if p[k] == 1:
        c=k+1
for l in p2:
    if p2[l] == 1:
        d=l+1
print(f"{c} {d}")


