n=int(input())
A=[]
for a in range(n):
    i = int(input())
    A.append(i)

def ts(v):
    a, b = [0, 1], [0, 9]
    i = 1
    while b[i] < v:
        i += 1
        a.append(a[i - 1] * 10)
        b.append(a[i] * i * 9 + b[i - 1])
    d = v - b[i - 1]
    num = a[i] + d // i
    if d % i == 0:
        num -= 1
    s = str(num)
    if d % i == 0:
        print(s[len(s) - 1])
    else:
        print(s[d % i - 1])
for k in A:
    ts(k)


