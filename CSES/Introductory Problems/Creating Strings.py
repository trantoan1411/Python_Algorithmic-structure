def S(A):
    if len(A) == len(s):
        if A in m:
            return
        else:
            m[A] = True
            v.append(A)
    for i in range(len(s)):
        if not c[i]:
            print(c)
            print(s[i])
            c[i] = True
            S(A + s[i])
            c[i] = False
s = input()
c = [False] * len(s)
m = {}
v = []

S('')

print(len(v))
v.sort()
for i in v:
    print(i)
