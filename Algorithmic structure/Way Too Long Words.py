n = int(input())
A=[]
for i in range(n):
    a=input()
    A.append(a)
for k in A:
    if len(k) < 11:
        print(k)
    else:
        print(k[0]+str(len(k)-2)+k[len(k)-1])






